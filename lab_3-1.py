import random

def generate_random_file(file_path, num_chars):
    with open(file_path, 'w') as file:
        for _ in range(num_chars):
            random_char = chr(random.randint(48, 90))
            file.write(random_char)

if __name__ == "__main__":
    generate_random_file("key.txt", 100)
