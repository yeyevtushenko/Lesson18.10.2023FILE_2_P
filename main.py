import os

def write_to_file(array, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for element in array:
                output_file.write(str(element) + '\n')

        print(f"Успішно записано у файл {output_filename}.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


string_array = ["Hello", "world", "Python", "is", "awesome"]
output_file_path = 'output.txt'

write_to_file(string_array, output_file_path)
