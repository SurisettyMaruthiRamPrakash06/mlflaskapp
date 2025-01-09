# generator
def square(i):
    #0,1,2,3,4,5,6,7,8,9
    for i in range(i):
        i=i+2
        yield i
        #return n
square(10)
for i in square(10):
    print(i)


# Wrapper

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