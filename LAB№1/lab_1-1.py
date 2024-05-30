def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

# Вводные данные
text = "Regular consumption of vegetables and fruits helps strengthen the immune system."
key = 5

# Вывод результата
encrypted_text = caesar_encrypt(text, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, key)
print("Дешифрованный текст:", decrypted_text)
