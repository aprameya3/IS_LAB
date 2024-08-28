def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=key.index))  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix = []
    used_chars = set()
    
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def proc_text(ptext):
    ptext = ptext.replace(' ', '').upper()
    ptext = ptext.replace('J', 'I')
    pairs = []
    i = 0
    while i < len(ptext):
        char1 = ptext[i]
        if i + 1 < len(ptext):
            char2 = ptext[i + 1]
            if char1 != char2:
                pairs.append((char1, char2))
                i += 2
            else:
                pairs.append((char1, 'X'))
                i += 1
        else:
            pairs.append((char1, 'X'))
            i += 1
    return pairs

def find_pos(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return (r, row.index(char))
    return None

def playfair_cipher(pair, matrix):
    r1, c1 = find_pos(matrix, pair[0])
    r2, c2 = find_pos(matrix, pair[1])
    if r1 == r2: 
        return (matrix[r1][(c1 + 1) % 5], matrix[r2][(c2 + 1) % 5])
    elif c1 == c2: 
        return (matrix[(r1 + 1) % 5][c1], matrix[(r2 + 1) % 5][c2])
    else:  
        return (matrix[r1][c2], matrix[r2][c1])

def encryption(message, key):
    matrix = create_playfair_matrix(key)
    pairs = proc_text(message)
    en_msg = []
    for pair in pairs:
        enc_pair = playfair_cipher(pair, matrix)
        en_msg.extend(enc_pair)
    return ''.join(en_msg)

key = "GUIDANCE"
message = "The key is hidden under the door pad"
encrypted = encryption(message, key)
print("Encrypted Message:", encrypted)

