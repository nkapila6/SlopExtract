from langstruct import LangStruct
from loader import txtloader

from dotenv import load_dotenv

load_dotenv()

# example from langstruct docs
# Define schema by example
extractor = LangStruct(
    example={
        "sku": "21NXCT01WW",
        "model": "Lenovo ThinkPad X1 Carbon Gen13 Aura Edition",
        "processor": "Intel Core Ultra 7 255U",
        "ram": "32GB",
        "storage": "1TB",
        "os": "Windows 11 Pro",
        "finish": "Black",
        "unit_price": 1699.00,
        "quantity": 129,
    }
)

# input txts
# text = 'Lenovo ThinkPad X1 Carbon Gen13 Aura Edition 14" WUXGA Touchscreen Laptop (Intel Core Ultra 7 255U, 32GB RAM, 1TB SSD, Windows 11 Pro) - Black (21NXCTO1WW)\n\n129\n\n0\n\n$1699.00'
inputs = txtloader("input.txt")

results: list[dict] = []
results = [extractor.extract(i).entities for i in inputs]
print(results)

import json

with open("output.txt", "w") as f:
    json.dump(results, f, indent=4)
