import sys, itertools, hashlib, bcrypt



#File location of the passList used for dictionary attacks
textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"


#Sets password to users input (Must be entered hashed if using a hashed method)
password = sys.argv[1]

#Variables to determine which function is run
type = ""
mode = ""
#sys.argv[2:] includes all arguments after 1
argList = sys.argv[2:]

#Checks all arguments after the password (1st argument)
for arg in argList:
    if (arg == "-b"):
        mode = "bruteforce"
    elif (arg == "-d"):
        mode = "dictionary"
    elif (arg == "-p"):
        type = "plaintext"
    elif (arg == "-m"):
        type = "md5"
    elif (arg == "-s"):
        type = "sha256"
    elif (arg == "-bc"):
        type = "bcrypt"

#Sets plaintext as default type if not stated otherwise
if (type == ""):
    type = "plaintext"
#Sets dictionary as default mode if not stated otherwise
if (mode == ""):
    mode = "dictionary"
#Doesn't allow hashes to be bruteforced. Instead sets type to plaintext
if (mode == "bruteforce" and (type == "md5" or type == "sha256" or type == "bcrypt")):
    print("Bruteforce and hashes are not a valid combination. Setting type to plaintext.\n")
    type = "plaintext"



#Import all password cracking functions
#Function to crack a plain text password using bruteforce
def bruteForce():
    l = input("How many characters is the password? ")
    length = int(l)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?."
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
def bCrypt():
    #Encodes password to prevent error in checkpw function
    p = password.encode('utf-8')
    passList = open(textPath, "r")
    with open(textPath, "r") as passList:
        for line in passList:
            guess = line.replace("\n", "")
            #Encodes guess to prevent error in checkpw function
            g = guess.encode('utf-8')
            print("Trying: " + guess)
            #checkpw function checks if the guess is equal to the bcrypt hash
            if (bcrypt.checkpw(g, p)):
                found = True
                print("You've found the password! The bcrypt hash " + password + " is " + guess + " in plain text.")
                break
        if (found == False):
            print("The password could not be located.")

#Runs bruteforce
if (mode == "bruteforce"):
    bruteForce()
#All dictionary attacks
elif (mode == "dictionary"):
    #Runs plain text dictionary attack
    if (type == "plaintext"):
        dictAttack()
    #Runs md5 hash dictionary attack
    elif (type == "md5"):
        md5()
    #Runs sha256 hash dictionary attack
    elif (type == "sha256"):
        sha256()
    #Runs bcrypt hash dictionary attack
    elif (type == "bcrypt"):
        bCrypt()