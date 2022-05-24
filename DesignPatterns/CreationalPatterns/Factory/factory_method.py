from abc import ABC, abstractmethod
class iPizza(ABC):

    @abstractmethod
    def create_pizza(self): pass

class NYStyleVeggiePizza(iPizza):

    def __init__(self):
        self.pizza = "NY Style Veggie Pizza"

    def create_pizza(self):
        print("More salt")
        print("Less Cheese")
        print("Lot Veggies")
        return self


class NYStyleCheesePizza(iPizza):

    def __init__(self):
        self.pizza = "NY Style Cheese Pizza"

    def create_pizza(self):
        print("Less salt")
        print("More Cheese")
        print("Less Veggies")
        return self

class NYStylePapparoniPizza(iPizza):

    def __init__(self):
        self.pizza = "NY Style Papparoni Pizza"

    def create_pizza(self):
        print("More salt")
        print("Less Cheese")
        print("Less Veggies")
        return self

class ChicagoStyleVeggiePizza(iPizza):

    def __init__(self):
        self.pizza = "Chicago Style Veggie Pizza"

    def create_pizza(self):
        print("Less salt")
        print("More Cheese")
        print("Less Veggies")
        return self


class ChicagoStyleCheesePizza(iPizza):

    def __init__(self):
        self.pizza = "Chicago Style Cheese Pizza"

    def create_pizza(self):
        print("More salt")
        print("Less Cheese")
        print("More Veggies")
        return self

class ChicagoStylePapparoniPizza(iPizza):

    def __init__(self):
        self.pizza = "Chicago Style Papparoni Pizza"

    def create_pizza(self):
        print("Less salt")
        print("More Cheese")
        print("More Veggies")
        return self

class NYPizzaFactory:

    @staticmethod
    def create_pizza(pizza_type):

        if pizza_type == 'veggie':
            return NYStyleVeggiePizza()
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        if pizza_type == 'papparoni':
            return NYStylePapparoniPizza()
        return None


class ChicagoPizzaFactory:

    @staticmethod
    def create_pizza(pizza_type):

        if pizza_type == 'veggie':
            return ChicagoStyleVeggiePizza()
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        if pizza_type == 'papparoni':
            return ChicagoStylePapparoniPizza()
        return None

nypf = NYPizzaFactory.create_pizza('veggie')
print(nypf.pizza)
print(nypf.create_pizza())

cpf = ChicagoPizzaFactory.create_pizza('veggie')
print(cpf.pizza)
print(cpf.create_pizza())

