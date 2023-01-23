import oop_ex04


class Employee(oop_ex04.Person):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary', 45000)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError('Invalid type of data for id')
        if value < 1 or value > 99999:
            raise ValueError('ID must be between 1 and 99999')
        self.__id = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise ValueError('Invalid type of data for salary')
        if value < 35000 or value > 500000:
            raise ValueError('salary must be between 35000 and 500000')
        self.__salary = value

    def __str__(self):
        return f'Employee(id={self.__id}, salary={self.__salary}, {super().__str__()})'


if __name__ == '__main__':
    e1 = Employee(id=1122, name='Ramesh', age=43, salary=85000)
    print(e1)
