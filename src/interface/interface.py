# %%
from abc import ABCMeta, abstractmethod

# %%


class IClass(metaclass=ABCMeta):
    @abstractmethod
    def hello(self):
        pass


class ClassImpl1(IClass):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = ClassImpl1()

# %%


class ClassImpl2(IClass):
    def __init__(self):
        pass

    def hello(self):
        print("hello")


if __name__ == '__main__':
    a = ClassImpl2()
