import os

# Функция для получения следующего ID
def get_next_id():
    if os.path.exists("last_id.txt"):  # Проверяем, существует ли файл с последним ID
        with open("last_id.txt", "r") as file:
            last_id = int(file.read())  # Читаем последний ID
        new_id = last_id + 1  # Увеличиваем ID на 1
    else:
        new_id = 1  # Если файла нет, начинаем с 1
    with open("last_id.txt", "w") as file:
        file.write(str(new_id))  # Сохраняем новый ID в файл
    return new_id  # Возвращаем новый ID

# Функция для создания записи
def create(name, time):
    user_id = get_next_id()  # Получаем новый ID
    # Здесь ты можешь записать данные в файл или выполнить другие действия
    with open("user_data.txt", "a", encoding="utf-8") as file:
        file.write(f"ID: {user_id}, Nimi: {name}, Aeg: {time}\n")  # Сохраняем данные
    print(f"ID: {user_id}, Nimi: {name}, Aeg: {time} on salvestatud edukalt")
