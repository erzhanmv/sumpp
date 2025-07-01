#task1
multiply_list = [3, 8, 9]
sum = 1

for i in multiply_list:
    sum *= i

print(sum)
#task2
text = input()
upper_letters = ""
lower_letters = ""

for i in text:
    if i.isupper():
        upper_letters += i
    elif i.islower():
        lower_letters += i

print(len(upper_letters))
print(len(lower_letters))
#task3
text = input("Enter a string: ")
reversed_text = ''.join(reversed(text))

if text == reversed_text:
    print("This string is palindrome")
else:
    print("This string is not palindrome")

#task4
import time
import math

number = float(input())
delay_ms = int(input())

time.sleep(delay_ms / 1000)
result = math.sqrt(number)

print(f"Square root of {int(number)} after {delay_ms} miliseconds is {result}")