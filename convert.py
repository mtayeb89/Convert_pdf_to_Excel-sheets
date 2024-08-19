import tabula
import pandas as pd

# Convert PDF to CSV
tabula.convert_into('sales2.pdf', 'sales2.csv', output_format='csv', pages='all')

# Read the CSV file
read_file = pd.read_csv('sales2.csv')

# Convert CSV to Excel
read_file.to_excel('sales2.xlsx', index=None, header=True)
