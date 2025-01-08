import pandas as pd
screen_time=[4,6,5]
stu_name=['asad','karthik','chintu']
id = [1,2,3]
my_dict={"id":id,"screen_time":screen_time,"stu_name":stu_name}
print(my_dict)
df=pd.DataFrame(my_dict)
print(df)

list =[1,2,3,4,5]
res=[i+5 for i in list]
print(res)

list =[1,2,3,4,5]
res=[i for i in list if i%2==0]
print(res)

list =[1,2,3,4,5]
res=[i for i in list if i%2!=0]
print(res)

dict1={"a":1,"b":2,"c":3}
#key and value are variables
result={value:key for key,value in dict1.items()}
print(result)

dict1 = {"a": 1, "b": 2, "c": 3}
#key and value are variables
result = {value: key for key, value in zip(dict1.keys(), dict1.values())}
print(result)

import math
numbers=[1,4,9,16,25]
res = tuple(math.sqrt(i) for i in numbers)
print(res)

lists = [
    {"name": "laptop", "price": 800},
    {"name": "smartphone", "price": 500},
    {"name": "Tablet", "price": 300}
]

affordable_products = {i["name"]: i["price"] for i in lists if i["price"] <= 500}
print(affordable_products)

a = [2, 3, 5, 7, 11]
b = [x**2 for x in a]
print(b)

b = [x**2 for x in range(2,12)]
print(b)

a=["madam","radar","abc"]
b=[i for i in a if i==i[::-1]]
print(b)

list=[1,2,3,4,5,6]
list1=[1,4,2,7,8,9,]
result=[i for i in list if i in list1]
print(result)