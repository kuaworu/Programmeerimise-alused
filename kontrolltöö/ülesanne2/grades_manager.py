# grades_manager.py
# Функция для добавления студента в список
def add_student(students, name, grades):
    students.append((name, grades))  # добавляем нового студента в список

# Функция для поиска студента по имени
def find_student_by_name(students, name):
    for student in students:
        # Сравниваем имя студента с введенным пользователем (игнорируем регистр)
        if student[0].lower() == name.lower():
            return student  # возвращаем информацию о студенте
    return None  # если студента нет, возвращаем None

# Функция для вычисления средней оценки студента
def calculate_average_grade(grades):
    if grades:  # если список оценок не пустой
        return sum(grades) / len(grades)  # возвращаем среднее значение
    return 0  # если список оценок пуст, возвращаем 0
