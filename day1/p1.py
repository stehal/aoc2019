import unittest
from collections import defaultdict

def doit():
	print("d")

class TestStringMethods(unittest.TestCase):
	
	def test(self):
		self.assertEqual( 1, 1)
		
	

#unittest.main()

infile = "in.txt"

#with open(infile) as f:
#	a = f.read()
	
for s in open(infile):
	print(s)
	doit()
	
	
	