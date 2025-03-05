from file_handler import read_notes, write_notes  

def add_note(title, text): #добавляет новую заметку в файл
    notes = read_notes()  
    notes.append("Pealkiri: " + title + "\nTekst: " + text)  # добавление заметки в конец списка
    write_notes(notes)  

 def view_notes(): #возвращает все заметки из файла
    return read_notes()  

def delete_note(title): #удаляет заметку с заданным заголовком
    notes = read_notes()  
    new_notes = []
    for note in notes:
        if not note.startswith("Pealkiri: " + title):
            new_notes.append(note)  # если элемент не начинается так, то добавляем его в новый список
    write_notes(new_notes)
