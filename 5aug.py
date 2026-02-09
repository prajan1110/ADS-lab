#ADDING 2 NUMBERS
def add_two_numbers(var1,var2):
    sum = var1+var2
    print(f"The sum of {var1} and {var2} is {sum}")

var1 = 4
var2 = 6
add_two_numbers(var1,var2)

#SUM OF ALL THE NUMBER IN A LIST
list1=[1,2,3,4,5]
sum = 0
for number in list1:
    sum = sum+number
print(f"The sum of all the numbers in the List is {sum}")


def sum_of_no_in_list(list1, total_sum):
    for number in list1:
        total_sum += number
    print(total_sum)

list1 = [1,2,3,4,5]
total_sum = 0
sum_of_no_in_list(list1,total_sum)


#SUM OF EVEN NUMBERS IN A LIST
list1=[1,2,3,4,5]
even_sum = 0
for number in list1:
    if number % 2 == 0:
        even_sum = even_sum+number
print(f"The sum of even numbers in the List is {even_sum}")


def sum_even(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0: 
            even_sum += number
    return even_sum

list1 = [1,2,3,4,5]
result = sum_even(list1)
print("Sum of even numbers in list is", result)


#SUM OF ODD NUMBERS IN A LIST
list1=[1,2,3,4,5]
odd_sum = 0
for number in list1:
    if number % 2 != 0:
        odd_sum = odd_sum+number
print(odd_sum)

def sum_odd(numbers):
    odd_sum = 0
    for number in numbers:
        if number % 2 != 0:
            odd_sum += number
    return odd_sum

list1 = [1,2,3,4,5]
result = sum_odd(list1)
print("Sum of odd numbers in list is",result)

#Prime nos.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is prime number.")
else:
    print(f"{number} is not a prime number.")