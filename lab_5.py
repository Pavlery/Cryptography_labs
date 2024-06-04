from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad_data(data):
    block_size = 16
    padding = block_size - len(data) % block_size
    return data + bytes([padding] * padding)

def unpad_data(data):
    padding = data[-1]
    return data[:-padding]

def hash_password(password, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    hashed_password = cipher.encrypt(pad_data(password))
    return iv + hashed_password

def bytes_to_hex_string(data):
    return data.hex()

def check_password(password, hashed_password, key):
    iv = hashed_password[:16]
    cipher_text = hashed_password[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_password = unpad_data(cipher.decrypt(cipher_text))
    return password == decrypted_password

if __name__ == "__main__":
    key = get_random_bytes(16)
    users = {}
    while True:
        print("1. Регистрация нового пользователя")
        print("2. Вход")
        choice = input("Выберите действие (1 или 2): ")
        if choice == '1':
            username = input("Введите логин: ")
            password = input("Введите пароль: ").encode()
            hashed_password = hash_password(password, key)
            users[username] = hashed_password
            print("Пользователь зарегистрирован.")
            hashed_password_hex = bytes_to_hex_string(hashed_password)
            print(f"Хеш-сумма пароля: {hashed_password_hex}")
        elif choice == '2':
            username = input("Введите логин: ")
            if username in users:
                password = input("Введите пароль: ").encode()
                if check_password(password, users[username], key):
                    print("Вход выполнен успешно.")
                else:
                    print("Неверный пароль.")
            else:
                print("Пользователь не найден.")