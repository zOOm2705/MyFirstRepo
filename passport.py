class Passport:
    def __init__(self,FIO='Unknown',data='Unknown',city="Unknown",country="Unknown",adress="Unknown"):
        self.FIO = FIO
        self.data = data
        self.city = city
        self.country = country
        self.adress = adress
    def print_data(self):
        return (f'Фамилия имя отчество: {self.FIO},\nДата рождения: {self.data},\nГород: {self.city},\nСтрана: {self.country},\nДомашний адрес: {self.adress}')
    def input_data(self):
        self.FIO = input()
    def print_FIO(self):
        return (self.FIO)
object1 = Human('Ivanov Inav Ivanovich','25.03.1992',"Омск","Россия","Колотушкина 02-05")
object2 = Human()
object1.input_data()
print(object1.print_FIO())
print(object1.FIO)


class ForeignPassport (Passport):
    def ForeignPassport (self):