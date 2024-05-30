def attack_caesar_c(cipher_text, dictionary):
    for key in range(0, 26):
        text = ""
        for char in cipher_text:
            if char.isalpha():
                if char.islower():
                    text += chr((ord(char) - key - 97) % 26 + 97)
                elif char.isupper():
                    text += chr((ord(char) - key - 65) % 26 + 65)
            else:
                text += char
        if any(word in text.lower() for word in dictionary):
            print("Ключ шифрования:", key)
            print("Дешифрованный текст:", text)

# Вводные данные
dictionary = ["consumption", "vegetables", "fruits", "apple", "python", "programm"]
cipher_text = "Wjlzqfw htsxzruynts tk ajljyfgqjx fsi kwznyx mjqux xywjslymjs ymj nrrzsj xdxyjr."

attack_caesar_c(cipher_text, dictionary)
