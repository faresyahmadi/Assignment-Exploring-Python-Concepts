#Task 1 
string = "Python is amazing!"

print(string[0:6])
print(string[10:18])
print(string[::-1])

#Task 2 
s = " hello, python world! "
print(s.strip())
print(s.title())
print(s.replace("world", "universe"))
print(s.upper())

#Task 3 

user_palind  = str(input("Enter your word to check for palindrome: "))
if user_palind == user_palind[::-1]: \
    print("Yes", user_palind, "is a palindrome! ")
