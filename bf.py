import itertools

#Get password to try and guess
password = input("Enter your desired password. ")
length = len(password)
#Gather all possible characters in the password
chars = input("What characters does the password consist of? ")
#Converting all viable characters to an element in a list
#cList = list(chars)
#Guessed pw that will be filled out later
guess = ""

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