# Translations CLI tools

## Instructions

Save a copy of .env.example as .env and update your OPENAI_API_KEY

Install requirements in root folder with pip:

```pip install os csv glob dotenv openai```

copy your exported csv files in a `language_code`, example: (`DE`) format inside the `originals` folder.

`cd` inside the `scripts/` folder, and run the appropriate script, for exmaple for french:

```python3 translate-fr.py```

the translates csv should populate in the `output` folder and are ready for import directly in Shopify's Translate and Adapt app.