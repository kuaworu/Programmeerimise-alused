from notes_manager import add_note, view_notes, delete_note 

def main():
    while True:
        print("\n1. Lisa märge\n2. Vaata märkmeid\n3. Kustuta märge\n4. Välju")  # добавить, посмотреть, удалить, выйти
        choice = input("Valik: ")  # запрашиваем ввод пользователя

        if choice == "1":
            title = input("Sisesta pealkiri: ")  # ввод заголовка
            text = input("Sisesta tekst: ")  # ввод текста
            add_note(title, text)  # добавление заметки
            print("Märge lisatud!")  # сообщение об успехе
        elif choice == "2":
            for note in view_notes():  # перебираются заметки
                print(note + "\n")  # выводится заметка с новой строки
        elif choice == "3":
            title = input("Sisesta kustutatava märkme pealkiri: ")  # ввод заголовка заметки для удаления
            delete_note(title)  # удаление заметки
            print("Märge kustutatud!")  # сообщение об удалении
        elif choice == "4":
            break  # выход из цикла
        else:
            print("Vale valik!")  # сообщение об ошибке ввода

main()
