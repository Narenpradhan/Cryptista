
def encrypt_decrypt(user_input, key):
    binary_message = ''.join(format(ord(char), '08b') for char in user_input)
    binary_key = ''.join(format(ord(char), '08b') for char in key)

    key = (binary_key * (len(binary_message) // len(binary_key) + 1))[:len(binary_message)]
    
    encrypted_binary = ''.join(str(int(m) ^ int(k)) for m, k in zip(binary_message, key))
    encrypted_message = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))
    return encrypted_message


def banner():
    print('''\033[38;5;202m
*******************************************************************************************
                                                   ,,            ,,                        
`YMM'   `MP' .g8""8q. `7MM"""Mq.        .g8"""bgd  db          `7MM                        
  VMb.  ,P .dP'    `YM. MM   `MM.     .dP'     `M                MM                        
   `MM.M'  dM'      `MM MM   ,M9      dM'       ``7MM `7MMpdMAo. MMpMMMb.  .gP"Ya `7Mb,od8 
     MMb   MM        MM MMmmdM9       MM           MM   MM   `Wb MM    MM ,M'   Yb  MM' "' 
   ,M'`Mb. MM.      ,MP MM  YM.       MM.          MM   MM    M8 MM    MM 8M""""""  MM     
  ,P   `MM.`Mb.    ,dP' MM   `Mb.     `Mb.     ,'  MM   MM   ,AP MM    MM YM.    ,  MM     
.MM:.  .:MMa.`"bmmd"' .JMML. .JMM.      `"bmmmd' .JMML. MMbmmd'.JMML  JMML.`Mbmmd'.JMML.   
                                                        MM                                 
                                                      .JMML.                     
*******************************************************************************************''')



banner()

key = input("\033[38;5;230m[*] Enter the key : ")
separator = "-----------------------------------------"
user_input = input("\033[38;5;230m[*] Enter text to Encrypt :")
result = encrypt_decrypt(user_input, key)
print(f'\n\033[38;5;202m{separator}')
print("\033[38;5;39m[*] Encrypting Plain Text.... ")
time.sleep(1.5)
print(f'\033[38;5;82m[+] Encrypted Text : *{result}*')
print(f'\033[38;5;202m{separator}')
result = encrypt_decrypt(result, key)
print(f'\n\033[38;5;202m{separator}')
print("\033[38;5;39m[*] Decrypting Cipher.... ")
time.sleep(1.5)
print(f'\033[38;5;82m[+] Decrypted Text : {result}')
print(f'\033[38;5;202m{separator}')