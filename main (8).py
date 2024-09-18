#Ассоциация - наследование при котором один класс является полем другого класса (целое состоит из частей)
#Асоциация-Композиция - в UML (Унифицированный язык моделирования) - линия с незакрашенным ромбом (часть удалена объект - целое удаляется)
class Salary:
    def __init__(self, pay):
        self.pay = pay
        #Метод вывода зп за год
    @property
    def getSummofYear(self):
        return int(self.pay*12)

class Worker:
    def __init__(self, pay, bonus, name):
        self.pay = pay
        self.bonus = bonus
        self.name = name
        
#Метод - выводит зп сотрудниказа год вместе с премией
    def getSummofYearforWorker(self):
        return f"Зарплата вместе с премией у сотрудника {self.name} состовляет {self.bonus + self.pay.getSummofYear}"

class Tax:
    def __init__(self, pay,bonus,tax,name_tax):
        self.pay = pay
        self.bonus = bonus
        self.name_tax = name_tax
        self.tax = tax
        self.salary = Salary(self.pay)
    @property   
    def getTaxofYear(self):
        return (self.bonus + self.salary.getSummofYear) * self.tax / 100

    @property
    def getInformationOfTax(self):
        return f"Сумма налога {self.name_tax} за год составила {self.getTaxofYear} Рублей"
        
# Объект - зарплата за месяц 
salary_of_month = Salary(20000)
print(salary_of_month.getSummofYear)
sasha = Worker(salary_of_month, 20000, 'Саша')
print(sasha.getSummofYearforWorker())
tax = Tax(20000,20000,13,'Подоходный для физических лиц')
print(tax.getInformationOfTax)         