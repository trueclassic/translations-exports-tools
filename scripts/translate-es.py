import csv
import os
import glob
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../.env")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def translate_text(text):
    try:
      response = client.chat.completions.create(
        model="gpt-4",
        messages=[
          {"role": "system", "content": "Translate only the following if it's text, English text to Spanish. Ignore any text in brackets. Ignore numbers, dates, times and strings you cannot interpret. Only respond if translation is possible. Translate 'Crew Neck T-Shirts', 'Crew Necks' or 'Crews' as 'T-shirts' only! and Never translate 'True Classic'"},
          {"role": "user", "content": text}
        ]
      )
      return response.choices[0].message.content
    except Exception as e:
      print(f"API error: {e}")
      return None

for filename in glob.glob('../originals/ES/*.csv'):
  print(f"Processing file: {filename}")
  if 'output' not in filename:
    with open(filename, 'r', encoding='utf-8') as file:
      output_dir = os.path.join('../output', os.path.basename(os.path.dirname(filename)))
      os.makedirs(output_dir, exist_ok=True)

      output_file = os.path.join(output_dir, 'output_' + os.path.basename(filename))

      with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
          if row['Field'] not in ['url', 'handle'] and row['Type'] not in ['METAFIELD']:
            translated_text = translate_text(row['Default content'])
            row['Translated content'] = translated_text
            print(f"Translated '{row['Default content']}' to '{translated_text}'")

          writer.writerow(row)
          print(f"Wrote row: {row}")
