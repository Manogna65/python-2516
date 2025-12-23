# Exeception Handling
# when no errors occured
print("program execution started")
num1=10
num2=5
print(num1/num2)
print("program execution completed")
print("="*50)

# when  errors occured
print("program execution started")
num1=10
num2=0
# print(num1/num2) ZeroDivisionError: division by zero
print("program execution completed")
print("="*50)

# when  errors occured how execeptions will handle single error
print("program execution started")
num1=10
num2=5
try:
    print(num1/num2)
except:
    print("oops devison cannot undefied with zero in maths")
print("program execution completed")
print("="*50)

# when  errors occured how execeptions will handle multiple error
print("program execution started")
data=[1,2,"python",0,3]
for i in data:
    try:
        print(1/i)
    except TypeError:
        print("oops! dont pass strings in maths we cannot divide strings and numbers")
    except ZeroDivisionError:
        print("oops devison cannot undefied with zero in maths")
print("program execution completed")
print("="*50)

print("program execution started")
num1=10
num2=5
try:
    print(num1/num2)
except:
    print("oops devison cannot undefied with zero in maths")
else:
    print("calculation completed")
finally:
    print("program execution completed")
print("="*50)


# exception class
# print(help(exception))
# based on our req ----->we need custom exception
class agetooyoungerror(Exception):
    pass

class Noiderror(Exception):
    pass

age=int(input("Enter your age: "))
if age<18:
    raise agetooyoungerror("you must need above 18 age to register")
else:
    has_id = input("do you have id? (yes/no)")
    if has_id != "yes":
        raise Noiderror("you must have id to register")
print("registration succesfull")