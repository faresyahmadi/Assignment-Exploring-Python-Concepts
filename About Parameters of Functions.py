
print("------------- Task1 ---------------------")

def greet_user(name): 
    return "Hello, " +  name + "! Welcome Aboard." 


def add_numbers(a,b):
    return "The sum of " + str(a) + " and " + str(b) + " is " + str((a +b))

print(greet_user("Fares"), add_numbers(20,5))



print("------------- Task2 ---------------------")

def describe_pet(pet_name, animal_type): 
    return "I have a " + animal_type + " named " + pet_name
print(describe_pet("Nemo", "Fish"))



print("------------- Task3 ---------------------")

def make_sandwich(*arg): 
    return "Making a sandwich with the following ingredients:" + str(arg)
print(make_sandwich("Lettuce", "Onion", "Turkey"))


print("------------- Task4 ---------------------")

def factorial(n): 
    if n == 1: 
        return 1 
    else:   
        return n * factorial(n-1)
    


def fibonnaci(n): 
    if n ==0: 
        return 0
    elif n ==1: 
        return 1 
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

print("Factorial of 5 is ", factorial(5), ". The 6th Fibonacci number is ", fibonnaci(6))