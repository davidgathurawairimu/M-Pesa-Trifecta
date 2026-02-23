import re
import csv

def extract_mpesa_data(messages):
    # Regex pattern to capture Amount, Recipient Name, and Date
    pattern = r"Ksh([\d,]+\.\d{2})\s+paid to\s+(.*?)\.\s+on\s+(\d{1,2}/\d{1,2}/\d{2,4})"
    extracted_data = []
