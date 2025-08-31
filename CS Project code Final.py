import pickle as pk
import csv
from Admin_Mode import AdminMode
def train_data():
    f=open('Train_data.dat','rb+')
    try:
        while True:
            d=pk.load(f)
    except:
        pass
    f.close()
def mainmenu():
    print('------------------------------------ WELCOME TO INDIAN RAILWAY SERVICE APP ---------------------------------------------')
    print()
    print("1-Find the train using PNR Code.")
    print("2-Find trains available between 2 stops.")
    print("3-Find time of travel and distance of travel for a given train between 2 stops.")
    print("4-Food Delivery")
    print("5-Admin Mode")
    print("6-Exit")
    print()
def Exit():
    while True:
        option=input("Enter E to go back to main menu: ")
        if option=='E' or option=='e':
            print()
            return mainmenu()
        else:
            print('Error, Did you mean to write "E"?')
def traindetails():
    while True:
       try: 
        no=int(input("Enter the train code: "))
        n=0
        for i in d:
            if i==no:
                print("The details of the train are given below: ")
                print('Name: ',str(d[i][0]))
                print('Stops: ',tuple(d[i][1]))
                n+=1
                print()
                return
        if n==0:
            print("Sorry, the train cannot be found. Try Again.")
       except:
           print('An Error has occured, please try again.')
           traindetails()
def traintimings():
    while True:
      try:
        trainno=int(input('Train no.: '))
        initial=input('initial destination: ')
        final=input('final destination: ')
        keys=list(d[trainno][1].keys())

        if initial not in keys:
            print("The given departure station is not in the train's stop list. Check for case.")
        
        elif final not in keys:
            print("The given arrival station is not in the train's stop list. Check for case.")
        else:
            tdept=d[trainno][1][initial]
            tarrsched=d[trainno][1][final]
            i1=keys.index(initial)
            i2=keys.index(final)    
            speed=84
            harrsched=int(tarrsched[0:2])
            hdepsched=int(tdept[0:2])
            marrsched=int(tarrsched[3:])
            mdepsched=int(tdept[3:])
            ttravel=(harrsched+(marrsched/60))-(hdepsched+(mdepsched/60))
            ttotal=ttravel
            htotal=int(ttotal)
            mintotal=int((ttotal-htotal)*60)
            distance=speed*ttotal
            if mintotal<10:
               print("Estimated time of travel: ", htotal, "h0", mintotal, ".", sep='')
            else:
               print("Estimated time of travel: ", htotal, "h", mintotal, ".", sep='')
               
            print("Distance: ",distance,'km',sep='')
            print("Departure Time from ",initial,': ',hdepsched,'h',mdepsched,sep='')
            print("Arrival Time at ",final,': ',harrsched,'h',marrsched,sep='')
            print()
            return
      except:
          print('An Error has occured, try again.')
          traintimings()
def admin_mode():
    from Admin_Mode import entryAdmin,AdminMode
    
    entryAdmin()


#-----Food Delivery Service-----          

menu = {
    "Veg Thali": 120,
    "Non-Veg Thali": 150,
    "Biryani": 100,
    "Sandwich": 60,
    "Tea": 20,
    "Coffee": 30,
    "Soft Drink": 40
}


orders = []


def place_order():
    print("\n--- Place Your Order ---")
    train = input("Enter Train No: ").strip()
    coach = input("Enter Coach: ").strip()
    seat = input("Enter Seat No: ").strip()
    print("\nMenu:")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item} - ₹{price}")

    selected_items = []
    while True:
        choice = input("Enter item number to add (or 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(menu):
            print("Invalid choice, try again.")
            continue
        item_name = list(menu.keys())[int(choice)-1]
        selected_items.append(item_name)
        print(f"Added: {item_name}")

    if not selected_items:
        print("No items selected. Order cancelled.")
        return

    total = sum(menu[item] for item in selected_items)
    order = {
        "Train": train,
        "Coach": coach,
        "Seat": seat,
        "Items": selected_items,
        "Total": total
    }
    orders.append(order)
    print(f"\nOrder placed! Total: ₹{total}")


def view_orders():
    if not orders:
        print("\nNo orders placed yet.")
        return
    print("\n--- All Orders ---")
    for i, order in enumerate(orders, 1):
        print(f"\nOrder {i}:")
        print(f" Train: {order['Train']}")
        print(f" Coach: {order['Coach']}")
        print(f" Seat: {order['Seat']}")
        print(f" Items: {', '.join(order['Items'])}")
        print(f" Total: ₹{order['Total']}")
        print("------------------------")


def main_area_to_order():
    while True:
        print("\n1. Place Order")
        print("2. View All Orders")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            place_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
mainmenu()

while True:
    a=int(input("Enter option: "))
    if a==1:
        
        traindetails()
        x=input('Do you want to exit? Press Y to exit or any key to cancel: ')
        if x=='Y' or x=='y':
            Exit()
        else:
            traindetails()
        
        
    elif a==2:
        st1=input("Enter the starting station: ")
        st2=input("Enter the destination: ")
        b=0
        for i in d:
            if st1 in d[i][1] and st2 in d[i][1]:
                print("The train available is: ",i,'-',str(d[i][0]))
                b+=1
        if b==0:
            print("Sorry, there are no trains available for these stops.")
       
        Exit()
    elif a==3:
        traintimings()
        x=input('Do you want to exit? Press Y to exit or press any key to cancel: ')
        if x=='Y' or x=='y':
            Exit()
        else:
            traintimings()
    elif a==4:
        main_area_to_order()
        x=input('Do you want to exit? Press Y to exit or press any key to cancel: ')
        if x.lower()=='y':
            Exit()
        else:
            main_area_to_order()
        
    elif a==5:
        admin_mode()
        x=input('Do you want to exit? Press Y to exit or press any key to cancel: ')
        if x=='Y' or x=='y':
            Exit()
        else:
            admin_mode()
        
        

    elif a==6:
        print('Thank you for using our app.')
        break
    else:
        print('The given option is not a valid option. Please select an option between 1 and 5.')
        
        mainmenu()
        
