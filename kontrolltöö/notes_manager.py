from file_handler import read_notes, write_notes  # Импорт функций работы с файлом

def add_note(title, text):
    notes = read_notes()  
    notes.append("Pealkiri: " + title + "\nTekst: " + text)  #добавление заметки в конец списка
    write_notes(notes)  

def view_notes():
    return read_notes()  

def delete_note(title):
    notes = read_notes()  
    new_notes = [note for note in notes if not note.startswith("Pealkiri: " + title)]  #если элемент не начинается так, то добавляем
    write_notes(new_notes)
