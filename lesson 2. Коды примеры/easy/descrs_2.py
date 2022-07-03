"""
Пытаемся решить проблему традиционным способом - через геттеры и сеттеры
"""

#
# class Worker:
#     """Делаем атрибуты защищенными"""
#     def __init__(self, name, surname, hours, rate):
#         self.name = name
#         self.surname = surname
#         self._hours = hours
#         if hours <0:
#             raise  ValueError("Значение часов не может быть отрицательным")
#         self._rate = rate
#         if rate <0:
#             raise  ValueError("Значение ставки не может быть отрицательным")
#
#     def total_profit(self):
#             """Вычисляем зарплату"""
#             return self._hours * self._rate
#
# OBJ = Worker('Иван', 'Иванов', 10, 100)
# print(OBJ.total_profit())

#валидация не работает
#можем валидировать только передаваемые параметры
#но нет контроля изменения через объект
#геттер
# OBJ._hours = -10
# OBJ._rate = 100
# print(OBJ.total_profit())
#
#


#
#
class Worker:
    """Делаем атрибуты защищенными"""
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self._hours = hours
        if hours <0:
            raise  ValueError("Значение часов не может быть отрицательным")
        self._rate = rate
        if rate <0:
            raise  ValueError("Значение ставки не может быть отрицательным")



    # Для создания свойства-геттера над свойством ставится аннотация @property
    @property
    def hours(self):
        """Геттер"""
        return self._hours

    # сеттер
    # Для создания свойства-сеттера над свойством устанавливается
    # аннотация имя_свойства_геттера.setter
    @hours.setter
    def hours(self, value):
        """Сеттер"""
        if value < 0:
            raise ValueError("Значение часов не может быть отрицательным")
        self._hours = value

    @property
    def rate(self):
        """Геттер"""
        return self._rate

    @rate.setter
    def rate(self, value):
        """Сеттер"""
        if value < 0:
            raise ValueError("Значение ставки не может быть отрицательным")
        self._rate = value

    def total_profit(self):
        """Вычисляем зарплату"""
        return self._hours * self._rate


OBJ = Worker('Иван', 'Иванов', 10, 100)     #работа __init__
print(OBJ.total_profit())

# а здесь вроде решена
# но не будем же мы на каждый атрибут делать геттер и сеттер
# это избыточность кода, т.е. проблема в целом не решена
OBJ.hours = -10
OBJ.rate = 100
print(OBJ)
