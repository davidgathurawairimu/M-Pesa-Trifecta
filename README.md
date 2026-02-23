# M-Pesa-Trifecta
A lightweight Python utility designed to extract the core "trifecta" of M-Pesa transaction data: Amount, Date, and Recipient/Sender Name. Clean, fast, and regex-powered.

M-Pesa-Trifecta is a specialized parser that cuts through the noise of M-Pesa confirmation messages. Instead of dealing with messy strings, this tool isolates the three most critical data points for financial tracking:

Amount: Precision numerical extraction (Float).

Date: Cleaned and standardized timestamps.

Name: Accurate identification of the person or business involved.

Perfect for personal finance trackers, automated bookkeeping, or small business ledger integration.


M-Pesa-Trifecta is a robust Python-based parsing engine designed to transform unstructured M-Pesa SMS confirmations into structured, actionable data.

By focusing on the "Financial Trifecta"—Transaction Amount, Date, and Counterparty Name—this tool strips away the noise of mobile money messages to provide a clean dataset. It is specifically built for users who need to digitize their transaction history for personal budgeting, small business accounting, or data analysis.

🗝️ Key Features
Precision Extraction: Uses optimized Regular Expressions (Regex) to identify and isolate the Amount, Transaction Date, and Recipient/Sender Name from various M-Pesa message formats (P2P, Lipa na M-Pesa, Paybill).

Data Cleaning: Automatically handles currency formatting (e.g., removing "Ksh" and commas) to ensure values are ready for mathematical operations.

CSV Export Engine: seamlessly compiles parsed data into a standardized .csv format, allowing for immediate import into Excel, Google Sheets, or QuickBooks.

Batch Processing: Capable of handling single strings or bulk processing entire logs of exported messages.

📊 How the Data Flows
Input: Raw M-Pesa SMS text (e.g., "QBT451H789 Confirmed. Ksh2,400.00 sent to JANE DOE...")

Process: The Trifecta engine scans and maps the core fields.

Output: A structured CSV row:
| Date | Name | Amount |
| :--- | :--- | :--- |
| 2026-02-23 | JANE DOE | 2400.00 |

💡 Use Cases
Personal Finance: Export your monthly spending to a spreadsheet to track your habits.

Small Businesses: Quickly generate a digital ledger from a business phone's SMS inbox.

Developers: Use the parsing logic as a backbone for larger Fintech applications.
