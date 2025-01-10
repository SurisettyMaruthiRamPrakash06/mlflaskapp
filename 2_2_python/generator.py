## generator
def square(i):
    #0,1,2,3,4,5,6,7,8,9
    for i in range(i):
        i=i+2
        yield i
        #return n
square(10)
for i in square(10):
    print(i)


## Wrapper

def sample(func):
    def wrapper(item):
        item = item.upper()
        return func(item)  # Call the wrapper function with modified value
    return wrapper
@sample
def process(item):
    return item
# Testing the function
result = process
print(result("hello"))


## Decorators

def dev_dec(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
@dev_dec

def div(a,b):
    #print(a/b)
    #if a<b:
        #a,b=b,a
    return a/b #Perform the division
# Test cases
div(2,4)
    #a/b
    #2/4 0.5 # Normal case
#div() # Division by zero case



##

def dev_dec(func):
    def inner(a, b):
        product = a * b
        if product <= 20:
            print("Not eligible or not qualified.")
            return
        return func(a, b)
    return inner

@dev_dec
def mul(a, b):
    return a * b

print(mul(3, 4))
print(mul(5, 5))


##

def dev_dec(func):
    def inner(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a / b
print(div(4, 0))