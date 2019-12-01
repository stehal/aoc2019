import unittest

def required_fuel(mass):
	return mass // 3 - 2
	
def total_required_fuel(mass):
	total = 0
	fuel = required_fuel(mass)
	while fuel > 0:
		total += fuel
		fuel = required_fuel(fuel)
	return total

class TestFirst(unittest.TestCase):
	
	def test1(self):
		self.assertEqual( 2, required_fuel(12))
		self.assertEqual( 2, required_fuel(14))
		self.assertEqual( 654, required_fuel(1969))
		self.assertEqual( 33583, required_fuel(100756))
		
	def test2(self):
		self.assertEqual( 2, total_required_fuel(14))
		self.assertEqual( 966, total_required_fuel(1969))
		self.assertEqual( 50346, total_required_fuel(100756))

if __name__ == '__main__':
    unittest.main()

infile = "in.txt"

sum = 0
for s in open(infile):
	sum += required_fuel(int(s))
print("part 1:",sum)

sum = 0
for s in open(infile):
	sum += total_required_fuel(int(s))
print("part 2:",sum)
	
	
	