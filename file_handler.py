# file_handler.py

def read_grades(filename="grades.txt"):
    """Читает оценки всех студентов из файла"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()  # Чтение содержимого файла и удаление лишних пробелов
            return content.split("---\n") if content else []
    except FileNotFoundError:
        return []  # Если файл не найден, возвращаем пустой список

def write_grades(grades, filename="grades.txt"):
    """Записывает оценки студентов в файл"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n---\n".join(grades) + "\n")  # Каждая запись разделена "---\n"
