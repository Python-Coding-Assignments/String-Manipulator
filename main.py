from Functions import menu, changeChars, getStatistics, getRandomStr

#declaration and initialization of variables
userString = userSelection = ""
value = False

#prompting user to enter any string and then printing out the menu options
print("To get started, enter anything you would like, then hit enter: ")
userString = input()
menu()

#while loop which runs while value is value does not equal True
while value == False:
    #getting menu selection from user
    userSelection = input("Selection -----> ")

    #conditional statement which checks if the user entered menu selection one
    if userSelection == "1":
        #prints current string to the user
        print("Current String: " + userString + "\n")

    #conditional statement which checks if the user entered menu selection two    
    elif userSelection == "2":
        #changes applicable characters within the user's string to be upper case
        userString = userString.upper()    

    #conditional statement which checks if the user entered menu selection three    
    elif userSelection == "3":
        #changes applicable characters within the user's string to be lower case
        userString = userString.lower()

    #conditional statement which checks if the user entered menu selection four    
    elif userSelection == "4":
        #calls changeChars function and sets the new string to be the user's new string
        userString = changeChars(userString) 

    #conditional statement which checks if the user entered menu selection five       
    elif userSelection == "5":
        #calls getStatistics function and displays the string's statistics
        getStatistics(userString)

    #conditional statement which checks if the user entered menu selection six    
    elif userSelection == "6":
        #prompts the user to enter a new string
        print("Enter a new string:")    
        userString = input()
        print()

    #conditional statement which checks if the user entered menu selection seven    
    elif userSelection == "7":
        #calls getRandomStr to get new string from user
        userString = getRandomStr()
        print("Your string is now: " + userString + "\n")

    #conditional statement which checks if the user entered menu selection eight    
    elif userSelection == "8":
        #calls menu function to print menu to the screen
        menu()

    #conditional statement which checks if the user entered menu selection nine    
    elif userSelection == "0":
        print("Bye!")
        value = True

    #conditional statement which checks if the user entered an invalid menu selection    
    else:
        print("Invalid Choice.\n")         