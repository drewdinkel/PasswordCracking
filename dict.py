textPath = "/home/goofygoober/Desktop/PasswordCracking/passList.txt"
#Variable to determine if the password was found
tF = False

def dictAttack():
    password = input("Enter the password you want to be cracked. ")
    passList = open(textPath, "r")
    with open(textPath, "r") as passList:
        for line in passList:
            #Cuts out \n so passwords match
            guess = line.replace("\n", "")
            print("Trying: " + guess)
            if (guess == password):
                #Sets tF to true so line 21 doesn't run
                tF = True
                print("You've found the password! The password is " + guess)
                #Leave function when the password was found
                break
        #If password wasn't found print so
        if (tF == False):
            print("The password could not be located.")

#Runs the function for testing
dictAttack()