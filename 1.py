class Human:
    def __init__(self,FIO='Unknown',data='Unknown',phone="Unknown",city="Unknown",country="Unknown",adress="Unknown"):
        self.FIO = FIO
        self.data = data
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress
    def print_data(self):
        return (f'Фамилия имя отчество: {self.FIO},\nДата рождения: {self.data},\nКонтактный телефон: {self.phone},\nГород: {self.city},\nСтрана: {self.country},\nДомашний адрес: {self.adress}')
object1 = Human('Ivanov Inav Ivanovich','25.03.1992',"88005553535","Омск","Россия","Колотушкина 02-05")
object2 = Human()
print(object1.print_data())