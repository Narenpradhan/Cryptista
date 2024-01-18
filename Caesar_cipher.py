import time


def banner():
    print(
"""\033[38;5;202m
******************************************************************
   ___                               ___ _       _               
  / __\__ _  ___  ___  __ _ _ __    / __(_)_ __ | |__   ___ _ __ 
 / /  / _` |/ _ \/ __|/ _` | '__|  / /  | | '_ \| '_ \ / _ \ '__|
/ /__| (_| |  __/\__ \ (_| | |    / /___| | |_) | | | |  __/ |   
\____/\__,_|\___||___/\__,_|_|    \____/|_| .__/|_| |_|\___|_|   
                                          |_|                    
******************************************************************""")


def encrypt_decrypt(user_input, key, mode):
    letters = "abcdefghijklmnopqrstuvwxyz123456789~`!@#$%^&*(<_-+={):;/?>.,}|'\'"
    numletters = len(letters)
    result = ""
    if mode == "d":
        key = -key

    for letter in user_input:
        letter = letter.lower()
        if letter != " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= numletters:
                    new_index -= numletters
                result += letters[new_index]
        else:
            pass
    return result


# Driver Code
banner()

mode = input("\n\033[38;5;230m[*] Do you want to Encrypt or Decrypt (e/d) : ")
key = int(input("\033[38;5;230m[*] Enter the key (1-63) : "))
separator = "-----------------------------------------"

if mode == "e":
    user_input = input("\033[38;5;230m[*] Enter text to Encrypt :")
    result = encrypt_decrypt(user_input, key, mode)
    print(f'\n\033[38;5;202m{separator}')
    print("\033[38;5;39m[*] Encrypting Plain Text.... ")
    time.sleep(1.5)
    print(f'\033[38;5;82m[+] Encrypted Text : {result}')
    print(f'\033[38;5;202m{separator}')
elif mode == "d":
    user_input = input("\033[38;5;230m[*] Enter text to Decrypt :")
    result = encrypt_decrypt(user_input, key, mode)
    print(f'\n\033[38;5;202m{separator}')
    print("\033[38;5;39m[*] Decrypting Cipher.... ")
    time.sleep(1.5)
    print(f'\033[38;5;82m[+] Decrypted Text : {result}')
    print(f'\033[38;5;202m{separator}')
