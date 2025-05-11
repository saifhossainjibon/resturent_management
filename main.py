from food_item import FoodItem
from menu import Menu
from users import Customer, Admin,Employee
from restaurant import Resturent
from orders import Order

mama_resturent=Resturent("mamar resturent")
def customer_menu():
    name = input("Enter your Name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your Address: ")
    customer=Customer(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {customer.name} !!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            customer.view_menu(mama_resturent)
        elif choice==2:
            item_name=input("Enter item Name: ")
            item_quantity=int(input("Enter Item Quantity: "))
            customer.add_to_cart(mama_resturent, item_name, item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else: 
            print("Invalid Input")



def admin_menu():
    name = input("Enter your Name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your Address: ")
    admin=Admin(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {admin.name} !!")
        print("1. Add new Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("5. Exit")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            item_name=input("Enter item Name: ")
            item_price=int(input("Enter Item Price: "))
            item_quantity=int(input("Enter Item Quantity: "))
            item =FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mama_resturent,item)

        elif choice==2:
            name=input("Enter your Name: ")
            phone=input("Enter your Phone: ")
            email=input("Enter your Email: ")
            address=input("Enter your address: ")
            age=input("Enter your Age: ")
            designation=input("Enter your designation: ")
            salary=input("Enter your salary: ")
            employee=Employee(name, phone, email, address,age,designation,salary)
            admin.add_empoloyee(mama_resturent,employee)
        
        elif choice==3:
            admin.view_employee(mama_resturent)

        elif choice==4:
            admin.view_menu(mama_resturent)

        elif choice==5:
            item_name=input("Enter Item name: ")
            admin.remove_item(mama_resturent,item_name)
        elif choice==6:
            break
        else:
            print("Invalid Input")

while True:
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice= int(input("Enter your Choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input")
    