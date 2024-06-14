#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT

# In[3]:


#1.  Write a program that takes two numbers as input and prints their sum

num1 = float(input("Enter the first number: "))    #taking first number as input
num2 = float(input("Enter the second number: "))   #taking second number as input
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)


# In[4]:


#2. Write a python program that checks whether a given number is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")


# In[6]:


#3.  Write a python program that calculates the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print("The factorial of", number, "is", result)


# In[8]:


#4. Write a program that asks the user for their name and then prints a greeting message

name = input("Enter your name: ")
print(f"Hello, {name}! Nice to meet you.")


# In[7]:


#5. Write a program that takes a string input from the user and writes it to a text file.

user_input = input("Enter a string to write to the file: ")
filename = "output.txt"
with open(filename, 'w') as file:
    file.write(user_input)

print(f"The string has been written to {filename}.")


# In[13]:


#6. Write a program that reads the content of a text file and prints it to the console.

file_name = "output.txt"

with open(file_name, "r") as file:
        content = file.read()
        print(content)
 


# In[20]:


#7. Write a python program that takes a string as input and returns its length.

user_input = input("Enter a string: ")

length_of_string = len(user_input)

print(f"The length of the string is:,{length_of_string}")


# In[22]:


#8. Write a python program that concatenates two strings and returns the result.

first_string = input("Enter the first string: ")

second_string = input("Enter the second string: ")

result = first_string + second_string

print("The concatenated string is:", result)


# In[24]:


#9.  Write a python program that checks if a substring is present in a given string.

main_string = input("Enter the main string: ")

substring = input("Enter the substring to check: ")

if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")


# In[25]:


#10.  Write a python program that converts a given string to uppercase.

input_string = input("Enter a string: ")

uppercase_string = input_string.upper()

print("Uppercase version of the string:", uppercase_string)


# In[26]:


#11. Write a python program that generates the first n numbers in the Fibonacci sequence.

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_numbers = fibonacci_sequence(n)
print(f"The first {n} numbers in the Fibonacci sequence:")
print(fib_numbers)


# In[28]:


#12.  Write a python program that calculates the sum of the digits of a given number.
 
def sum_of_digits(number):
    sum_digits = 0
    
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print(f"The sum of digits of {number} is: {result}")


# In[29]:


#13. Write a program that asks the user for their birth year and calculates their age.

from datetime import datetime
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))

age = calculate_age(birth_year)

print(f"You are {age} years old.")


# In[30]:


#14.  Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines = []

while True:
    line = input("Enter a line (press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("\nLines entered:")
for line in lines:
    print(line)


# In[35]:


#15.  Write a program that reads data from a CSV file and prints it to the console.
import csv

#MAKING A CSV FILE

data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Jane', 30, 'San Francisco'],
    ['Doe', 28, 'Los Angeles']
]

file_name = 'data.csv'

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_name}' has been created.")

print("-----------------------------------------------------------------")

#READING THE CSV FILE

file_path = 'data.csv'

with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(', '.join(row))



# In[36]:


#16.  Write a program in python that counts the frequency of each character in a string
def count_characters(s):
    char_freq = {}

    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    return char_freq
input_string = input("Enter a string: ")

frequency = count_characters(input_string)

print("Character frequencies:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")


# In[38]:


#17. Write a program in python that converts a given string to title case (first letter of each word capitalized)
def title_case(input_string):
    words = input_string.split()
    title_case_words = []

    for word in words:
        title_case_words.append(word.capitalize())
    
    title_case_string = ' '.join(title_case_words)
    
    return title_case_string

input_string = input("Enter a string to convert to title case: ")

title_case_output = title_case(input_string)

print("Title case output:")
print(title_case_output)


# In[39]:


#18. Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False

    count_str1 = {}
    count_str2 = {}
    
    for char in str1:
        if char in count_str1:
            count_str1[char] += 1
        else:
            count_str1[char] = 1
    
    for char in str2:
        if char in count_str2:
            count_str2[char] += 1
        else:
            count_str2[char] = 1

    if count_str1 == count_str2:
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


# In[40]:


#19. Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):

    translator = str.maketrans('', '', string.punctuation)

    cleaned_string = input_string.translate(translator)
    
    return cleaned_string

input_string = "Hello! How are you? I'm doing well, thank you!"
cleaned_string = remove_punctuation(input_string)

print("Original string:")
print(input_string)
print("\nString with punctuation removed:")
print(cleaned_string)


# In[41]:


#20. Write a python program that takes a list of numbers and returns their sum
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

num_list = [1, 2, 3, 4, 5]

result = calculate_sum(num_list)

print(f"The sum of the numbers {num_list} is: {result}")


# In[42]:


#21. Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2

occurrences = count_occurrences(my_list, element_to_count)

print(f"The element {element_to_count} appears {occurrences} times in the list.")


# In[43]:


#22.  Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    if not numbers:
        return None, None  # Return None for both min and max if the list is empty

    min_value = numbers[0]
    max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    return min_value, max_value

num_list = [3, 5, 1, 7, 9, 2, 8]

min_value, max_value = find_min_max(num_list)

print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")


# In[44]:


#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Welcome to the temperature converter!")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter '1' or '2'.")




# In[45]:


#24.  Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator."

print("Welcome to the simple calculator!")
print("Supported operations: +, -, *, /")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")


# In[46]:


#25.  Write a program that copies the contents of one text file to another
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: One of the files '{source_file}' or '{destination_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

source_file = "output.txt"
destination_file = "destination.txt"

copy_file(source_file, destination_file)


# In[47]:


#26.  Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

def check_prefix_suffix(input_string, prefix=None, suffix=None):
    starts_with_prefix = False
    ends_with_suffix = False
    
    if prefix:
        starts_with_prefix = input_string.startswith(prefix)
    
    if suffix:
        ends_with_suffix = input_string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

input_string = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"

starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix_to_check, suffix_to_check)

if starts_with_prefix:
    print(f"The string '{input_string}' starts with '{prefix_to_check}'.")
else:
    print(f"The string '{input_string}' does not start with '{prefix_to_check}'.")

if ends_with_suffix:
    print(f"The string '{input_string}' ends with '{suffix_to_check}'.")
else:
    print(f"The string '{input_string}' does not end with '{suffix_to_check}'.")


# In[48]:


#27.  Write a program in python that converts a string into a list of its characters.
def string_to_char_list(input_string):
    char_list = list(input_string)
    return char_list

input_string = "Hello, World!"

char_list = string_to_char_list(input_string)

print(f"The original string: {input_string}")
print(f"The list of characters: {char_list}")


# In[ ]:




