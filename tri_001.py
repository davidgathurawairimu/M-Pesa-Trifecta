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
    if results:
        keys = results[0].keys()
        with open('mpesa_exports.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(results)
        print(f"\nSuccessfully exported {len(results)} records to 'mpesa_exports.csv'.")
    else:
        print("\nNo valid M-PESA transaction data found.")

if __name__ == "__main__":
    main()
