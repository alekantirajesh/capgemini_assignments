#day7assignment


class Email:
    def send(self):
        print("the email has been sent")


class Sms:
    def send(self):
        print("th e  sms is sent")

class Push:
    def send(self):
        print("this is push")

def send1(obj):
    obj.send()


obj=Email()
obj1=Sms()
obj2=Push()

send1(obj)
send1(obj1)
send1(obj2)

 
# from abc import ABC,abstractmethod

# class Example(ABC):
#     @abstractmethod
#     def send1 ():
#         pass
#     def eg():
#         print("error")
# class Email(Example):
#     def send1 (self):
#         print("email")
    
    
#     def send(self,a,b):
#         self.b=b
#         self.a=a
    
#         print(f"the  email sent from  : {self.a}   to    : {self.b} ")
        
        


# class Sms(Example):
#     def send1 (self):
#         print("sms")
#     def send(self,a,b):
#         self.b=b
#         self.a=a
        
#         print(f"the  sms sent from  : {self.a}   to    : {self.b} ")
    

# class Push(Example):
#     def send1 (self):
#         print("push")
#     def send(self,a,b):
#         self.a=a
#         self.b=b
#         print(f"the data is pushed to address {self.a}")
    

# def send1(obj):
#   obj.send(a,b)
#   


# obj1=Email()

# obj2=Sms()

# send1(obj1)
# # send1(obj2)



