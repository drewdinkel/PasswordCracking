# 2023 CSHS Cybersecurity Password Cracking Project

A conceptual program built to crack passwords through bruteforce combinations, bruteforce dictionary, md5 dictionary, sha256 dictionary, and bcrypt dictionary.



# Dependencies
- passList.txt file

For the dictionary attacks to work the textPath variable must be changed to wherever the passList.txt file has been saved on the user's computer.



# Command Line Arguments
Format: python3 [filename] [password] [argument one] [argument two]
- If using a hash the entered password must already be hashed

First Argument:
- -b = bruteforce (Only cracks plaintext)
- -d = dictionary

Second Argument (only used with dictionary):
- -p = plaintext
- -m = md5 hash
- -s = sha256 hash
- -bc = bcrypt hash (Password must be entered in '' to work)

Examples:
- python3 main.py dad3 -b
- python3 main.py cliff -d -p
- python3 main.py 5f4dcc3b5aa765d61d8327deb882cf99 -d -m
- python3 main.py '$2y$10$wnHNwi6JjtGjV5CeB3JPV.5PW97fn2iQ9mX1nQ95yUmphTYFvpBnG' -d -bc



# Limitations
- If the password is not on the dictionary list the password will not be found.
- Bruteforce combination goes through most common characters but not all. If there is a strange character like "}" the password will not be found.
