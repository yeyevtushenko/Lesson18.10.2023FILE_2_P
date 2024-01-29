import os


def filter_words(input_filename, output_filename, min_length=7):
    try:
        if os.path.isfile(input_filename):
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                words = input_file.read().split()
        else:
            print(f"Файл {input_filename} не існує.")
            user_choice = input("Бажаєте створити файл? (y/n): ").lower()
            if user_choice != 'y':
                print("Фільтрація скасована.")
                return
            else:
                with open(input_filename, 'w', encoding='utf-8') as new_input_file:
                    new_input_file.write('')
                words = []

        filtered_words = [word for word in words if len(word) >= min_length]

        # Перевіряємо наявність вихідного файлу для запису результатів
        if os.path.isfile(output_filename):
            print(f"Файл {output_filename} вже існує.")
            user_choice = input("Бажаєте переписати його? (y/n): ").lower()
            if user_choice != 'y':
                print("Фільтрація скасована.")
                return

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(' '.join(filtered_words))

        print(f"Успішно відфільтровано та записано у файл {output_filename}.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


input_file_path = 'input.txt'
output_file_path = 'output.txt'

filter_words(input_file_path, output_file_path)