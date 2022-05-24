from abc import ABC, abstractmethod

class iFruit(ABC):

    @abstractmethod
    def create_fruit(self): pass

class ConcreteFruitA(iFruit):

    def __init__(self):
        self.fruits = ['Apple', 'Avacado', 'Apricot']

    def create_fruit(self):
        return self

class ConcreteFruitB(iFruit):

    def __init__(self):
        self.fruits = ['Banana', 'Blue Berries', 'BilBerries']

    def create_fruit(self):
        return self

class ConcreteFruitC(iFruit):

    def __init__(self):
        self.fruits = ['Chayote', 'ChokeBerries', 'Cherry Fruit']

    def create_fruit(self):
        return self

class ConcreteFruitD(iFruit):

    def __init__(self):
        self.fruits = ['Date']

    def create_fruit(self):
        return self

class FruitFactory:

    @staticmethod
    def create_fruit(alphabet):
        if alphabet == 'a':
            return ConcreteFruitA()
        if alphabet == 'b':
            return ConcreteFruitB()
        if alphabet == 'c':
            return ConcreteFruitC()
        if alphabet == 'd':
            return ConcreteFruitD()

        return None

# Client Side Code

f = FruitFactory.create_fruit('d')
print(f.fruits)

