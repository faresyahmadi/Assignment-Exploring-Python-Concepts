

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
    input = int(input("Enter a word "))
    c = a + input
    print(c)
except TypeError: 
    print("TypeError occurred! Unsupported operand types." )