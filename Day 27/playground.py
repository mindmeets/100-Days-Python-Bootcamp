def add(*args):
    print(args[0])
    print(args[1])
    total = 0
    if len(args) >= 1:
        for i in args:
            total += i
    return total

print(add(3,5, 6, 2, 1))

def calculate(n, **kwargs):
    # total = 0
    # for key, value in kwargs.items():
    #     if "add" == key:
    #         total += value
    #     elif "multiply" == key:
    #         total *= value
    # print(kwargs)
    # return total
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    return n

print(calculate(n=2, add=3, multiply=5))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Ford") #, model="Mustang")
print(my_car.make, my_car.model)
