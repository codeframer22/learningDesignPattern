

class Employee:

    def __init__(self):
        # Address
        self.street = None
        self.postcode = None
        self.city = None
        # Employment Details
        self.employment_number = None
        self.position = None
        self.annual_income = None

    def specification(self):
        return f'Address: {self.street}, {self.postcode}, {self.city} '\
                f'Employment Details: {self.employment_number}, {self.position}, {self.annual_income}'

class EmployeeBuilder:

    def __init__(self, employee=Employee()):
        self.employee = employee

    @property
    def address_info(self):
        return AddressBuilder(self.employee)

    @property
    def employment_info(self):
        return EmploymentBuilder(self.employee)

    def build(self):
        return self.employee

class AddressBuilder(EmployeeBuilder):

    def __init__(self, employee):
        super().__init__(employee)

    def setstreet(self, street):
        self.employee.street = street
        return self

    def setpostcode(self, postcode):
        self.employee.postcode = postcode
        return self

    def setcity(self, city):
        self.employee.city = city
        return self

class EmploymentBuilder(EmployeeBuilder):

    def __init__(self, employee):
        super().__init__(employee)

    def setemploymentnumber(self, number):
        self.employee.employment_number = number
        return self

    def setposition(self, position):
        self.employee.position = position
        return self

    def setannualincome(self, income):
        self.employee.annual_income = income
        return self

eb = EmployeeBuilder()

employee = eb\
            .address_info\
                .setstreet('Clean Street')\
                .setpostcode('123456')\
                .setcity('Nice City')\
            .employment_info\
                .setemploymentnumber('1111')\
                .setposition('Engineer')\
                .setannualincome(500000)\
            .build()

print(employee.specification())











































