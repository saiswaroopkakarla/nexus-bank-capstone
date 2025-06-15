import gzip
import shutil

input_file = 'data/cleaned/credit_card_fraud_cleaned.csv'
output_file = input_file + '.gz'

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print(f"Compressed: {output_file}")
