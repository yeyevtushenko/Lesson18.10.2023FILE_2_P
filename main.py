import os


def count_words_starting_with_char(input_filename, start_char):
    try:
        if os.path.isfile(input_filename):
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                words = input_file.read().split()

            count = sum(1 for word in words if word.startswith(start_char))

            print(f"Кількість слів, що починаються з символу '{start_char}': {count}")
        else:
            print(f"Файл {input_filename} не існує.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")

input_file_path = 'input.txt'
user_start_char = input("Введіть символ: ")

count_words_starting_with_char(input_file_path, user_start_char)
