#Finding Prime numbers in the list
list1=[1,2,4,5,6]
def is_prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
def find_primelist(list1):
    prime_numbers=[num for num in list1 if is_prime(num)]
    return prime_numbers
prime = find_primelist(list1)
print("Prime numbers in the list:", prime)

# Write a program that takes a positive integer N and prints the sum of the first N natural numbers.
def natural_sum(num):
    sum1 = 0
    for i in range(1, num + 1):
        sum1 += i
    return sum1

num = int(input("Enter a number: "))
sum_of_natural_numbers = natural_sum(num)
print("The sum of the first", num, "natural numbers is:", sum_of_natural_numbers)

# Write a program that takes a positive integer N and prints the factorial of N
def factorial(number):
    if number < 0:
        print("Negative number doesnt have any factorial!")
    if number == 0:
        return 1
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact
number=int(input("Enter a number: "))
result=factorial(number)
print("The factorial of",number, "is: ", result)

# Write a program that prints all prime numbers between 1 and 100
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print("Prime numbers between",start, "and" ,end,"are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
print_primes_in_range(1, 100)

        
# Write a program that takes a number as input and prints its multiplication table of a particular number
def multiplication_table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

user_input = int(input("Enter a number: "))
multiplication_table(user_input)

# Write a program that takes a number and prints the fibonacci number of that particular number
def fibonacci(n):
    if n <= 0:
        print("Invalid input!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def print_fibonacci_number(num):
    result = fibonacci(num)
    print("The Fibonacci number for ",num,"is:",result)

num = int(input("Enter a number: "))
print_fibonacci_number(num)
