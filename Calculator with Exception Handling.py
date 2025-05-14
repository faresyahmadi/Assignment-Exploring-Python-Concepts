import logging #to be able to use logging in python

logging.basicConfig(
    filename= r'C:\Users\didif\OneDrive\Desktop\school\Summer2025\exceptions_log.txt',  # the name of the log file 
    level=logging.ERROR,  # capture errors
    format='%(asctime)s - %(levelname)s - %(message)s',  #customizing logging format
)

#addition func 
def addition(): 

    try: 
        a = int(input("Enter the first number "))
        b = int(input("Enter the second number "))
    except ValueError: #making sure the user inputs a number if not then print the error message and log it to the file
        print("Please enter a valid number ")
        logging.exception("Please enter a valid number/// error occured in addition")
    else: #if everything is valid go ahead and print the output
        print("The result of ", a , " + ", b, " is ", a+b)

def substraction(): 

    try: 
        a = int(input("Enter the first number "))
        b = int(input("Enter the second number "))
    except ValueError: #making sure the user inputs a number if not then print the error message and log it to the file
        print("Please enter a valid number ")
        logging.exception("Please enter a valid number/// error occured in substraction")
    else:#if everything is valid go ahead and print the output
        print("The result of ", a , " - ", b, " is ", a-b)   

def multiplication(): 
  
    try: 
        a = int(input("Enter the first number "))
        b = int(input("Enter the second number "))
    except ValueError: #making sure the user inputs a number if not then print the error message and log it to the file
        print("Please enter a valid number ")
        logging.exception("Please enter a valid number/// error occured in multiplication")
    else:#if everything is valid go ahead and print the output
        print("The result of ", a , " * ", b, " is ", a*b)
    
def division(): 
    try:
        a = int(input("Enter the first number "))
        b = int(input("Enter the second number "))
        print("The result of ", a , " / ", b, " is ", a/b) #if everything is valid go ahead and print the output
    except ZeroDivisionError: #making sure the user inputs a number if not then print the error message and log it to the file
        print("You can't divide by zero ")
        logging.exception("Cannot divide by zero/// error occured in div")
    except ValueError: #making sure the user inputs a number if not then print the error message and log it to the file
        print("Please enter a valid number ")
        logging.exception("Please enter a valid number/// error occured in Division")


#the calculator app starts here
print("Welcome to the Error-Free Calculator!")
print("Choose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit")
while True: #keep prompting the user until they decide to exit(5)

    try: 
        user_input = int(input(" Choose an option: \n"))
    except ValueError: #if the user doesnt enter a valid number log and print this message
        print("Please enter a number\n")
        logging.exception("Please enter a number/// error occured in main menu")
    else: #once the user has entered a valid choice we check which choice and call the correct function declared above
        if user_input == 1: 
            print("You chose Addition\n")
            addition()
        elif user_input == 2: 
            print("You chose Substraction\n")
            substraction()
        elif user_input == 3: 
            print("You chose Multiplication\n")
            multiplication()
        elif user_input == 4: 
            print("You chose Division\n")
            division()
        elif user_input == 5: #only exit out of the app and log when the session ended
            logging.exception("Session Ended")
            break


        