'''
class Myclass:
    x = 2
    y = 4
    z = 6

    def add_3(self, a ,b):
        sum = self.x+self.y+self.z+a+b
        # print(sum)
        return sum
 
    def div(self):
        divi=self.add_3(5,6)
        # print(divi)
        return divi

object = Myclass()
d=object.div()
print(d)
# contructor 
class Myclass:
     x = 10
     y = 20  
     @staticmethod
     def addtwo():
        sum = Myclass.x +Myclass.y 
        print(sum)

#from static
print(Myclass.x)
print(Myclass.y)
#from object
obj1 = Myclass()
print(obj1.x,obj1.y)
'''
'''
#abstrac
from abc import ABC,abstractclassmethod
class father:
    x = 10
    y = 20
    @abstractclassmethod
    def print0to10(self):
      pass

    def add(self):
       print(self.x + self.y)
        
class son(father):
    pass
    def print0to10(self):
      pass

obj = son()
obj.add()
'''

#Encasulation 
class Banking:
    
    __balance = 0



    def deposit(self,amount):
        if (amount>0):
            self.__balance += amount
            print("deposit sucessess")
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if (amount>0 and amount <= self.__balance) :
            self.__balance -= amount
            print("withdrawal sucess")
        else:
            print("Insufuciant Balance")

    def cheak_balance(self):
        return self.__balance
    

obj = Banking()
obj.deposit(500)
print(obj.cheak_balance())
obj.withdraw(400)
print(obj.cheak_balance())

