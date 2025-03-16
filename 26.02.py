
# 1
# Write a program that prompts the user to create an empty list. Then, the user should be able to add elements to the list using three different methods: append(), extend(), and insert().
# Use append() to add a single element to the end of the list.
# Use extend() to add multiple elements (from another list or iterable) at the end of the list.
# Use insert() to add an element at a specific index in the list.



# def foo():
#     elements = []
#     while (choice := input("\n1-Append 2-Extend 3-Insert 4-Exit: ")) != '4':
#         if choice == '1':
#             elements.append(input("Value: "))
#         elif choice == '2':
#             elements.extend(input("Values: ").split())
#         elif choice == '3':
#             elements.insert(int(input("Index: ")), input("Value: "))
#         else:
#             print("Invalid choice.")
#         print("List:", elements)
    
# print(foo())






# 2
# Extend the previous program to allow the user to remove elements using two methods: remove() and pop().
# Use remove() to remove a specific element by its value.
# Use pop() to remove an element at a specific index.

# def foo():
#     elements = []
#     while (choice := input("\n1-Append 2-Extend 3-Insert 4-Remove 5-Pop 6-Exit: ")) != '6':
#         if choice == '1':
#             elements.append(input("Value: "))
#         elif choice == '2':
#             elements.extend(input("Values: ").split())
#         elif choice == '3':
#             elements.insert(int(input("Index: ")), input("Value: "))
#         elif choice == '4':
#             try:
#                 elements.remove(input("Value to remove: "))
#             except ValueError:
#                 print("Value not found.")
#         elif choice == '5':
#             try:
#                 print("Removed:", elements.pop(int(input("Index to pop: "))))
#             except (IndexError, ValueError):
#                 print("Invalid index.")
#         else:
#             print("Invalid choice.")
#         print("List:", elements)

# print(foo())        





# 3
# Write a program that prompts the user to create a list containing different types of elements (integers, strings, floating-point numbers, etc.). Allow the user to add elements of different types to the list using append(), extend(), and insert().
# The user should be able to add elements of different types (e.g., int, float, str) to the list.
# Demonstrate adding elements using all three methods.



# def foo():
#     elements = []
#     while (c := input("\n1-Append 2-Extend 3-Insert 4-Exit: ")) != '4':
#         try:
#             if c == '1': elements.append(eval(input("Value: ")))
#             elif c == '2': elements.extend(map(eval, input("Values: ").split()))
#             elif c == '3': elements.insert(int(input("Index: ")), eval(input("Value: ")))
#             else: print("Invalid choice.")
#         except Exception as e:
#             print("Error:", e)
#         print("List:", elements)

# print(foo())




# 4
# Write a program to create a list and a tuple with some elements. Print them and display their types.

# list=[2,5,7,9]
# tuple=(5,3,6,7)

# print("list:",list)
# print("tuple:",tuple)
# print("type of list:",type(list))
# print("type of tuple:",type(tuple))


# 5
# Write a program to count the occurrences of a specific element in a list and tuple.

# list=[5,3,6,9,5,4,5]
# tuple=(5,6,9,4,7,5)

# count_element=5
# list_count = list.count(count_element)
# tuple_count = tuple.count(count_element)


# print(f"Element {count_element} occurs {list_count} times in the list.")
# print(f"Element {count_element} occurs {tuple_count} times in the tuple.")


# 6
# Write a program to find and print the maximum and minimum values in a list and a tuple.


# list=[5,6,19,4,7]
# tuple=(5,6,22,4,7,3)

# max_list=max(list)
# min_list=min(list)
# max_tuple=max(tuple)
# min_tuple=min(tuple)

# print(f"Maximum value in the list: {max_list}")
# print(f"Minimum value in the list: {min_list}")
# print(f"Maximum value in the tuple: {max_tuple}")
# print(f"Minimum value in the tuple: {min_tuple}")



# 7
# Write a program to access elements from a nested list and a nested tuple.

# list=[[1,5,7],[5,9,6],[4,6,7]]
# tuple=((1,5,8),(1,9,6),(4,5,8))

# list_element=list[1][2]
# tuple_element=tuple[0][2]

# print(f"Element from nested list: {list_element}")
# print(f"Element from nested tuple: {tuple_element}")





# 8
# Write a program to find the sum of all elements in a list and a tuple.

# list=[5,6,19,4,7]
# tuple=(5,6,22,4,7,3)

# list_sum = sum(list)
# tuple_sum = sum(tuple)


# print(f"Sum of elements in the list: {list_sum}")
# print(f"Sum of elements in the tuple: {tuple_sum}")




# 9
# Write a program to reverse a list and a tuple.

# list=[5,6,19,4,7]
# tuple=(5,6,22,4,7,3)

# reversed_list = list[::-1]

# reversed_tuple = tuple[::-1]


# print(f"Reversed list: {reversed_list}")
# print(f"Reversed tuple: {reversed_tuple}")


# 10
# Create a program that adds, subtracts, multiplies, and divides two integers, two floats, and a combination of both.


# int1 = 17
# int2 = 21
# float1 = 5.5
# float2 = 6.5


# int_add = int1 + int2
# int_sub = int1 - int2
# int_mul = int1 * int2
# int_div = int1 / int2 if int2 != 0 else "Division by zero is not allowed"


# float_add = float1 + float2
# float_sub = float1 - float2
# float_mul = float1 * float2
# float_div = float1 / float2 if float2 != 0 else "Division by zero is not allowed"


# int_float_add = int1 + float1
# int_float_sub = int1 - float1
# int_float_mul = int1 * float1
# int_float_div = int1 / float1 if float1 != 0 else "Division by zero is not allowed"


# print("Operations on two integers:")
# print(f"{int1} + {int2} = {int_add}")
# print(f"{int1} - {int2} = {int_sub}")
# print(f"{int1} * {int2} = {int_mul}")
# print(f"{int1} / {int2} = {int_div}")

# print("\nOperations on two floats:")
# print(f"{float1} + {float2} = {float_add}")
# print(f"{float1} - {float2} = {float_sub}")
# print(f"{float1} * {float2} = {float_mul}")
# print(f"{float1} / {float2} = {float_div}")

# print("\nOperations on an integer and a float:")
# print(f"{int1} + {float1} = {int_float_add}")
# print(f"{int1} - {float1} = {int_float_sub}")
# print(f"{int1} * {float1} = {int_float_mul}")
# print(f"{int1} / {float1} = {int_float_div}")




# 11
# Write a program to calculate the product of two complex numbers.


# complex1 = 5 + 3j
# complex2 = 3 + 7j
# product = complex1 * complex2

# print(f"The product of {complex1} and {complex2} is {product}")




# 12
# Create a fraction that represents 1/2 and another fraction representing 2/3. Add them and print the result.


# from fractions import Fraction

# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(2, 3)

# result = fraction1 + fraction2

# print(f"The sum of {fraction1} and {fraction2} is {result}")




# 13
# Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.

# from decimal import Decimal

# decimal_sum = Decimal('0.1') + Decimal('0.2')

# float_sum = 0.1 + 0.2


# print(f"Sum using Decimal: {decimal_sum}")
# print(f"Sum using float: {float_sum}")


# if decimal_sum == float_sum:
#     print("The results are equal.")
# else:
#     print("The results are not equal.")




# 14
# Write a program to check if the sum of three numbers is equal to 100. Use boolean comparisons to print the result as True or False.
 
# num1=30
# num2=20
# num3=50

# result=(num1+num2+num3)==100

# print(result)



# 15
# Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them. 
# Use the fractions.Fraction class to handle fractions and print the resulting fraction in its simplified form.


# from fractions import Fraction

# fraction1_input = input("Enter the first fraction (a/b): ")
# fraction2_input = input("Enter the second fraction (a/b): ")

# fraction1 = Fraction(fraction1_input)
# fraction2 = Fraction(fraction2_input)

# result = fraction1 * fraction2

# print(f"The result of multiplying {fraction1} and {fraction2} is {result}")





# 16
# Accept two fractions from the user and find their GCD using the math.gcd() function along with the numerator and denominator attributes of each fraction.

# from fractions import Fraction
# import math

# fraction1 = input("Enter the first fraction (a/b): ")
# fraction2 = input("Enter the second fraction (a/b): ")

# fraction1 = Fraction(fraction1)
# fraction2 = Fraction(fraction2)

# gcd_numerator = math.gcd(fraction1.numerator, fraction2.numerator)
# gcd_denominator = math.gcd(fraction1.denominator, fraction2.denominator)

# print(f"The GCD of the numerators is: {gcd_numerator}")
# print(f"The GCD of the denominators is: {gcd_denominator}")




# 17
# Write a program to check if a number is even or odd


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")




# 18
# Compare the values of a float and an int and print whether they are equal or not.


# float_num = float(input("Enter a float number: "))
# int_num = int(input("Enter an integer number: "))

# if float_num == int_num:
#     print("The float and integer values are equal.")
# else:
#     print("The float and integer values are not equal.")




# 19
# Calculate the square of an integer and a float using the exponentiation operator (**).


# int_num = int(input("Enter an integer: "))
# float_num = float(input("Enter a float: "))

# int_square = int_num ** 2
# float_square = float_num ** 2

# print(f"The square of the integer {int_num} is {int_square}.")
# print(f"The square of the float {float_num} is {float_square}.")




# 20
# Write a program to find the maximum of three numbers using nested conditional operators.


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

# print(f"The maximum number is: {max_num}")




# 21
# Accept two integer inputs from the user and calculate the absolute difference between them using the abs() function. Print the result.


# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))

# difference = abs(num1 - num2)

# print(f"The absolute difference between {num1} and {num2} is {difference}.")



# 22
# Accept an integer input from the user and use conditional statements to print whether the number is positive, negative, or zero.


# num = int(input("Enter an integer: "))

# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")




# 23
# Accept two integer inputs from the user. Check if the first number is a multiple of the second and print True if it is, otherwise print False.


# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))

# is_multiple = num1 % num2 == 0

# print(is_multiple)

