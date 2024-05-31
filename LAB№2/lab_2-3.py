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
    print(f"Энтропия файла {file_path} по частотам = {entropy:.4f}")

def main():
    file_paths = ["same_a.txt", "random_01.txt", "random_255.txt"]
    for file_path in file_paths:
        find_frq(file_path)

if __name__ == "__main__":
    main()