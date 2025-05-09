

special_char = ['@','#','$']
is_valid = True
while True: 
    password = str(input("Enter your password: "))
    if len(password) < 8: 
        print("Password must contain at least 8 characters")
        is_valid = False
    if not any(char in special_char for char in password ): 
        print("Password must contain at least one special character")
        is_valid = False
    if not any(char.isupper() for char in password ): 
        print("Password must contain at least one uppercase character")
        is_valid = False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase character")
        is_valid = False
    if not any(char.isdigit() for char in password): 
        print("Password must contain at least one digit")
        is_valid = False

    if is_valid: 
        print("Your password is strong! " )
        break
    else: 
        continue 

    