def prep_text(ptext):
    ptext = ptext.upper().replace(' ', '')
    ptext = ptext.replace('J', 'I')  # Standard practice for shift ciphers
    return ptext

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def find_shift(plaintext, ciphertext):
    pt_numbers = text_to_numbers(plaintext)
    ct_numbers = text_to_numbers(ciphertext)
    shift = (ct_numbers[0] - pt_numbers[0]) % 26
    return shift

def shift_cipher_decrypt(ciphertext, shift):
    ct_numbers = text_to_numbers(ciphertext)
    pt_numbers = [(num - shift) % 26 for num in ct_numbers]
    return numbers_to_text(pt_numbers)

given_ciphertext = "CIW"
given_plaintext = "yes"
tablet_ciphertext = "XVIEWYWI"

prep_plaintext = prep_text(given_plaintext)
prep_ciphertext = prep_text(given_ciphertext)

shift = find_shift(prep_plaintext, prep_ciphertext)
print(f"Shift Key: {shift}")

decrypted_message = shift_cipher_decrypt(tablet_ciphertext, shift)
print(f"Decrypted Message: {decrypted_message}")

