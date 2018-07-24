#make a function that returns the time you wake up (as a string, ex. "7:20"), based on the day of the week and whether it is during vacation or not
#1 <- Monday 7 <- sunday

def whatTime(day):
    if day == 'Monday':
        print("7am")

    elif day == 'Tuesday':
        print("7.1am")

    elif day == 'Wednesday':
        print("7.2am")

    elif day == 'Thursday':
        print("7.3am")

    elif day == 'Friday':
        print("7.4am")

    elif day == 'Saturday':
        print("10am")

    elif day == 'Sunday':
        print("10am")

whatTime('Tuesday')

#Enter day of the week below to find out what time to wake up.



#make a function that returns the time you go to sleep




#add test cases here

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

