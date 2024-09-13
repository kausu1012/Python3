class Complex:
    def __init__(self,real, img):
        self.real = real
        self.img = img

    def showno(self):
        print(self.real , "i +" , self.img , "j" )

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return Complex(newReal,newImg) 

    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img 
        return Complex(newReal,newImg) 
num1 = Complex(2,4)
num1.showno()

num2 = Complex(3,8)
num2.showno()

num3= num1 + num2
num3.showno()

num4= num2 - num1
num4.showno()


# class Student:
#     def __init__(self,phy,chem,math): 
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3)  + "%"

# Std1 = Student(78,98,45)
# print(Std1.percentage)
# Std1.phy = 95
# print(Std1.percentage)





# class Car:
#     def __init__(self,type): 
#        self.type = type 

#     @staticmethod
#     def Start():
#         print("The car is started")

#     @staticmethod
#     def Stop():
#         print("The car has been stoped")

# class TyotaCar(Car):
#     def __init__(self,name,type): 
#        super().__init__(type)
#        self.name = name 

# Car1 = TyotaCar("Foutuner","Electric")
# print(Car1.type)

# class Person:
#     def __init__(self): 
#         __name = "annonymous"

#     def __hello(self):
#         print("Hello Person! ")

#     def welcome(self):
#         self.__hello()

# P1 = Person()
# print(P1.welcome())

 # class Account:
#     def __init__(self,acc_no, acc_pass): 
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass():
#         print(self.__acc_pass)

# acc1 = Account("12345","awdfth")

# print(acc1.acc_no)
# print(acc1.__acc_pass)



# class Student():
    
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Kaushal")
# del s1
# print(s1)    


# class Circle:
#     def __init__(self,r):
#         self.r = r

#     def area(self):
#         return (22/7) * self.r ** 2
    
#     def Peri(self):
#         return 2 * (22/7) * self.r
    
# r1 = Circle(21)
# print(r1.area())
# print(r1.Peri())

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role 
        self.dept = dept 
        self.salary = salary

    def showDetails(self):
        
        print("The Role is", self.role )  
        print("The Dep is", self.dept )
        print("The Sal is", self.salary )
    
class Engineer(Employee):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Chief","Civil","75000")
        
emp1 = Employee("Manager","DIGItech","89000")
emp1.showDetails()

print('\n')
engg1 = Engineer("shubham","22")
engg1.showDetails()




