import csv
import re
import os
import glob

for filename in glob.glob('../originals/*/*.csv'):
    if 'output' not in filename:
        with open(filename, 'r') as file:

            output_dir = os.path.join('../output', os.path.basename(os.path.dirname(filename)))
            os.makedirs(output_dir, exist_ok=True)
            
            output_file = os.path.join(output_dir, 'output_' + os.path.basename(filename))
            
            with open(output_file, 'w', newline='') as outfile:
                reader = csv.DictReader(file)
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['Field'] == 'handle':
                        default_matches = re.findall(r'[\w-]+$', row['Default content'])
                        translated_matches = re.findall(r'[\w-]+$', row['Translated content'])
                        if default_matches and translated_matches:
                            default_slug = default_matches[0]
                            translated_slug = translated_matches[0]
                            if default_slug != translated_slug:
                                row['Translated content'] = ''
                    writer.writerow(row)