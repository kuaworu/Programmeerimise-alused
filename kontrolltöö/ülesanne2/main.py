# main.py
#split – разделяет строку на части.
#strip – удаляет пробелы по краям.
#join – объединяет элементы в строку.
#lower - все буквы маленькими становятся.
from file_handler import read_grades_from_file, write_grades_to_file
from grades_manager import add_student, find_student_by_name, calculate_average_grade

FILENAME = "grades.txt"  # Имя файла с оценками студентов

def display_students(students):
    if not students:  # если список студентов пуст
        print("Pole õpilaste andmeid.")  # выводим сообщение, что данных нет
    else:
        for student in students:
            name, grades = student  # извлекаем имя студента и его оценки
            avg_grade = calculate_average_grade(grades)  # вычисляем среднюю оценку
            print(f"Nimi: {name}, Hinded: {', '.join([str(grade) for grade in grades])}, Keskmine hinne: {avg_grade:.2f}")

            # выводим имя, оценки и среднюю оценку

def main():
    students = read_grades_from_file(FILENAME)  # загружаем данные из файла

    while True:
        print("\nMenüü:")
        print("1. Lisa õpilane ja tema hinded")
        print("2. Vaata kõiki õpilasi ja nende hindeid")
        print("3. Otsi õpilast nime järgi")
        print("4. Välju")
        choice = input("Vali tegevus (1-4): ")

        if choice == '1':
            name = input("Sisesta õpilase nimi: ")
            grades_input = input("Sisesta hinded (eralda komaga): ")
            grades = [int(grade) for grade in grades_input.split(',')]
  # преобразуем строку оценок в числа
            add_student(students, name, grades)  # добавляем нового студента
            write_grades_to_file(FILENAME, students)  # сохраняем изменения в файл
            print("Õpilane on lisatud.")
        elif choice == '2':
            display_students(students)  # выводим список студентов
        elif choice == '3':
            name = input("Sisesta õpilase nimi otsinguks: ")
            student = find_student_by_name(students, name)  # ищем студента
            if student:
                name, grades = student
                avg_grade = calculate_average_grade(grades)
                print(f"Nimi: {name}, Hinded: {', '.join([str(grade) for grade in grades])}, Keskmine hinne: {avg_grade:.2f}")

            else:
                print("Õpilast ei leitud.")
        elif choice == '4':
            print("Programmist väljumine.")
            break  # выходим из программы
        else:
            print("Vale valik, proovige uuesti.")  # если введен неверный выбор

# Запуск программы
main()

