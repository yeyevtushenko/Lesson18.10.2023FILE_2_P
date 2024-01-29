import os

def count_lines(input_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        line_count = len(lines)
        print(f"Кількість рядків у файлі {input_filename}: {line_count}")
    except FileNotFoundError:
        print(f"Помилка: файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


input_file_path = 'input.txt'

count_lines(input_file_path)
