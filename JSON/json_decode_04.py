# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json

# Convert JSON to Python Object (Example)
# =======================================
# JSON data often holds multiple objects, an example of how to use that below:
json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'

try:
    decoded = json.loads(json_input)

    # Access data
    for x in decoded['persons']:
        print(x['name'])

except (ValueError, KeyError, TypeError):
    print("JSON format error")
