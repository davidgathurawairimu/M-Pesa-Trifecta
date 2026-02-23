import re
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def extract_mpesa_data(text_content):
    # Regex to capture Amount, Recipient, and Date
    # Handles 'paid to', 'sent to', and 'Give to' variations
    pattern = r"Ksh([\d,]+\.\d{2})\s+(?:paid|sent|give)\s+to\s+(.*?)\s+on\s+(\d{1,2}/\d{1,2}/\d{2,4})"
    messages = text_content.splitlines()
    extracted_data = []

    for msg in messages:
        match = re.search(pattern, msg, re.IGNORECASE)
        if match:
            # Cleaning the numeric amount for calculations
            raw_amount = match.group(1).replace(',', '')
            recipient = match.group(2).strip().rstrip('.')
            
            extracted_data.append({
                "Amount": float(raw_amount),
                "Recipient": recipient,
                "Date": match.group(3)
            })
    return extracted_data

class MpesaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("M-PESA Bulk Extractor")
        self.root.geometry("700x550")
        
        # Main container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Instructions
        ttk.Label(self.main_frame, text="Paste M-PESA Messages Below:", font=('Segoe UI', 11, 'bold')).pack(anchor=tk.W)

        # Text input area
        self.text_area = tk.Text(self.main_frame, wrap=tk.WORD, height=15, font=('Consolas', 10))
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(5, 15))

        # Bottom UI elements
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(fill=tk.X)

        # Submit Button
        self.submit_btn = ttk.Button(self.controls_frame, text="SUBMIT & PROCESS", command=self.handle_submit)
        self.submit_btn.pack(side=tk.LEFT, ipadx=20, ipady=5)

        # Clear Button
        self.clear_btn = ttk.Button(self.controls_frame, text="Clear", command=lambda: self.text_area.delete('1.0', tk.END))
        self.clear_btn.pack(side=tk.LEFT, padx=10)

        # Results Summary Labe
        self.summary_var = tk.StringVar(value="Ready to process...")
        self.summary_label = ttk.Label(self.main_frame, textvariable=self.summary_var, font=('Segoe UI', 10, 'italic'))
        self.summary_label.pack(pady=10, anchor=tk.W)

    def handle_submit(self):
        content = self.text_area.get("1.0", tk.END).strip()
        
        if not content:
            messagebox.showwarning("Empty", "Please paste at least one message.")
            return

        results = extract_mpesa_data(content)

        if not results:
            self.summary_var.set("❌ No valid transactions found.")
            messagebox.showerror("Error", "Could not find any transaction data. Check your message format.")
            return

        # Calculate totals for the summary
        total_count = len(results)
        total_spent = sum(item['Amount'] for item in results)
        self.summary_var.set(f"✅ Found {total_count} transactions. Total: Ksh {total_spent:,.2f}")

        # Prompt to save
        if messagebox.askyesno("Export Data", f"Found {total_count} records. Would you like to save to CSV?"):
            self.save_to_file(results)

    def save_to_file(self, data):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="mpesa_report.csv"
        )

        if file_path:
            try:
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    # Note: Amount is now a float, so we convert back to string for CSV
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    # Apply a slightly more modern look if available
    style = ttk.Style()
    if 'clam' in style.theme_names():
        style.theme_use('clam')
    
    app = MpesaApp(root)
    root.mainloop()
