import sys, itertools, hashlib


#Sets password to users input (Must be entered hashed if using a hashed method)
password = sys.argv[1]
#File location of the passList used for dictionary attacks
#textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"
textPath = "C:/Users/Owner/OneDrive/Desktop/Cybersecurity/Python/PasswordCracking/PasswordCracking/passList.txt"



#Import all password cracking functions
#Function to crack a plain text password using bruteforce
def bruteForce():
    l = input("How many characters is the password? ")
    length = int(l)
    chars = input("What characters are used in the password? ")
    #itertools.product factors (Ex. product("AB", "AB") => AA AB BA BB)
    for x in itertools.product(chars, repeat = length):
        #Sets guess equal to the next possible combination
        #.join combines each iterator value into one complete string
        guess = "".join(x)
        print("Trying: " + guess)
        #Checks if the guess is correct
        if (guess == password):
            print("You've found the password! The password is " + guess)
            #Exits the for function once the password has been found
            break

#Function to crack a plain text password using a dictionary attack
def dictAttack():
    #Variable to determine if the password was/wasn't found
    found = False
    passList = open(textPath, "r")
    #Loop to check each line in passList
    with open(textPath, "r") as passList:
        for line in passList:
            #Cuts out \n so passwords match
            guess = line.replace("\n", "")
            print("Trying: " + guess)
            #Checks if the guess is correct
            if (guess == password):
                #Sets found to true so line later if statement is false and doesn't run inside print statement
                found = True
                print("You've found the password! The password is " + guess)
                #Leave function when the password was found
                break
        #If password wasn't found print so
        if (found == False):
            print("The password could not be located in the dictionary.")

#Function to crack a md5 hash using a dictionary attack
def md5():
    found = False
    passList = open(textPath, "r")
    with open(textPath, "r") as passList:
        for line in passList:
            guess = line.replace('\n', '')
            #Converts guess into md5 hash (utf-8 is most common encoding / hexdigest() turns into base16)
            hashGuess = hashlib.md5(guess.encode('utf-8')).hexdigest()
            print("Trying: " + hashGuess)
            if (password == hashGuess):
                found = True
                print("You've found the password! The md5 hash " + password + " is " + guess + " in plain text.")
                break
        if(found == False):
            print("The password could not be found in the dictionary.")

#Function to crack a sha256 hash using a dictionary attack
def sha256():
    found = False
    passList = open(textPath, "r")
    with open(textPath, "r") as passList:
        for line in passList:
            guess = line.replace('\n', '')
            #Converts the guess into a sha256 hash
            hashGuess = hashlib.sha256(guess.encode('utf-8')).hexdigest()
            print("Trying: " + hashGuess)
            if (password == hashGuess):
                found = True
                print("You've found the password! The sha256 hash " + password + " is " + guess + " in plain text.")
                break
        if (found == False):
            print("The password could not be found in the dictionary.")

#Function to crack a bcrypt hash
def bcrypt():
    print("bcrypt still a work in progress.")

#Runs bruteforce
if (sys.argv[2] == "-b"):
    bruteForce()
#All dictionary attacks
elif (sys.argv[2] == "-d"):
    #Runs plain text dictionary attack
    if (sys.argv[3] == "-p"):
        dictAttack()
    #Runs md5 hash dictionary attack
    elif (sys.argv[3] == "-m"):
        md5()
    #Runs sha256 hash dictionary attack
    elif (sys.argv[3] == "-s"):
        sha256()
    #Runs bcrypt hash dictionary attack
    elif (sys.argv[3] == "-bc"):
        bcrypt()
    else:
        print("Not a valid argument. Check the readme.md for more information on proper arguments.")
else:
    print("Not a valid argument. Check the readme.md for more information on proper arguments.")