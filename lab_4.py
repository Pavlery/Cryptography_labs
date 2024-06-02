from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def read_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def pad_data(data):
    block_size = 16
    padding = block_size - len(data) % block_size
    return data + bytes([padding] * padding)

def unpad_data(data):
    padding = data[-1]
    return data[:-padding]

def encrypt_file(input_file, output_file, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    open_text = read_file(input_file)
    padded_text = pad_data(open_text)
    cipher_text = iv + cipher.encrypt(padded_text)
    write_file(output_file, cipher_text)

def decrypt_file(input_file, output_file, key):
    cipher_text = read_file(input_file)
    iv = cipher_text[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(cipher_text[16:])
    unpadded_text = unpad_data(decrypted_text)
    write_file(output_file, unpadded_text)

if __name__ == "__main__":
    key_input = input("Введите ключ (16 байт): ")
    key = key_input.encode()
    if len(key) != 16 and len(key) != 32:
        print(f"Неверная длина ключа шифрования ({len(key)} байт)")
    else:
        encrypt_file("open_text.txt", "encrypted_text.txt", key)
        decrypt_file("encrypted_text.txt", "decrypted_text.txt", key)
        print(f"Шифрование и дешифрование выполнено")