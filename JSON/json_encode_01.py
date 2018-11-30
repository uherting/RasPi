# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json
# from decimal import Decimal

# Convert Python Object (Dict) to JSON
# ====================================
# If you want to convert a Python Object to JSON use the json.dumps() method.
d = {}
d["Name"] = "Luke"
d["Country"] = "Canada"

print(json.dumps(d, ensure_ascii=False))
# result {"Country": "Canada", "Name": "Luke"}
