import os


def add_stars_after_last_non_comma_line(input_filename, output_filename):
    try:
        if os.path.isfile(input_filename):
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                lines = input_file.readlines()

            last_non_comma_index = -1
            for i, line in enumerate(reversed(lines)):
                if ',' not in line:
                    last_non_comma_index = len(lines) - 1 - i
                    break

            lines.insert(last_non_comma_index + 1 if last_non_comma_index != -1 else len(lines), '************\n')

            if os.path.isfile(output_filename):
                print(f"Файл {output_filename} вже існує.")
                user_choice = input("Бажаєте переписати його? (y/n): ").lower()
                if user_choice != 'y':
                    print("Додавання рядка скасовано.")
                    return

            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines)

            print(f"Рядок із зірочками успішно додано до файлу {output_filename}.")
        else:
            print(f"Файл {input_filename} не існує.")
            print("Додавання рядка скасовано.")

    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


input_file_path = 'input.txt'
output_file_path = 'output_stars.txt'

add_stars_after_last_non_comma_line(input_file_path, output_file_path)