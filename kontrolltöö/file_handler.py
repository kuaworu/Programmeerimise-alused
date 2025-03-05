 def read_notes(filename="notes.txt"): #чтения содержимого файла и возвращения его в виде списка заметок
    try:
        with open(filename, "r", encoding="utf-8") as file:
            #удаляет пробелы и символы новой строки
            content = file.read().strip() 
            if content:
                return content.split("---\n")
            else:
                return []  # если файл пустой, возвращаем пустой список
    except FileNotFoundError: #Обрабатывает ошибку отсутствия файла
        return []  # если файл не найден, возвращаем пустой список

def write_notes(notes, filename="notes.txt"): #Записывает список заметок в файл.
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n---\n".join(notes) + "\n")
