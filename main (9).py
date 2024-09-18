##Принцип ООП Полиморфизм (поли - много, морфизм - образ) - одноимённые методы в разных классах (метод с одним именем может выполнять разные функции)
class Car:
    def move(self):
        print("Едет по дороге")

class Moto:
    def move(self):
        print("Едет по дороге")

class Train:
    def move(self):
        print("Едет по жд")

class Boat:
    def move(self):
        print("Идёт по воде")

lada = Car()
voskhod = Moto()
lastochka = Train()
salut = Boat()

print(lada.move())
print(voskhod.move())
print(lastochka.move())
print(salut.move())
            
            
#добваить класс
class NewRoot:
    def __init__(self, params):
        self.params = params
    def name(self):
        print "вывод атрибута"
                            
        
