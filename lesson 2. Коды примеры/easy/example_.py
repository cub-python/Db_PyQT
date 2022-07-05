class MyMeta(type):
    """Метакласс, проверяющий наличие строк в документации в подконтрольном классе"""
    def __init__(self,clsname,bases,clsdict):
        #к моменту начала работы метода __ini__ метакласса словарь
        #атрибутов контролируемого класса уже сформирован

        for key ,value in clsdict.items():
            #Пропустим специальные и частные методы
            if key.startswith("__"):
                continue

            #Пропустим любые невызываемые объекты
            if not hasattr(value,"__call__"):
                continue
            #Проверить наличие строки документирования
            #берем только вызываемые функции
            if not getattr(value,"__doc__"):
                raise TypeError(f'Метод {key} должен иметь строку документации из class {clsdict.get("__qualname__")}')

        type.__init__(self,clsname,bases,clsdict)


    def __call__(self, *args, **kwargs):
        obj = type.__call__(self,*args)
        for name in kwargs:
            setattr(obj,name,kwargs[name])
        return obj
