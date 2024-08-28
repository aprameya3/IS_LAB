def prep_text(ptext):
    ptext = ptext.upper().replace(' ', '') 
    ptext = ptext.replace('J', 'I') 
    return ptext

def text_num(ptext):
    return [ord(char) - ord('A') for char in ptext] 

def num_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers) 

def matrix_mult(keymat, block):
    block_size = len(keymat)
    encrypted_block = [0] * block_size
    for i in range(block_size):
        encrypted_block[i] = sum(keymat[i][j] * block[j] for j in range(block_size)) % 26
    return encrypted_block

def hill_ci_encrypt(ptext, keymat):
    ptext = prep_text(ptext)
    block_size = len(keymat) 
    
    #checking matrix mult cond and adding PADDING
    if len(ptext) % block_size != 0:
        ptext += 'X' * (block_size - len(ptext) % block_size)
    
    text_number = text_num(ptext)
    ci_nums = []
    
    #conv matrix to numpy for matrix operations block by block and then appending to ans in numericals
    
    for i in range(0, len(text_number), block_size):
        block = text_number[i:i + block_size]
        enc_block = matrix_mult(keymat, block)  
        ci_nums.extend(enc_block)
    
    return num_text(ci_nums)

keymat = [
    [3, 3],
    [2, 7]
]

message = "We live in an insecure world"

enc_msg = hill_ci_encrypt(message, keymat)
print("Encrypted Message:", enc_msg)

