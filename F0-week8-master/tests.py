import unittest
from main import to_upper
class MyTestCase(unittest.TestCase): 
def test_to_upper(self):
name = "Harini" 
upper_name = to_upper(name)
self.assertEqual(upper_name, "Karuna")

if __name	== '	main	': unittest.main() 

