from pykkar import *
from painter import paint_square

# Создание мира
create_world("""
###########################
#>     #      #     #     #
#      #      #     #     #
#                         #
#      #      #     #     #
#      #      #     #     #
###########################
""")

# Функция для покраски всех клеток
paint_square()
repeat_steps()

input("Нажмите Enter, чтобы завершить...")
