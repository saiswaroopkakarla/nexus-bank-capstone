import gzip
import shutil
#To avoid large file issues in the git, this is a utility to compress the files into .gz format
#data/cleaned/eurusd_fx_cleaned.csv
#data/cleaned/spy_stock_cleaned.csv
#data/cleaned/credit_card_fraud_cleaned.csv

#data/raw/eurusd_fx_cleaned.csv
#data/raw/spy_stock.csv
#data/raw/credit_card_fraud.csv

input_file = 'data/raw/credit_card_fraud.csv'
output_file = input_file + '.gz'

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print(f"Compressed: {output_file}")
