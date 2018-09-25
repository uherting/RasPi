#!/usr/bin/python

import sys
import os

# add classes directory of current project to the search path in order
# to find custom classes used in this script
print('apple')
# print(os.path.realpath(__file__))
# print(dirname(os.path.realpath('/sdf/ttt.txt')))
# print('#' + sys.path.append(os.path.dirname('sdf/ttt.txt') + '/classes#'))
print(os.path.realpath(os.path.dirname(__file__) + '/classes'))
print('pear')
print(sys.path)
