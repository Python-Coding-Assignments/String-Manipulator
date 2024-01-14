import random
import string

def getRandomStr():
    """This function generates a random string whose length can range from one character long to fifty characters long.  The function then returns the randomly generated string."""

    #declaration and initialization of variables
    allChars = string.ascii_letters + string.digits + string.punctuation
    lengthOfReturn = randomCharIndex = 0
    newString = ""

    #generates the random length of the string, from one to fifty, inclusive
    lengthOfReturn = random.randint(1, 50)

    #for loop which iterates over every integer from zero, inclusive, to the length of the string, exclusive
    for i in range(0, lengthOfReturn):
        #generates a random character from the string containing all characters on the keyboard
        randomCharIndex = random.randint(0, (len(allChars) - 1))
        #adding randomly generated character to new string that will be returned by the function
        newString += allChars[randomCharIndex]

    #returning randomly generated string
    return newString    