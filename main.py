#import letters_counter as counter
#import filter_numbers as filter_func
import search_element as search_func

# # Запрашиваем слово у пользователя
# word = input("Введите слово: ")

# # Вызываем функцию для подсчёта букв
# result = counter.count_letters(word)

# # Печатаем результат
# for letter, count in result.items():
#     print(f"букв {letter} {count}")

#tuples
# tuple = (2,4,5)
# print(tuple)
# tuple = "õun", "pirn", "ploom"
# print(tuple2)

# andmed = (10, 15, 20, 25, 30, 35)
# result = filter_func.filter_by_ten(andmed)
# print(result)

# Кортеж с названиями
names_tuple = ("тушканчик", "мандарин", "капибара", "человек паук", "бетмен")

# Вводим элемент для поиска
element = input("Введите название для поиска: ")

# Вызываем функцию для поиска элемента
result = search_func.search_element(names_tuple, element)

# Выводим результат
if result != -1:
    print(f"Элемент '{element}' найден на позиции {result}.")
else:
    print(f"Элемент '{element}' -1.")
