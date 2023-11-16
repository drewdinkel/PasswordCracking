# * Imports all functions
from bf import *
from hash import *


method = input("Which password cracking method would you like to use (bruteforce, hash, or dictionary)? ")
m = method.lower()

if(m == "bruteforce"):
    #Calls all the functions in the bf.py file
    variables()
    bruteForce()
elif(m == "hash"):
    type = input("Which type of hash would you like to crack (md5, bcrypt, or sha256)? ")
    t = type.lower()
    if(t == "md5"):
        md5()
    elif(t == "bcrypt"):
        bcrypt()
    elif(t == "sha256"):
        sha256()
    else:
        print("Hash type not found.")
elif(m == "dictionary"):
    print("dict")
else:
    print("Password cracking method not found.")