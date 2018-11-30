# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json

# Convert JSON to Python Object (Dict)
# ====================================
# To convert JSON to a Python dict:
json_data = '{"name": "Brian", "city": "Seattle"}'
json_obj = json.loads(json_data)
print(json_obj["name"])
print(json_obj["city"])
