import unittest

def parse(data):
    return list(map(int, data.split(","))) 
    
def operate(ints, pos):
    val1, val2 = ints[pos +1], ints[pos +2]    
    result_pos = ints[pos + 3]
   
    op = ints[pos]
    if op == 1:
         ints[result_pos] = ints[val1] + ints[val2]
    if op == 2:
        ints[result_pos] = ints[val1] * ints[val2]
     
    return ints
    
def doit(data):
    pos = 0
    while pos < len(data):
        if data[pos] == 99:
           return data
        data = operate(data,pos)
        pos += 4        
    
class TestFirst(unittest.TestCase):
    data = "1,9,10,3,2,3,11,0,99,30,40,50"

    def test_parse(self):
        self.assertEqual( 1, parse(self.data)[0])
        self.assertEqual( 50, parse(self.data)[11])

    def test_op(self):
        ints = parse(self.data)
        ints = operate(ints,0)
        self.assertEqual( 70, ints[3])
        ints = operate(ints,4)
        self.assertEqual( [3500,9,10,70,2,3,11,0,99,30,40,50], ints)

    def test_doit(self):
        self.assertEqual([30,1,1,4,2,5,6,0,99], doit([1,1,1,4,99,5,6,0,99]))

if __name__ == '__main__':
    unittest.main()

infile = "in.txt"
data = open(infile).read()
ints = parse(data)
ints[1], ints[2] = 12, 2
print("part 1",doit(ints)[0])
    
ints = parse(data)
for i in range(100):
    for j in range(100):
        new_ints = list(ints)
        new_ints[1], new_ints[2] = i,j
        if doit(new_ints)[0] == 19690720:
            print("part 2", 100*i+j)
            break