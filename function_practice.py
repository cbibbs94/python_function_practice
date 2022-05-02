def hello():
    print("Welcome to today's Python Practice repo")    
hello() 

def pack(item1, item2, item3):
    packing_list = [item1, item2, item3]
    return packing_list
print(pack("wallet", "shoes", "Shirts"))

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("We Don't any lunch yet")
    else: 
        for i in range(len(lunch_list)):
            if i == 0:
                print(f"First thing for lunch today is {lunch_list[0]}")
            else:
                print(f"Next thing im eating today is {lunch_list[i]}") 
eat_lunch(['CheeseBurger', 'french fries', 'Root Beer', 'Chocolate cake'])

