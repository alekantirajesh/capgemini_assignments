
# 1) convert the prices in USD & Euro using appropriate function
#     PricesList_inr =[3000,56000,45000,2300]

# 2) student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayanan","Nithin Rajesh","Mani Prasad"]
#     List the name which has more than 6 characters as lone_names list using appropriate function

# 3) products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
#     Display the Product in ascending order based on the price of the product

# 4) You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order

# 5) You have a list of cities with their population data. Sort the cities in descending order of their population.
#    cities = [
#     {"name": "New York", "population": 8419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]

# 6) Extract Emails of Verified Users
#   You have a list of user records with email and a verification status. Extract the emails of verified users.
# 	users = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]

# 7) Calculate Discounts for Products
#  You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and return the updated prices.

# 	products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
# ]
# list out discounted products

# 8) sort Words by Length
#   Sort them in ascending order of their lengths.
# 	words = ["apple", "banana", "cherry", "date", "fig"]


# 9) write a program to remove the duplicates in the list
# # numbers3=[2,2,4,6,3,4,6,1]




PricesList_inr =[3000,56000,45000,2300]

# 1 usd = 86.43 Inr
# 1 euro =  90.43 euro

usd= map(lambda x: x/86.43,PricesList_inr)
euro=map(lambda x: x/90.43,PricesList_inr)

print(list(usd))
print(list(euro))
 


#     List the name which has more than 6 characters as lone_names list using appropriate function

student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayanan","Nithin Rajesh","Mani Prasad"]

lone_names=filter(lambda x: len(x)>6,student_name_list)

print(list(lone_names))

products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]
#     Display the Product in ascending order based on the price of the product

np=sorted(products,key=lambda x:x["price"])

print(np)

# 4) You have a list of numbers. Filter out the odd ones, double the even 
# numbers, and sort them in ascending order

numbesrs=[1,2,3,4,5,6,7,8,9,10]

evenlist=filter(lambda x:  x%2==0    ,numbesrs )

evenlist1=list(evenlist)
evenlist1.sort()
doubled_evenlist=map(lambda x:2*x ,evenlist1)

print(list(doubled_evenlist))

numbesrs=[1,2,3,4,5,6,7,8,9,10]
evenlist2=map(lambda x: 2*x if x%2==0 else  numbesrs.remove(x),numbesrs )

print(list(evenlist2))

cities = [
    {"name": "New York", "population": 2319600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 8919600}
]

new_cities=sorted(cities,key=lambda x:(-x["population"]))

print(new_cities)




users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]


new_user=filter(lambda x: x["verified"]==True,users)

print(list(new_user))




#  7) Calculate Discounts for Products
#  You have a list of products with their prices. Apply a 20% discount to products 
# costing more than $100 and return the updated prices.

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
]

x=filter(lambda x:x['price']>100 ,products )

nx=list(x)
print(nx)
nnx=map(lambda x:x["price"]*0.8,nx)

print(list(nnx))
print(nx)




words = ["apple", "banana", "cherry", "date", "fig"]
new_words=sorted(words,key=lambda x :len(x))
print(new_words)

numbers3=[2,2,4,6,3,4,6,1]

d={}

for i in numbers3:
    if i not in  d:
        d[i]=1
print(d) 

numbers4=list(d.keys())
print(numbers4)

s=set()
numbers3=[2,2,4,6,3,4,6,1]

for i in numbers3:
    s.add(i)
l=list(s)
print(l)




# claculate the total amount  based price and quantity as input from user

price=int(input("enter price of 1 unit"))
quantity=int(input("enter quantity "))

amount=lambda x,y: x*y

print(amount(price,quantity))