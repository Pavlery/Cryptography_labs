def find_frq(file_path):
    char_frq = {}
    total_chars = 0

    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in char_frq:
                        char_frq[char] += 1
                    else:
                        char_frq[char] = 1
                    total_chars += 1

    for char, i in char_frq.items():
        frq = i / total_chars
        print(f"Частота появления '{char}' = {frq}")

file_path = r"M:\Progs\Python\Doc\tеxt1.txt"
find_frq(file_path)
