class MixinRepr:
    """
    Класс Mixin для дополнения классов методом __repr__
    """

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.__dict__.items()}'
