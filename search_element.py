# Функция для поиска элемента в кортеже
def search_element(tpl, element):
    if element in tpl:
        return tpl.index(element)  # Возвращаем индекс элемента, если он найден
    else:
        return -1  # Возвращаем -1, если элемент не найден
