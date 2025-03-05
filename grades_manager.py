# grades_manager.py

def add_student_grade(name, grades, filename="grades.txt"):
    """Добавляет нового студента и его оценки в файл"""
    grades_entry = f"Nimi: {name}\nHinded: {', '.join(map(str, grades))}"
    all_grades = read_grades(filename)  # Чтение всех существующих данных
    all_grades.append(grades_entry)  # Добавление новой записи
    write_grades(all_grades, filename)  # Запись обновленных данных в файл

def calculate_average_grade(name, filename="grades.txt"):
    """Вычисляет среднюю оценку студента по имени"""
    all_grades = read_grades(filename)
    for entry in all_grades:
        if entry.startswith(f"Nimi: {name}"):
            grades_str = entry.split("Hinded: ")[1]
            grades = list(map(int, grades_str.split(", ")))  # Преобразуем строку в список чисел
            return sum(grades) / len(grades)  # Возвращаем среднее значение
    return None  # Если студент не найден

def find_student(name, filename="grades.txt"):
    """Ищет студента по имени и возвращает его данные"""
    all_grades = read_grades(filename)
    for entry in all_grades:
        if entry.startswith(f"Nimi: {name}"):
            return entry  # Возвращаем всю запись студента
    return None  # Если студент не найден

def view_all_grades(filename="grades.txt"):
    """Просматривает все оценки студентов"""
    return read_grades(filename)
