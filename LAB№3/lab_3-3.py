from Crypto.Cipher import ARC4
def read_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data
def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def get_user_key():
    key = input("Введите ключ: ")
    return key.encode()

def rc4_cipher(data, key):
    cipher = ARC4.new(key)
    cipher_text = cipher.encrypt(data)
    return cipher_text
def rc4_decipher(cipher_text, key):
    cipher = ARC4.new(key)
    open_text = cipher.decrypt(cipher_text)
    return open_text

if __name__ == "__main__":
    key = get_user_key()
    open_text = read_file("open_text.txt")

    cipher_text = rc4_cipher(open_text, key)
    write_file("encrypted_text_rc4.txt", cipher_text)

    decrypted_text = rc4_decipher(cipher_text, key)
    write_file("decrypted_text_rc4.txt", decrypted_text)
