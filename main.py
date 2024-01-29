import os

def replace_chars(input_filename, output_filename):
    try:
        if os.path.isfile(input_filename):
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                lines = input_file.readlines()

            with open(output_filename, 'w', encoding='utf-8') as output_file:
                for line in lines:
                    modified_line = line.replace('*', '&').replace('&', '*')
                    output_file.write(modified_line)

            print(f"Успішно виконано та записано у файл {output_filename}.")
        else:
            print(f"Файл {input_filename} не існує.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")

input_file_path = 'input.txt'
output_file_path = 'output.txt'

replace_chars(input_file_path, output_file_path)
