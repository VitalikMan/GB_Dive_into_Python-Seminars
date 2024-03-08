# Задача:
# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

# * на уровне пакета
# from new_package import *

# * на уровне модуля внутри пакета
from new_package.data_parser import *

# from new_package import Task_5
# from new_package import data_parser
from random import *

data_parser()
