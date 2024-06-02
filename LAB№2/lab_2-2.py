import math
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

    entropy = 0
    for i in char_frq.values():
        chance = i / total_chars
        entropy += chance * math.log2(1 / chance)

    print(f"Энтропия файла по частотам = {entropy:.4f}")

file_path = "tеxt.txt"
find_frq(file_path)
