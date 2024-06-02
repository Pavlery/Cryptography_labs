import random
def generate_file_same_char(file_path, char, num_chars):
    with open(file_path, 'w') as file:
        file.write(char * num_chars)

def generate_file_random_binary(file_path, num_chars):
    with open(file_path, 'w') as file:
        for _ in range(num_chars):
            random_bit = str(random.randint(0, 1))
            file.write(random_bit)

def generate_file_random_bytes(file_path, num_chars):
    with open(file_path, 'w', encoding='utf-8') as file:
        for _ in range(num_chars):
            random_byte = random.randint(0, 255)
            random_char = chr(random_byte)
            file.write(random_char)

# Генерация файлов
generate_file_same_char ("same_a.txt", 'a', 100)
generate_file_random_binary("random_01.txt", 100)
generate_file_random_bytes("random_255.txt", 100)

print("Текстовые файлы успешно сгенерированы.")
