textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"
#Variable to determine if the password was found
found = False

#if statement allows the functions only to be run when executed, not imported
#__name__ = __main__ when run directly, but gets set to the name of the module when imported
if __name__ == "__main__":
    #Function to find the password using the passList
    def dictAttack():
        password = input("Enter the password you want to be cracked. ")
        passList = open(textPath, "r")
        #Loop to check each line in passList
        with open(textPath, "r") as passList:
            for line in passList:
                #Cuts out \n so passwords match
                guess = line.replace("\n", "")
                print("Trying: " + guess)
                #Checks if the guess is correct
                if (guess == password):
                    #Sets found to true so line 26 is false and doesn't run inside print statement
                    found = True
                    print("You've found the password! The password is " + guess)
                    #Leave function when the password was found
                    break
            #If password wasn't found print so
            if (found == False):
                print("The password could not be located.")