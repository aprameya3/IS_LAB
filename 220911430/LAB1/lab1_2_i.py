def char_to_int(c):
    return ord(c) - ord('a')

def int_to_char(n):
    return chr(n + ord('a'))
    
def vig_encrypt(plaintext, key):
	key = key.lower()
	plaintext = plaintext.lower().replace(" ","")
	encrypted_text = []
	
	key_ln = len(key)
	key_int = [char_to_int(i) for i in key]
	plaintext_int = [char_to_int(i) for i in plaintext]
	
	for i in range(len(plaintext_int)):
		value = (plaintext_int[i] + key_int[i % key_ln]) % 26
		encrypted_text.append(int_to_char(value))
		
	return ''.join(encrypted_text)

def vig_decrypt(ciphertext, key):
	key = key.lower()
	ciphertext = ciphertext.lower().replace(" ","")
	decrypted_text = []
	
	key_ln = len(key)
	key_int = [char_to_int(i) for i in key]
	ciphertext_int = [char_to_int(i) for i in ciphertext]
	
	for i in range(len(ciphertext_int)):
		value = (ciphertext_int[i] - key_int[i % key_ln]) % 26
		decrypted_text.append(int_to_char(value))
		
	return ''.join(decrypted_text)
	
message="the house is being sold tonight"
key = "dollars"

encrypted_msg = vig_encrypt(message, key)
print("Encrypted message: ", encrypted_msg)

decrypted_msg = vig_decrypt(encrypted_msg, key)
print("Decrypted message: ", decrypted_msg)
