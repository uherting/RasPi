# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

import json
from decimal import Decimal

# Convert JSON to Python Object (float)
# =====================================
# Floating points can be mapped using the decimal library.

jsondata = '{"number": 1.573937639}'

x = json.loads(jsondata, parse_float=Decimal)
print(x['number'])
