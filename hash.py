import hashlib

password = input("Enter the hash you want to be cracked. ")
textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"

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