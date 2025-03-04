# Проверка на наличие цифры
def has_digit(password):
    # Проверяет, есть ли хотя бы одна цифра в пароле
    return any(char.isdigit() for char in password)

# Проверка на наличие заглавной буквы
def has_uppercase(password):
    # Проверяет, есть ли хотя бы одна заглавная буква в пароле. цикл, чтоб всё проверило
    return any(char.isupper() for char in password)

# Проверка на длину пароля
def is_long_enough(password):
    # Проверяет, что длина пароля не меньше 8 символов
    return len(password) >= 8

# Основная функция для проверки паролей
def valid_passwords(paroolid):
    # Список для хранения паролей, которые соответствуют всем условиям
    valid_passwords_list = []
    
    # Проходим по каждому паролю в списке
    for password in paroolid:
        # Проверка всех условий: длина пароля, наличие цифры и заглавной буквы
        if is_long_enough(password) and has_digit(password) and has_uppercase(password):
            # Если пароль удовлетворяет всем условиям, добавляем его в список валидных
            valid_passwords_list.append(password)
    
    # Возвращаем список паролей, которые соответствуют всем условиям
    return valid_passwords_list

# Запрос 4 паролей у пользователя
paroolid = []  # Создаём пустой список для хранения паролей
for i in range(4):  # Цикл для ввода 4 паролей
    user_input = input(f"Введите пароль {i+1}: ")  # Запрашиваем пароль у пользователя
    paroolid.append(user_input)  # Добавляем введённый пароль в список

# Вызов функции и вывод результата
valid_parools = valid_passwords(paroolid)  # Проверяем пароли на соответствие условиям
# Печать валидных паролей
print(f"Действительные пароли: {valid_parools}")