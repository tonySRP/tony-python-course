#This is a function that returns a number cubed
def testCube(base):
    return base*base*base

#This function triples a string
def testTripleString(word):
    return word+word+word

#add some test cases for both of them

def printTwice(input):
    print(input)
    print(input)

base = 10
word = 'corn'

printTwice(testCube(base))
printTwice(testTripleString(word))

