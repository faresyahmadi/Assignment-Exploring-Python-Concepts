

#This is the recursion function for the factorial
def factorial(n): 
    if n == 1: 
        return 1 
    else:   
        return n * factorial(n-1)

#This is the recursion function for finding the nth number in the fibonnaci sequence
def fibonnaci(n): 
    if n ==0: 
        return 0
    elif n ==1: 
        return 1 
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
    
#This is the function that draws a recursive fractal pattern
def star_pattern(n):
    if n == 0:
        return
    print('*' * n)
    star_pattern(n - 1)
    print('*' * n)

##DISREGARD: 
##def valid_input(input, message, limit): 
    ##while True: 
        ##input = int(input(message))
        ##if input>=limit: 
        #once the condition is satisfied break the loop and continue to the print stmt 
            ##break


#This is where the menu app starts

#while loop to make sure the user inputs a number that is on the menu (1-4). In case the user doesn't the code will keep asking for a valid input
while True:  
    print("Welcome to the Recursive Artistry Program!")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Draw a Recursive Fractal")
    print("4. Exit")
    user_input = int(input(" Choose an option: "))

    #if the input is 4 then exit
    if user_input == 4: 
        break


    #if the input is 1 then we ask the user for a number to calculate its factorial
    elif user_input == 1: 
        #this loop is to make sure the user inputs a valid number for factorial function which is any number equal or larger than 1
        #IDEA: SINCE I WILL BE USING A SIMILAR CODE FOR INPUT VALIDATION WE CAN CREATE A FUNCTION WITH ARGUMENTS INPUT, MESSAGE FOR THE INPUT DISPLAY , AND LIMIT TO CONTROL WHEN TO BREAK
        #LOOK AT def valid_input func defined right below star_pattern
        while True: 
            n = int(input("Enter a number to find its factorial: "))
            if n>=1: 
                #once the condition is satisfied break the loop and continue to the print stmt 
                break
        print("The factorial of ", n, " is ", factorial(n))
        break

    elif user_input == 2:
        #this loop is to make sure the user inputs a valid number for fibonnaci function which is any number equal or larger than 0
        while True: 
            fib = int(input("Enter a number to find its index in the fibonacci sequence: "))
            if fib >= 0: 
                #once the condition is satisfied break the loop and continue to the print stmt 
                break
        print("The ", fib,"th fibonnaci number is ",fibonnaci(fib))
        break

    #if the input is 3 then initiate the part of drawing patterns using the star function 
    elif user_input == 3: 
        while True: 
            pattern = int(input("Enter a number to create a star pattern: "))
            if pattern > 0: 
                break
        star_pattern(pattern) 
        break

    #this is to make sure that in case the user inputs anything other than 1-4 we asks him for another input until it's valid. 
    else: 
        continue 

