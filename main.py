import pdfplumber #install on project create
import csv

pdf_path = 'RLD-LicenseeList.pdf'
csv_file_path = 'complete_data.csv'

with pdfplumber.open(pdf_path) as pdf, open(csv_file_path, 'w', newline='') as csvfile:
    writer = None
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            if not writer:
                # Initialize CSV writer and write headers if this hasn't been done yet
                writer = csv.writer(csvfile)
                headers = table[0]  # Assuming the first row of the first table contains headers
                writer.writerow(headers)
            for row in table[1:]:  # Skip header row for all tables after the first
                writer.writerow(row)

print("All data extracted and written to CSV successfully.")
