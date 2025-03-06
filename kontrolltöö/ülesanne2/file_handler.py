# file_handler.py
def read_grades_from_file(filename):
    students = []  # создание пустого списка студентов
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()  # удаляем пробелы по углам
            if content:
                entries = content.split('---')  # разделяем записи студентов по разделителю "---"
                for entry in entries:
                    lines = entry.strip().split('\n')
                    if len(lines) >= 2:
                        # Разделяем строку по двоеточию, чтобы получить имя студента
                        name = lines[0].split(':')[1].strip()  # получаем имя после ":"
                        
                        # Получаем строки оценок и преобразуем их в список чисел
                        grades_str = lines[1].split(':')[1].strip()  # находим строку с оценками
                        grades = [int(grade) for grade in grades_str.split(',')]  # преобразуем строки в числа
                        
                        students.append((name, grades))  # добавляем студента в список
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return students

def write_grades_to_file(filename, students):
    with open(filename, 'w', encoding='utf-8') as file:
        for name, grades in students:
            file.write(f"Nimi: {name}\nHinded: {', '.join([str(grade) for grade in grades])}\n---\n")
            # join соединяет оценки в одну строку, разделяя запятыми


