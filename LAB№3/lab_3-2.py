def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def vernam_cipher(open_text, key):
    encrypted_text = ''.join(chr(ord(a) ^ ord(b))
        for a, b in zip(open_text, key))
    return encrypted_text

def vernam_decipher(encrypted_text, key):
    decrypted_text = ''.join(chr(ord(a) ^ ord(b))
        for a, b in zip(encrypted_text, key))
    return decrypted_text

if __name__ == "__main__":
    open_text = read_file("open_text.txt")
    key = read_file("key.txt")

    encrypted_text = vernam_cipher(open_text, key)
    write_file("encrypted_text_vernam.txt", encrypted_text)

    decrypted_text = vernam_decipher(encrypted_text, key)
    write_file("decrypted_text_vernam.txt", decrypted_text)
