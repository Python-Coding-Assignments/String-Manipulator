import string

def getStatistics(userString):
    """This function prints the number letters, punctuation characters, digits, and whitespaces that are found in the user's string.  The function takes in one argument in the function's call, which is the user's string."""

    #declaration and initialization of variables
    allPunctuation = string.punctuation
    numWhiteSpace = numPunctuation = numDigits = numLetters = 0

    #for loop which iterates over each integer between the zero, inclusive, and the length of the user's string, exclusive
    for i in range(0, len(userString)):
        #conditional statement which checks if character at index i in user's string is a punctuation character
        if userString[i] in allPunctuation:
            numPunctuation += 1
        #conditional statement which checks if character at index i in user's string is a whitespace character    
        elif userString[i] == " ":
            numWhiteSpace += 1
        #conditional statement which checks if character at index i in user's string is a digit    
        elif userString[i].isdigit() == True:
            numDigits += 1  
        #conditional statement which checks if a character at index i in user's string is a letter of any case    
        else:
            numLetters += 1                

    #printing information about the user's string to the user
    print("Letters: " + str(numLetters))
    print("Punctuation: " + str(numPunctuation))
    print("Digits: " + str(numDigits))
    print("WhiteSpace: " + str(numWhiteSpace) + "\n")