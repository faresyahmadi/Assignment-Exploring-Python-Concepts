

inventory = {"apple": (10,2.5), "banana": (10,2.1)}

def inventory_print(): 
    for key in inventory: 
        print("Item: ",key, ", Quantity: ", inventory[key][0], ", Price: $", inventory[key][1])

def price():
    total = 0  
    for key in inventory: 
        total += inventory[key][0]*inventory[key][1]
    print("Total value of inventory: $",total)

print("Welcome to the Inventory Manager!")
print("Current inventory: ")
inventory_print()
print("Adding a new item to the inventory: Mango")
inventory["mango"] = (15,3.0)
print("Updating inventory! updatibg banana and deleting apple")
inventory.update({"banana": (18,2.0)})
inventory.pop("apple")
print("Updated Inventory! ")
inventory_print()
price()