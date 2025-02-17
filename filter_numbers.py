def filter_by_ten(andmed):
    filtered_numbers = []  # Список для хранения чисел, делящихся на 10

    # Перебираем каждый элемент в кортеже
    for number in andmed:
        if number % 10 == 0:  # Проверяем, делится ли число на 10
            filtered_numbers.append(number)  # Если делится, добавляем в список

    # Преобразуем список обратно в кортеж и возвращаем
    return tuple(filtered_numbers)
