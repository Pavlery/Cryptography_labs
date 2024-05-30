def attack_caesar_o(open_text, cipher_text):
    for key in range(0, 25):
        decrypted_text = decrypt(cipher_text, key)
        if decrypted_text == open_text:
            return key
    return None

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Вводные данные
cipher_text = "Wjlzqfw htsxzruynts tk ajljyfgqjx fsi kwznyx mjqux xywjslymjs ymj nrrzsj xdxyjr."
open_text = "Regular consumption of vegetables and fruits helps strengthen the immune system."

# Вывод результата
find_key = attack_caesar_o(open_text, cipher_text)
print("Ключ шифрования:", find_key)
