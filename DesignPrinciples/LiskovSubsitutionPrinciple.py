# Liskov Substitution Principle

# Example 1
class VehicleCheck:

    def check_wheels(self):
        # Write some code to check wheels
        wheel_status = 'Works Fine'
        return wheel_status

    def check_body(self):
        # Write some code to check body
        body_status = 'Works Fine'
        return body_status

    def check_engine(self):
        # Write some code to check engine
        engine_status = 'Works Fine'
        return engine_status

    def check_battery(self):
        # Write some code to check battery
        battery_status = 'Works Fine'
        return battery_status

class VehicleCheckWithoutEngine(VehicleCheck):

    def check_wheels(self):
        # Write some code to check wheels
        wheel_status = 'Works Fine'
        return wheel_status

    def check_body(self):
        # Write some code to check body
        body_status = 'Works Fine'
        return body_status

class CarCheck(VehicleCheck):

    def check_wheels(self):
        # Write some code to check wheels
        wheel_status = 'Works Fine'
        return wheel_status

    def check_body(self):
        # Write some code to check body
        body_status = 'Works Fine'
        return body_status

    def check_engine(self):
        # Write some code to check engine
        engine_status = 'Works Fine'
        return engine_status

    def check_battery(self):
        # Write some code to check battery
        battery_status = 'Works Fine'
        return battery_status

class BikeCheck(VehicleCheck):

    def check_wheels(self):
        # Write some code to check wheels
        wheel_status = 'Works Fine'
        return wheel_status

    def check_body(self):
        # Write some code to check body
        body_status = 'Works Fine'
        return body_status

    def check_engine(self):
        # Write some code to check engine
        engine_status = 'Works Fine'
        return engine_status

    def check_battery(self):
        # Write some code to check battery
        battery_status = 'Works Fine'
        return battery_status

class CycleCheck(VehicleCheckWithoutEngine):
    def check_wheels(self):
        # Write some code to check wheels
        wheel_status = 'Works Fine'
        return wheel_status

    def check_body(self):
        # Write some code to check body
        body_status = 'Works Fine'
        return body_status


# Example 2
class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self._width} Height: {self._height}'

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(ob):
    w = ob.width
    ob.height = 10
    expected = int(w * 10)
    print(f'expected result is {expected} and we got {ob.area}')

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

