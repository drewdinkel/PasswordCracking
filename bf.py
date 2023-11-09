import itertools

#Function to assign all variables (Global gives bruteForce() access to variables)
def assign():
    #Get password to try and guess
    global password; password = input("Enter your desired password. ")
    global length; length = len(password)
    #Gather all possible characters in the password
    global chars; chars = input("What characters does the password consist of? ")
    global guess; guess = ""

#Function to crack the password
def bruteForce():
    #itertools.product factors (Ex. product("AB", "AB") => AA AB BA BB)
    for x in itertools.product(chars, repeat = length):
        #Sets guess equal to the next possible combination
        #.join combines each iterator value into one complete string
        guess = "".join(x)
        print("Trying: " + guess)
        if (guess == password):
            print("You've found the password! The password is " + guess)
            #Exits the for loop once the password has been found
            break

#Calls functions
assign()
bruteForce()