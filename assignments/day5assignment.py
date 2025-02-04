
# 1)  calculate count the item frequency from the below products and store it in dictionary
# products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
# i=0
# d={}
# while(i<len(products)):
#     s=""
#     while(i<len(products) and products[i]!=" "):
#         s+=products[i]
#         i+=1
#     if s in d:
#         d[s]+=1
#     else:
#         d[s]=1

    
#     i+=1
# print(d)




# 2) Store management
   #   calculate the current stock and display current stock

# initial_stock = {"apple": 50,"banana": 100,"orange": 75}

# sold_item = {"apple": 10, "banana": 20, "orange": 15}
# current={}
# invalid=0
# for i in initial_stock:
#     if i in sold_item:
#         if initial_stock[i]>sold_item[i]:
#             current[i]=initial_stock[i]-sold_item[i]
#         else:
#             invalid=1
# if invalid==1:
#     print("it is not possible ")
# print(current)



# 3)You have sales data for different regions and want to calculate the total sales for each region.

# sales_data = [
#     {"region": "North", "sales": 15000},
#     {"region": "South", "sales": 8000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
# ]
# new_sales_data={}

# for i in sales_data:
#     if i["region"] not in new_sales_data:
#         new_sales_data[i["region"]]=i["sales"]
#     else:
#         new_sales_data[i["region"]]+=i["sales"]
# print(new_sales_data)

# 4) take input of your mobile number and display it in word format

#  234= two three four

# mobile_number=input("enter number \n")

#  
# alphabet_number=""

# for i in mobile_number:
#     alphabet_number= alphabet_number+ dictionary[i]
# print(alphabet_number)