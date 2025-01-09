# # 1. Program to print numbers from 1 to n and calculate the sum using for and while loops:

n = int(input("Enter a positive integer: "))

for i in range(1, n+1):
    print(i)

i = 1
sum_numbers = 0
while i <= n:
    sum_numbers += i
    i += 1

print("Sum of numbers from 1 to", n, "is:", sum_numbers)


# # 2. Program with a user-defined function calculate_square:

def calculate_square(n):
    return n * n

n = int(input("Enter a positive integer: "))
result = calculate_square(n)
print("The square of", n, "is:", result)