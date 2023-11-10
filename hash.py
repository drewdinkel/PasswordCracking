import hashlib

#passList = open("/home/goofygoober/Desktop/PasswordCracking/passList.txt", "r")
#with open("/home/goofygoober/Desktop/PasswordCracking/passList.txt", "r") as passList:
#    for line in passList:
#        print(line)



my_str = 'password'
my_hash = hashlib.md5(my_str.encode('utf-8')).hexdigest()
print(my_hash)