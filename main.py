import os


def reverse_copy_file(source_filename, destination_filename):
    try:
        if os.path.isfile(source_filename):
            with open(source_filename, 'r', encoding='utf-8') as source_file:
                lines = source_file.readlines()

            if os.path.isfile(destination_filename):
                print(f"Файл {destination_filename} вже існує.")
                user_choice = input("Бажаєте переписати його? (y/n): ").lower()
                if user_choice != 'y':
                    print("Копіювання скасовано.")
                    return
            else:
                print(f"Файл {destination_filename} не існує.")
                user_choice = input("Бажаєте створити файл та ввести його вміст? (y/n): ").lower()
                if user_choice != 'y':
                    print("Копіювання скасовано.")
                    return
                else:
                    lines.reverse()
                    content = ''.join(lines)

                    with open(destination_filename, 'w', encoding='utf-8') as destination_file:
                        destination_file.write(content)

                    print(f"Успішно скопійовано у файл {destination_filename}.")
                    return

            lines.reverse()
            with open(destination_filename, 'w', encoding='utf-8') as destination_file:
                destination_file.write(''.join(lines))

            print(f"Успішно скопійовано у файл {destination_filename}.")
        else:
            print(f"Файл {source_filename} не існує.")
            print("Копіювання скасовано.")

    except Exception as e:
        print(f"Виникла помилка: {str(e)}.")


source_file_path = 'source.txt'
destination_file_path = 'destination_reverse.txt'

reverse_copy_file(source_file_path, destination_file_path)
