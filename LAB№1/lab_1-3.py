def attack_caesar_c(cipher_text):
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
        print("Ключ %d: %s" % (key, text))

cipher_text = "Wjlzqfw htsxzruynts tk ajljyfgqjx fsi kwznyx mjqux xywjslymjs ymj nrrzsj xdxyjr."
attack_caesar_c(cipher_text)
