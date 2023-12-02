import hashlib, bcrypt

#textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"
textPath = "C:/Users/Owner/OneDrive/Desktop/Cybersecurity/Python/PasswordCracking/PasswordCracking/passList.txt"

#if statement allows the functions only to be run when executed, not imported
#__name__ = __main__ when run directly, but gets set to the name of the module when imported
if __name__ == "__main__":
    #Function to crack md5 hashes
    def md5():
        #Variable later used to see if the password has been found (False by default)
        found = False
        password = input("Enter the md5 hash you want to be cracked. ")
        passList = open(textPath, "r")
        #Loop to go through passList (list of 10k most common passwords)
        with open(textPath, "r") as passList:
            for line in passList:
                #Have to cut last two characters to properly convert hash (Otherwise \n messes up the hash)
                guess = line.replace('\n', '')
                #Converts guess into md5 hash (utf-8 is most common encoding / hexdigest() turns into base16)
                hashGuess = hashlib.md5(guess.encode('utf-8')).hexdigest()
                print("Trying: " + hashGuess)
                #Checks if the guess is correct
                if (password == hashGuess):
                    #Sets found to true so the later if statement doesn't run
                    found = True
                    print("You've found the password! The md5 hash " + password + " is " + guess + " in plain text.")
                    #Exits function after password has been found
                    break
            #Only runs if the password wasn't found
            if(found == False):
                print("Hash could not be found")

if __name__ == "__main__":
    def bCrypt():
        password = input("Enter the password you want to be cracked. ")
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

if __name__ == "__main__":
    #Function to crack sha256 hashes
    def sha256():
        #Variable set to the value of whether the password has been found or not
        found = False
        password = input("Enter the sha256 hash you want to be cracked. ")
        passList = open(textPath, "r")
        #Loop to go through each line of the txt file with common passwords
        with open(textPath, "r") as passList:
            for line in passList:
                #Replaces \n so that the passwords don't include \n (Ensures they won't match)
                guess = line.replace('\n', '')
                #Converts the guess into a sha256 hash (base16 because of hexdigest) using utf-8
                hashGuess = hashlib.sha256(guess.encode('utf-8')).hexdigest()
                print("Trying: " + hashGuess)
                #Checks if the guess is correct
                if (password == hashGuess):
                    #Sets found to True so line later if statement doesn't run
                    found = True
                    print("You've found the password! The sha256 hash " + password + " is " + guess + " in plain text.")
                    #Exits the function after finding the correct hash/password
                    break
            #Only runs if the password wasn't found
            if (found == False):
                print("Hash could not be found.")