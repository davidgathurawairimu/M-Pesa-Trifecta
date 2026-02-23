import re
import csv

def extract_mpesa_data(messages):
    # Regex pattern to capture Amount, Recipient Name, and Date
    pattern = r"Ksh([\d,]+\.\d{2})\s+paid to\s+(.*?)\.\s+on\s+(\d{1,2}/\d{1,2}/\d{2,4})"
    extracted_data = []
for msg in messages:
        match = re.search(pattern, msg)
        if match:
            extracted_data.append({
                "Amount": match.group(1),
                "Name": match.group(2),
                "Date": match.group(3)
            })
    return extracted_data

def main():
    print("Paste your M-PESA messages below. Press Enter on an empty line to finish:")
    user_input = []
    while True:
        line = input()
        if not line:
            break
        user_input.append(line)

    results = extract_mpesa_data(user_input)
