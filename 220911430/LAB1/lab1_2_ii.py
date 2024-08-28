def char_to_int(c):
    return ord(c) - ord('a')

def int_to_char(n):
    return chr(n + ord('a'))

def autokey_encrypt(plaintext, key):
    key_char = int_to_char(key) 
    key = key_char.lower()
    plaintext = plaintext.lower().replace(" ", "")
    encrypted_text = []
    
    extended_key = key + plaintext  
    
    key_length = len(extended_key)
    key_as_int = [char_to_int(i) for i in extended_key]
    plaintext_int = [char_to_int(i) for i in plaintext]
    
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i]) % 26
        encrypted_text.append(int_to_char(value))
    
    return ''.join(encrypted_text)

def autokey_decrypt(ciphertext, key):
    key_char = int_to_char(key) 
    key = key_char.lower()
    ciphertext = ciphertext.lower()
    decrypted_text = []
    
    extended_key = key 
    key_as_int = [char_to_int(i) for i in extended_key]
    ciphertext_int = [char_to_int(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if i > 0:  
            extended_key += decrypted_text[i-1]
            key_as_int.append(char_to_int(decrypted_text[i-1]))
        
        value = (ciphertext_int[i] - key_as_int[i]) % 26
        decrypted_char = int_to_char(value)
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)

message = "the house is being sold tonight"
key = 7 

encrypted_msg = autokey_encrypt(message, key)
print("Encrypted message:", encrypted_msg)

decrypted_msg = autokey_decrypt(encrypted_msg, key)
print("Decrypted message:", decrypted_msg)

