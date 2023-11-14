import csv
import re
import glob

for filename in glob.glob('../originals/*/*.csv'):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Field'] == 'handle':
                default_matches = re.findall(r'[\w-]+$', row['Default content'])
                translated_matches = re.findall(r'[\w-]+$', row['Translated content'])