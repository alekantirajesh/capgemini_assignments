# assignment2
# find area of rectangle using type conversion and format string 

x=int(input())
y=int(input())

area=float(x)*float(y)

print(f"area of rectangle is {area}")

# assignment 2

x=input("enter inputname \n")
y=input("enter password \n")

t=0
if x=="testuser":
    while t<3:
        if y=='Password123':
            print("valid user")
            break
        else:
            t+=1
            print("try again \n")
            y=input("enter password")
    if t==2:
        print(" 3 chances completed   so  try again after some time ")
else:
    print("invalid credentials enter correct username")

#assign 3

# check given num is prime or not

n=int(input("enter number \n"))
c=0
for i in range(2,int(n/2)+1):
    if n%i==0:
        c+=1
    if c==1:
        break
if c==0:
    print("is prime")
else:
    print("not a prime")



 # calculate tax based on salary
    # gross salary <5lpa   tax 10%
    #   else 20%
    # gross salary
    # net salry
    

net_salary=int(input("enter salary  \n"))
allowance=int(input("enter allowance  \n"))

gross_sal=net_salary+allowance
print(f"total salary = {gross_sal}")

if(gross_sal<5):
    print("tax paid =",gross_sal*0.1)
else:
    print("tax paid =",gross_sal*0.2)

   
  

    # calculate attendence tracker based on no of classes attended 
    # if attendence is above 75 you are eligible for exam
    #     or
    #     not eligible for exam 

total_classes=int(input("total classess"))
class_attended=int(input("classes attended"))
attendence_percentage= (class_attended/total_classes)*100
if(attendence_percentage>75):
    print("eligible")
else:
    print("not eligible")


