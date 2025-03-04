def read_notes(filename="notes.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            #читает всё содержимое файла в одну строку и удаляет пробелы или пустые строки в начале и конце
            content = file.read().strip()
            return content.split("---\n") if content else []
    except FileNotFoundError:
        return [] #если файл пустой, выдает пустой список

def write_notes(notes, filename="notes.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n---\n".join(notes) + "\n")