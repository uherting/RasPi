# found at: https://pythonspot.com/json-encoding-and-decoding-with-python/

Converting JSON data to Python objects
JSON data can be converted (deserialized) to Pyhon objects using the json.loads() function.

A table of the mapping:
JSON 	Python
--------------
object 	dict
array 	list
string 	str
number (int) 	int
number (real) 	float
true 	True
false 	False
null 	None