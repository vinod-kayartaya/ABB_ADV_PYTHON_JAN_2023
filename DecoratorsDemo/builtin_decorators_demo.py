class MyClass:
    __numbers = [10, 20, 30]  # this belongs to the class; all objects share this

    @classmethod
    def add_number(cls, new_number):
        cls.__numbers.append(new_number)

    @staticmethod
    def numbers():
        return MyClass.__numbers

    def __init__(self):
        self.nums = [11, 22, 33]  # this belongs to the object; different objects have different copies


if __name__ == '__main__':
    mc1 = MyClass()
    mc2 = MyClass()

    print(mc1.numbers(), mc1.nums)
    print(mc2.numbers(), mc2.nums)

    # mc1.numbers.append(40)
    MyClass.add_number(200)
    mc1.nums.append(44)
    print(mc1.numbers(), mc1.nums)
    print(mc2.numbers(), mc2.nums)

    mc3 = MyClass()
    print(mc3.numbers(), mc3.nums)
