

print("-------------#TASK 1--------------", "\n") 
fruit_list = ["pineapple", "apple", "peach", "watermelon", "kiwi", "mango"]

print ("original list: ", fruit_list)

fruit_list.append("date")
print("After adding a fruit: ", fruit_list)
fruit_list.remove("apple")
print("After removing a fruit: ", fruit_list)
print("Reversed list: ", fruit_list[::-1])

print("-------------#TASK 2--------------", "\n") 

dict = {"name": "Fares", "age": "23", "city": "New York"}
dict["favorite color"] = "blue"
dict.update({"city": "Los Angeles"})
output1 = "Keys: "
output2 = "Values: "
for i in dict: 
    output1 += i + ", "
    output2 += dict[i] + ", "
print(output1)
print(output2)

print("-------------#TASK 3--------------", "\n") 

tuple = ("Interstellar", "Gangnam Style", "The best we could do")
print("Favorite Things: ", tuple)
try: 
    tuple[0] = "Inception"
except TypeError: 
    print("Oops! Tuples cannot be changed.")

print("Length of Tuple: ", len(tuple))