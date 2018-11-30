# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json

# Convert JSON to Python Object (List)
# ====================================
# JSON data can be directly mapped to a Python list.

array = '{"drinks": ["coffee", "tea", "water"]}'
data = json.loads(array)

for element in data['drinks']:
    print(element)
