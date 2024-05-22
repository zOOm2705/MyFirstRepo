class Human:

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

myFirstObject = Human('Eduard', 'Denisov', 'male', '55')

class Builder(Human):
    pass

class Sailor(Builder):
    pass

class Pilot(Sailor):
    print(myFirstObject)
    print(myFirstObject.first_name + ' ' + myFirstObject.last_name)
    print(myFirstObject.sex)
    print(myFirstObject.age)
