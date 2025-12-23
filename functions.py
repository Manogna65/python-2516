# without functions

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# with function
a=100
b=200

# define function----->100,200
def arthematic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
arthematic()

# call function------->1000,2000
a=1000
b=2000
arthematic()

# functions with parameters
def arthematic(a,b): #---->(a,b)parameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
# arthematic()---->error
# arthematic(100)---->error
arthematic(100,200)

# positional argumets
def login(username,password):
    if username == "manu" and password == "12345":
        print("login success")
    else:
        print("login failed")

login("manu","12345") #exact order
login("manu","123")   #exact order wrong password
login("12345","manu") #order changed with correct details

# default arguments
def emp_inf(emp_name,emp_email,emp_loc="hyd"): #----giving everyon same location "=" use to parameter
    print(f"Hello {emp_name} your mail is {emp_email} and location is {emp_loc}")

#emp_inf()----->emp_inf() missing 3 required positional arguments: 'emp_name', 'emp_email', and 'emp_loc'
emp_inf("manu","manu@gmail.com","hyd")
emp_inf('kedar',"kedar@gamil.com")

# keyword arguments
def emp_inf(emp_name,emp_email,emp_loc="hyd",adress="india"):
    print(f"Hello {emp_name} your mail is {emp_email} and location is {emp_loc} actually from {adress}")

emp_inf(emp_name="manu",emp_email="manu@gmail.com")

# arbitrary arguments
def add_all(*numbers):
    total=0
    for i in numbers:
        total = total+i
    print(f"total is {total}")

add_all(1)
add_all(1,2)
add_all(1,2,3,4,5,6)

# arbitrary keyword arguments
def profile(**info):
    print(info)

profile()
profile(id="123")
profile(id="1234",name="manu")
profile(id="1234",name="manu",rating=4.5)

# using both *args and **kwargs
def cred_trans_new(*trans,**info):
    print(trans)
    print(info)
    total=0
    for i in trans:
        total=total+i
    print(f"hii {info['name']} you have done {total} amount of transaction ")

cred_trans_new(1000,2000,3000,name="manu",email="manu@gamil.com")

# functions without return key word
def add(a,b):
    a+b
print(add(100,200))

# functions with return key word
def add(a,b):
    return a+b
print(add(100,200))

# when using return,give appropriate responses
def add(a,b):
    return "hello"
print(add(100,200))

def new_math(a,b):
    return a+b
    return a-b
    return a*b

print(new_math(10,20))

# local scope for variables
def add():
    # local variables are b and c
    b=5
    c=6
    print(b) #accesing inside function
    print(c) #accesing inside function
add()

# global varaible
a=30
def add(b,c):
    print(b)
    print(c)
    print(a)
add(1,2)

# without lambda
def add(a,b):
    return a+b
print(add(3,4))

# with lambda 
sum=lambda a,b: a+b
print(sum)
print(sum(5,6))

# IILE
print((lambda a,b: a+b) (100,200))
print((lambda a,b: a-b) (100,200))
print((lambda a,b: a*b) (100,200))
print((lambda a,b: a/b) (100,200))

# without MAP 
# input [1,2,3,4]---->output [1,4,9,16]
def square_list(numbers):
    squared_list = []
    for n in numbers:
        squared_list.append(n*n)
    return squared_list

print(square_list([1,2,3,4]))

# with MAP 
# input [1,2,3,4,5]---->output [1,4,9,16,25]
# one liner function 
print(list(map(lambda n: n*n, [1,2,3,4,5])))

# print(list(map(lambda n: n+n, [100,200])))

# without FILTER
# input [1,2,3,4,5,6,7,8,9,10]---->output[2,4,6,8,10]
def even_list(numbers):
    even_nums = []
    for n in numbers:
        if n % 2 ==0:
            even_nums.append(n)
    return even_nums

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# with filter
# input [1,2,3,4,5,6,7,8,9,10]---->output[2,4,6,8,10]
# one liner functions
print(list(filter(lambda n: n % 2 ==0,[1,2,3,4,5,6,7,8,9,10])))

# without REDUCE
# input [1,2,3,4]----->output[1*2*3*4*=24]
def multiply_list(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return result
print(multiply_list([1,2,3,4]))

# with REDUCE
# input [1,2,3,4]----->output[1*2*3*4*=24]
from functools import reduce
print(reduce(lambda x,y: x*y,[1,2,3,4]))
