import bf
import dict
import hash

method = input("Which password cracking method would you like to use (bruteforce, hashes, dictionary)? ")
m = method.lower()

if(m == "bruteforce"):
    print("bf")
elif(m == "hashes"):
    print("hashes")
elif(m == "dictionary"):
    print("dict")
else:
    print("Password cracking method not found.")