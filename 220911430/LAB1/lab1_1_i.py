def char_to_int(c):
	return ord(c)-ord('a')

def int_to_char(n):
	return chr(n+ord('a'))
	
def encrypt_char(plain_char,key):
	if plain_char.isalpha():
		plaintext_int = char_to_int(plain_char.lower())
		encrypted_int = (plaintext_int+key) %26
		return int_to_char(encrypted_int)
	return plain_char

def decrypt_char(cipher_char,key):
	if cipher_char.isalpha():
		ciphertext_int = char_to_int(cipher_char.lower())
		decrypted_int = (ciphertext_int-key) %26
		return int_to_char(decrypted_int)
	return cipher_char
	
def msg_proc(message, key, mode):
	message=message.replace(" ","").lower()
	processed_chars = []
	
	if mode == 'encrypt':
		for char in message:
			processed_chars.append(encrypt_char(char, key))
	elif mode == 'decrypt':
		for char in message:
			processed_chars.append(decrypt_char(char, key))
		
	return ''.join(processed_chars)
	
message = "I am learning information security"
key = 20

encrypted_msg = msg_proc(message, key, 'encrypt')
print("Encrypted message:", encrypted_msg)

decrypted_msg = msg_proc(encrypted_msg, key, 'decrypt')
print("Decrypted message:", decrypted_msg)

