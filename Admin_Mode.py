import pickle as pk
import csv
def train_data():
    f=open('Train_data.dat','rb+')
    try:
        while True:
            global d
            d=pk.load(f)
            
    except:
        pass
    f.close()
def expcsv():
    try:
        with open("Train_data.dat", "rb") as f:
            trains = {}
            while True:
                try:
                    d = pk.load(f)
                    trains.update(d)  
                except EOFError:
                    break

        with open("Train_data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Train Code", "Train Name", "Stops"])  
            for code, details in trains.items():
                name = details[0]
                stops = ", ".join(details[1])
                writer.writerow([code, name, stops])

        print("\n Train data successfully exported to Train_data.csv\n")

    except FileNotFoundError:
        print("\n Train_data.dat not found.\n")
    except Exception as e:
        print("\n Error while exporting:", e, "\n")

def AdminMode():
        while True:
                print("ADMIN MODE")
                print("1-Add a new train")
                print("2-Delete a train")
                print("3-Add Delay")
                print('4-Add Seats available: ')
                print('5-Export All Train Information to CSV')
                print('6-Exit')
                e=int(input("Enter option: "))
                if e==1:
                  n=int(input("Enter number of trains to be added: "))
                  for c in range(n):
                      co=int(input("Enter train code: "))
                      t=()
                      L1=[]
                      L2=[]
                      st=input("Enter name of train: ")
                      L1.append(st)
                      num=int(input("Enter number of stops: "))
                      for i in range(num):
                          st=input("Enter stop: ")
                          L2.append(st)
                      t+=(L1,)
                      t+=(L2,)
                      d[co]=t
                      print('Added Train')
                      print(d[co])
                elif e==2:
                    num=int(input("Enter number of trains to be deleted: "))
                    for k in range(num):
                        tco=int(input("Enter train code to be deleted: "))
                        if tco in d:
                           del d[tco]
                           print('Deleted: ',tco)
                           print()
                elif e==3:
                    train=int(input('Enter Train Number: '))
                    station=input('Station name: ')
                    for i in d[train]:
                        if type(i)==dict:
                            for j in i:
                                if j==station:
                                    global initial_time
                                    initial_time=i[j]
                    new_time=input('New estimated time of arrival as AhB: ')
                    try:
                        if new_time == initial_time:
                           print('Status: On time')
                           print('Time is',initial_time)
                        else:
                           h=int(new_time[0:2])
                           new_min=int(new_time[3:])
                           old_min=int(initial_time[3:])
                           if new_min > old_min:
                             delay=new_min-old_min
                             print('The train is at delay of',delay,'minutes.')
                           else:
                             p2=new_min+60
                             delay=p2-old_min
                             print('The train is at delay of',delay,'minutes.')
                           for iteration in d[train]:
                             if type(iteration)==dict:
                               for j in iteration:
                                 if j==station:
                                    iteration[j]=new_time
                        print(d[train])
                        print()
                        return
                    except:
                        print('There has been an error. Please Try again.')
                        print()
                        from CS_project_Code_Final import admin_mode
                        admin_mode()
                
                elif e==4:
                    train=int(input('Enter Train number: '))
                    if train in d:
                        
                        train_name, stations = d[train]
                        sleep=int(input('Enter availability of sleeper seats: '))
                        AC3=int(input('Enter availability of AC 3-Tier seats: '))
                        AC2=int(input('Enter availability of AC 2-Tier seats: '))
                        ACC=int(input('Enter availability of AC Chair Car Seats: '))
                        d[train] = (train_name, stations,{"Sleeper": sleep, "AC 3-Tier": AC3, "AC 2-Tier": AC2, "AC Chair Car": ACC})
                    else:
                         print('Train not found, please try again.')
                         option5menu()
                elif e==5:
                    expcsv()
                elif e==6:
                    return
                    
                       
                        
train_data()

def entryAdmin():
    print("Admin Mode:")
    password=input('Password: ')
    if password=='rhnj0825**':
        AdminMode()
    else:
        print('Incorrect password')
        entryAdmin()


