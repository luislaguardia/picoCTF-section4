#replace the code in level4.py with the code i provided to get the flag

Changes Made:
1. Removed the Old Loop: The old loop that iterated from 1 to 100 was removed.
2. Used 'pos_ps_list': Added the list of possible passwords directly within 'level_4_pw_check' function.
3. Password Checking: The loop now iterates over each password in 'pos_pw_list', checking if its hash matches the
   correct password hash.
4. Error Handling: If no password is correct, it will print "That password is incorrect."

   note: ensure that level4.flag.txt.enc and level4.hash.bin files are correctly placed in your working directory.


Author: LT 'syreal' Jones

Description:
Can you crack the password to get the flag? 
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. 
There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.  

HINTS:
1 - A for loop can help you do many things very quickly.

2 - The str_xor function does not need to be reverse engineered for this challenge.
