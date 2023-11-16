import hashlib

textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"

#if statement allows the functions only to be run when executed, not imported
#__name__ = __main__ when run directly, but gets set to the name of the module when imported
if __name__ == "__main__":
    def md5():
        password = input("Enter the md5 hash you want to be cracked. ")
        passList = open(textPath, "r")
        with open(textPath, "r") as passList:
            for line in passList:
                #Have to cut last two characters to properly convert hash (Otherwise \n messes up the hash)
                guess = line.replace('\n', '')
                #Converts guess into md5 hash (utf-8 is most common encoding / hexdigest() turns into base16)
                hashGuess = hashlib.md5(guess.encode('utf-8')).hexdigest()
                print("Trying: " + hashGuess)
                if (password == hashGuess):
                    print("You've found the password! The md5 hash " + password + " is " + guess + " in plain text.")
                    break
            #If hash wasn't found
            print("Hash could not be found")

if __name__ == "__main__":
    def bcrypt():
        print("BCrypt")

if __name__ == "__main__":
    def sha256():
        print("SHA256")