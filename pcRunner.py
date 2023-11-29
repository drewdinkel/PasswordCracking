# * Imports all functions
from bf import *
from hash import *
from dict import *


method = input("Which password cracking method would you like to use (bruteforce, hash, or dictionary)? ")
#Ensures case doesn't matter
m = method.lower()

if(m == "bruteforce"):
    #Runs function to get password length and available characters
    variables()
    #Runs function to brute force the password
    bruteForce()
elif(m == "hash"):
    type = input("Which type of hash would you like to crack (md5, bcrypt, or sha256)? ")
    #Ensures case doesn't matter
    t = type.lower()
    if(t == "md5"):
        #Runs function to crack md5 hash
        md5()
    elif(t == "bcrypt"):
        #Runs function to crack bcrypt hash
        bcrypt()
    elif(t == "sha256"):
        #Runs function to crack sha256 hash
        sha256()
    else:
        print("Hash type not found.")
elif(m == "dictionary"):
    #Runs function to crack password using dictionary attack
    dictAttack()
else:
    print("Password cracking method not found.")