"""Пример метакласса, переопределяющего поведение методов __new__ и __init__ своих классов"""
# from easy.example_ import MyMeta
from example_ import MyMeta


class MyMetaClass(type):
    # Должен словарь для атрибутов класса
    @classmethod
    #name MyClass
    #bases parents Myclass type (list)
    def __prepare__(metacls, clsname, bases):
        print('Перегружаю prepare')
        return type.__prepare__(metacls,clsname,bases)
    # Вызывается для создания экземпляра класса, перед вызовом __init__
    #dct - словарь атрибутов класса
    def __new__(cls, name, bases, dct):
        print(f'Выделение памяти для класса {name}, '
              f'имеющего кортеж базовых классов {bases}, '
              f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)

    # Выделение памяти  для класса MyClass, имеющего кортеж базовых классов( <
    # class '__main__.Parent_1'>, < class '__main__.Parent_2' > ),
    # и словарь атрибутов {'__module__': '__main__', '__qualname__': \
    # 'MyClass', 'my_attr': 10}

    def __init__(cls, name, bases, dct):
        print(f'Инициализация класса {name}')
        super(MyMetaClass, cls).__init__(name, bases, dct)
    #Должен создать и вернуть экземпляр нового класса
    def __call__(self, *args, **kwargs):
        print('Перегружаю call')
        return type.__call__(self, *args, **kwargs)


# родитель 1
class Parent_1():
    pass

# родитель 2
class Parent_2():
    pass

# пользовательский класс
class MyClass(Parent_1, Parent_2, metaclass=MyMetaClass):
    my_attr = 10

MC = MyClass()


class Test(metaclass=MyMeta):

   def get_print1(self):
       """Test"""
       print('test')

   def get_print(self):
       """Test2"""
       print('test')


"""
Результат:

Выделение памяти для класса MyClass, 
имеющего кортеж базовых классов (<class '__main__.Parent_1'>, <class '__main__.Parent_2'>), 
и словарь атрибутов {'__module__': '__main__', '__qualname__': 'MyClass', 'my_attr': 10}

Инициализация класса MyClass
"""