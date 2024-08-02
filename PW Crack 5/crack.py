import hashlib

def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

with open('level5.hash.bin', 'rb') as file:
    correct_pw_hash = file.read()

with open('dictionary.txt', 'r') as file:
    dictionary_words = file.readlines()

correct_password = None
for word in dictionary_words:
    word = word.strip()
    if hash_pw(word) == correct_pw_hash:
        correct_password = word
        break

if correct_password:
    print(f"Correct password: {correct_password}")

    with open('level5.flag.txt.enc', 'rb') as file:
        flag_enc = file.read()

    decrypted_flag = str_xor(flag_enc.decode(), correct_password)
    print(f"Decrypted flag: {decrypted_flag}")
else:
    print("Correct password not found in dictionary.")
