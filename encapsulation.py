# Encapsulation

# Public

class A:
    def __init__(self,a,b):
        self.a = a # public
        self.b = b # public

obj = A(10,20)

# Accessing public 
print(obj.a)
print(obj.b)


# Private

class A:
    def __init__(self,a,b):
        self.__a = a # private
        self.__b = b # private

obj = A(10,20)

# Accessing private 
print(obj.a)
print(obj.b)


# Protected

class A:
    def __init__(self,a,b):
        self._a = a # protected
        self._b = b # protected

obj = A(10,20)

# Accessing protected
print(obj.a)
print(obj.b)