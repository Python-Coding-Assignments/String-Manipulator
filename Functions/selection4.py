def changeChars(userString):
    """This function changes the specified instances of a character within the user's string and changes it to a new character defined by the user.  The function takes in one argument, which is the original string.  Then the function returns the user's new string."""

    #declaration and initialization of variables
    replacer = replaced = returnString = ""
    value = False
    numReplaced = 0
    string = []

    #for loop which iterates through all integers between the value zero, inclusive, and the length of the user's string, exclusive
    for i in range(0, len(userString)):
        #appending all characters of the string to the local list
        string.append(userString[i])                   
    
    #while loop which runs until value is equal to True
    while value == False:
        #prompting the user to enter in a character that he or she would like to be replaced
        replaced = input("Replace all of these characters: ")

        #for loop which iterates over each integer between zero, inclusive, and the length of the user's string, exclusive
        for i in range(0, len(userString)):
            #conditional statement which checks if the replaced character matches any of the characters within the user's string and if the length of the user's input is equal to one
            if replaced == userString[i] and len(replaced) == 1:
                value = True
        #conditional statement which prints a message if the value of value is False        
        if value == False:
            print("Your current string does not contain the character " + replaced)   
    
    #while loop which runs until value is equal to False
    while value == True:
        #prompting the user to enter in a character that he or she would like to replaced the previous character with
        replacer = input("To these characters: ")
        #conditional statement which checks if the input's length is equal to one
        if len(replacer) == 1:
            value = False
    
    #for loop which iterates over each integer between zero, inclusive, and the length of the user's string, exclusive
    for i in range(0, len(userString)):
        #conditional statement which checks if the character within the user's string at index i is equal to the replaced character
        if userString[i] == replaced:
            #changing the instance of the character at index i to equal replacer
            string[i] = replacer
            numReplaced += 1

    #for loop which iterates over each integer between zero, inclusive, and the length of the user's string
    for i in range(0, len(string)):
        #appending characters to returnString variable
        returnString += string[i]      

    #conditional statement which checks if numReplaced is equal to one
    if numReplaced == 1:
        print(str(numReplaced) + " character replaced.\n")
    #conditional statement which checks if numReplaced is any other integer besides one    
    else:
        print(str(numReplaced) + " characters replaced.\n")

    #returning the local variable called returnString
    return returnString