import os

def count_characters(input_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        char_count = len(content)
        print(f"Кількість символів у файлі {input_filename}: {char_count}")
    except FileNotFoundError:
        print(f"Помилка: файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


input_file_path = 'input.txt'

count_characters(input_file_path)
