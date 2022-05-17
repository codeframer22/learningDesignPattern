
class Employee:

    def __init__(self):
        # Gerenal Information
        self.name = None
        self.mobile_number = None
        # Address
        self.street = None
        self.postcode = None
        self.city = None
        # Employment Details
        self.employment_number = None
        self.position = None
        self.annual_income = None

    def specification(self):
        return f'{self.name}, {self.mobile_number} ' \
               f'Address: {self.street}, {self.postcode}, {self.city} '\
                f'Employment Details: {self.employment_number}, {self.position}, {self.annual_income}'


class GeneralInfoBuilder:

    def __init__(self, employee=Employee()):
        self.employee = employee

    def setname(self, name):
        self.employee.name = name
        return self

    def setmobilenumber(self, number):
        self.employee.mobile_number = number
        return self




class AddressBuilder(GeneralInfoBuilder):

    def setstreet(self, street):
        self.employee.street = street
        return self

    def setpostcode(self, postcode):
        self.employee.postcode = postcode
        return self

    def setcity(self, city):
        self.employee.city = city
        return self



class EmploymentBuilder(AddressBuilder):

    def setemploymentnumber(self, number):
        self.employee.employment_number = number
        return self

    def setposition(self, position):
        self.employee.position = position
        return self

    def setannualincome(self, income):
        self.employee.annual_income = income
        return self

    def build(self):
        return self.employee

eb = EmploymentBuilder()

employee = eb\
            .setname('Mr.Employee')\
            .setmobilenumber('+919999999999')\
            .setstreet('Clean Street')\
            .setpostcode('123456')\
            .setcity('Nice City')\
            .setemploymentnumber('1111')\
            .setposition('Engineer')\
            .setannualincome(500000)\
            .build()

print(employee.specification())











































