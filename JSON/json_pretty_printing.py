# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json

# Pretty printing
# ===============
# If you want to display JSON data you can use the json.dumps() function.
json_data = '{"name": "Brian", "city": "Seattle"}'
json_obj = json.loads(json_data)
print(json.dumps(json_obj, sort_keys=True, indent=4))
