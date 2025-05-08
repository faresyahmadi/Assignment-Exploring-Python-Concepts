
#TASK 1 
num = int(input("Enter your number: "))

while num > 0:
    print(num)
    num -= 1 

print("Blast off!") 

#Task 2 

mult_num = num = int(input("Enter your number: "))
for i in range (1,11): 
    print(mult_num, "*", i, "=", mult_num*i)

#Task 3 

factorial_num = num = int(input("Enter your number: "))
for i in range(1,factorial_num):
    factorial_num = factorial_num*i 
print(factorial_num)