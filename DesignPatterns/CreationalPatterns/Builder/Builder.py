

class Laptop:

    def __init__(self):
        self.brand_name = None
        self.storage_type = None
        self.ram_size = None

    def specification(self):
        return f'The laptop is having brand name as {self.brand_name + " " if self.brand_name else "NA "}' \
               f'with storage type {self.storage_type + " " if self.storage_type else "NA "}' \
               f'with ram_size {self.ram_size + " " if self.ram_size else "NA "}'

class LaptopBuilder:

    def __init__(self, laptop=Laptop()):
        self.laptop = laptop

    def setbrandname(self, name):
        self.laptop.brand_name = name
        return self

    def setstoragetype(self, type):
        self.laptop.storage_type = type
        return self

    def setramsize(self, size):
        self.laptop.ram_size = size
        return self

    def build(self):
        return self.laptop

# lb = LaptopBuilder()
# laptop = lb.build()
# print(laptop.specification())
#
# lb.setbrandname('Apple').setramsize('8GB')
# print(laptop.specification())

class ScreenSize:
    def __init__(self, screen_size):
        self.screen_size = screen_size

class Processor:
    def __init__(self, processor):
        self.processor = processor

class StorageType:
    def __init__(self, storage_type):
        self.storage_stype = storage_type

class Laptop:

    def __init__(self):
        self.screen_size = None
        self.processor = None
        self.storage_type = None

    def specification(self):
        return f'Screen size is {self.screen_size + " " if self.screen_size else "NA "}'\
                f'Processor is {self.processor + " " if self.processor else "NA "}'\
                f'Storage type is {self.storage_type + " " if self.storage_type else "NA "}'

from abc import ABC, abstractmethod

class iLaptopBuilder(ABC):

    @abstractmethod
    def set_screen_size(self): pass

    @abstractmethod
    def set_processor(self): pass

    @abstractmethod
    def set_storage_type(self): pass

    @abstractmethod
    def build(self): pass


class HPLaptopBuilder(iLaptopBuilder):

    def __init__(self):
        self.laptop = Laptop()

    def set_screen_size(self, screen_size):
        self.laptop.screen_size = screen_size
        return self

    def set_processor(self, processor):
        self.laptop.processor = processor
        return self

    def set_storage_type(self, storage_type):
        self.laptop.storage_type = storage_type
        return self

    def build(self):
        return self.laptop

class DellLaptopBuilder(iLaptopBuilder):

    def __init__(self):
        self.laptop = Laptop()

    def set_screen_size(self, screen_size):
        self.laptop.screen_size = screen_size
        return self

    def set_processor(self, processor):
        self.laptop.processor = processor
        return self

    def set_storage_type(self, storage_type):
        self.laptop.storage_type = storage_type
        return self

    def build(self):
        return self.laptop

class Director:

    def __init__(self, laptop_builder):
        self.laptop_builder = laptop_builder

    def set_specifications(self, screen_size, processor, storage_type):
        return self.laptop_builder.set_screen_size(screen_size).set_processor(processor).set_storage_type(storage_type).build()


hp_laptop_builder = HPLaptopBuilder()
hp_laptop_builder2 = HPLaptopBuilder()
hp_director = Director(hp_laptop_builder)
hp_director2 = Director(hp_laptop_builder2)
hp_laptop = hp_director.set_specifications("15'", "Intel i7", "SDD")
hp_laptop2 = hp_director2.set_specifications("16'", "Intel i3", "HDD")
print(hp_laptop.specification())
print(hp_laptop2.specification())

dell_laptop_builder = DellLaptopBuilder()
dell_director = Director(dell_laptop_builder)
dell_laptop = dell_director.set_specifications("14'", "Intel i5", "SDD")
print(dell_laptop.specification())
