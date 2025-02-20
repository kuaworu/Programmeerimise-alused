from pykkar import *

def paint_square():
    # Мы начинаем движение с текущей позиции робота
    while not is_wall():
        # Если перед роботом нет стены, красим текущую клетку
        paint()
        step()
    
    # Красим угол (если необходимо)
    if not is_wall():
        paint()
        step()  # Еще один шаг для покраски следующей клетки

    if not is_wall():
        paint()
        step()
        paint()

    for _ in range(8):  # Например, 8 поворотов вправо
        right()
        paint()
        
        # Поворачиваем вправо и делаем 4 шага, красим каждую клетку
    right()  # Поворачиваем вправо
    for _ in range(4):  # 4 шага вперед
        if not is_wall():  # Если перед роботом нет стены
            paint()  # Красим текущую клетку
            step()   # Делаем шаг вперед

        # Сделаем один шаг вперед и покрасим клетку
    if not is_wall():
        paint()  # Покрасить текущую клетку
        step()   # Сделать шаг вперед

    # Поворачиваем вправо
    right()

    # Сделаем 8 шагов вперед, красим каждую клетку
    for _ in range(8):  # 8 шагов вперед
        if not is_wall():  # Если перед роботом нет стены
            paint()  # Красим текущую клетку
            step()   # Делаем шаг вперед

    right()  # Поворачиваем вправо
    for _ in range(4):  # 4 шага вперед
        if not is_wall():  # Если перед роботом нет стены
            paint()  # Красим текущую клетку
            step()   # Делаем шаг вперед

        # Поворачиваем вправо
    right()

    # Делаем шаг, поворачиваем вправо и делаем 3 шага с покраской
    for _ in range(2):  # 2 раза (повернуть и сделать шаг с покраской)
        if not is_wall():  # Если перед роботом нет стены
            step()   # Делаем шаг
            paint()  # Красим клетку
        
        right()  # Поворачиваем вправо

        if not is_wall():
            step()
            paint()
        
        paint()
        step()
        paint()

        right()
        right()
        right()
        
        right()
        right()
        right()
        step()
        right()
        step()
        paint()
        
    right()
    for _ in range(1):
        if not is_wall():  # Если перед роботом нет стены
            step()   # Делаем шаг
            paint()  # Красим клетку
            
        paint()
        right()
        step()
        step()
        paint()
        step()
        paint()
        right()
        paint()
        step()
        right()
        step()
        paint()
        right()
        right()
        right()
        paint()
        step()
        right()
        step()
        step()
        paint()
        right()
        paint()
        step()
        right()
        right()
        right()
        step()
        step()
        paint()
        step()
        right()
        right()
        right()
        paint()
        right()
        paint()
        #есл шот не такк тут удалять
        right()
        step()
        paint()
        step()
        paint()
        right()
        right()
        right()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        right()
        right()
        right()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        #stena verhnaja potom
        right()
        right()
        right()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        #третья строчка с клетками
        right()
        right()
        right()
        step()
        right()
        right()
        right()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        #4
        right()
        paint()
        step()
        paint()
        right()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        right()
        #1
        step()
        step()
        paint()
        step()
        paint()
        right()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        right()
        step()
        step()
        right()
        right()
        right()
        step()
        paint()
        step()
        paint()
        #3 комната
        #есл шот не такк тут удалять
        # Функция для шагов с покраской
        right()
        paint()
        step()
        paint()
        step()
        paint()
        right()
        right()
        right()
        step()
        paint()
        step()
        paint()
        step()
        paint()
        #ы
        right()
        right()
        right()


    # Шаги с покраской, повторяющиеся 4 раза
    for _ in range(4):
        paint()
        step()

    right()
    paint()
    step()

    right()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()

    #3
    step()
    paint()
    right()
    step()
    step()
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    paint()
    step()
    paint()
    right()
    right()
    right()
    paint()
    step()
    paint()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    paint()
    step()
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    #4 квадрат
# Функция для шагов с покраской
    step()
    paint()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    right()
    right()
    step()
    paint()
    right()
    right()
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    right()
    step()
    paint()
    right()
    step()
    paint()
    step()
    paint()
    step()
    right()
    step()
    step()
    step()
    right()
    paint()
    step()
    paint()
    step()
    paint()
    for _ in range(2):  # Повторить 2 раза
        step()
        paint()

