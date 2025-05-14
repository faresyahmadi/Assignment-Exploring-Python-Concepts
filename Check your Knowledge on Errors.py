

print("------------- Task1 ---------------------")

try:
    user_input = int(input("Enter a number: "))
    print(100/user_input)
except ZeroDivisionError: 
    print("You cannot divide by zero")
except ValueError: 
    print("You have to enter an int")



print("------------- Task2 ---------------------")
list = [1,2,3]
print(list)
index_input = int(input("Enter an index number: "))
try:
    a = list[index_input]
    print(a)
except IndexError: 
    print("List index out of range. ")

try:
    dict = {"name": "Fares", "age": 23}
    print(dict)
    key_input = str(input("Enter a key for the dict: "))
    b = dict[key_input]
    print(b)
except KeyError: 
    print("KeyError occurred! Key not found in the dictionary.")

try:
    a =  "hi"
    word = input("Enter anything ")
    if word.isdigit(): 
        word = int(word)
    c = a + word
    print(c)
except TypeError: 
    print("TypeError occurred! Unsupported operand types." )


print("------------- Task3 ---------------------")
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
try: 
    div = input_1/input_2 
except ZeroDivisionError: 
    print("Cannot divide by zero")
else: 
    print(div)
finally: 
    print("thank you for using our div calculator")
