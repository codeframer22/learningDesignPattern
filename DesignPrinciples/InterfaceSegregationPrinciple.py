# Interface Segregation Principle

class Machine:

    def printing(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def photocopy(self, document):
        raise NotImplementedError



class AdvancedMachine(Machine):

    def printing(self, document):
        # Meaningful implementation
        pass

    def scan(self, document):
        # Meaningful implementation
        pass

    def fax(self, document):
        # Meaningful implementation
        pass

    def photocopy(self, document):
        # Meaningful implementation
        pass

class OldMachine(Machine):

    def printing(self, document):
        # Meaningful implementation
        pass

    def scan(self, document):
        raise NotImplementedError('This method is not usable')

    def fax(self, document):
        # Meaningful implementation
        raise NotImplementedError('This method is not usable')

    def photocopy(self, document):
        # Meaningful implementation
        pass


from abc import ABC, abstractmethod

class Printing(ABC):
    @abstractmethod
    def printing(self, document):
        pass

class Scanning(ABC):
    @abstractmethod
    def scanning(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Photocopy(ABC):
    @abstractmethod
    def photocopy(self, document):
        pass


class OldMachine(Printing):
    def printing(self, document):
        # Meaningful implementation
        pass

class MultiFunctionMachine(Printing, Scanning):
    def printing(self, document):
        # Meaningful implementation
        pass

    def scanning(self, document):
        # Meaningful implementation
        pass

class AdvancedMachine(Printing, Scanning, Fax, Photocopy):
    def printing(self, document):
        # Meaningful implementation
        pass

    def scan(self, document):
        # Meaningful implementation
        pass

    def fax(self, document):
        # Meaningful implementation
        pass

    def photocopy(self, document):
        # Meaningful implementation
        pass


class MultiFunctionDevice(Printing, Scanning):
    @abstractmethod
    def printing(self, document):
        pass

    @abstractmethod
    def scanning(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):

    def printing(self, document):
        # Meaningful implementation
        pass

    def scan(self, document):
        # Meaningful implementation
        pass