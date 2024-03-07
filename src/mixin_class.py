class MixinRepr:
    """
    Класс Mixin для дополнения классов методом __repr__
    """

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        repr_file = [str(i[0]) + ': ' + str(i[1]) for i in self.__dict__.items()]
        return f' Обьект класса {self.__class__.__name__} ({", ".join(repr_file)})'
