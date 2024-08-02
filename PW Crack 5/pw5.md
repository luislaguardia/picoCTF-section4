# Solution for PW Crack 4 in picoCTF

replace the code in level4.py with the code i provided to get the flag

The script `level5.py` reads the dictionary words from `dictionary.txt`, hashes each word after 
removing any whitespace, and compares the hashed word with the correct password hash `level5.hash.bin`. 
If a match is found, the script uses the password to decrypt the flag from `level5.flag.txt.enc`.



Author: LT 'syreal' Jones

Description
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

HINTS:
1 - Opening a file in Python is crucial to using the provided dictionary.
2 - You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip
3 - The str_xor function does not need to be reverse engineered for this challenge.
