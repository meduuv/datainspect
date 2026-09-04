import unittest
from datainspect.core import json_stats
class Tests(unittest.TestCase):
 def test_object(self): self.assertEqual(json_stats('{"a":1}')['keys'],1)
if __name__=='__main__': unittest.main()
