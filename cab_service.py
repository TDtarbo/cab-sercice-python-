import os
import time


def main():
    while True:
        os.system("clear")
        print("""
        ==============================
        |         Welcome to         |
        |       Air Cab Service      |
        ==============================""")

        try:
            selection = int(input("""
        1-User Login
        2-Admin Login
        3-Register
        0-Exit
            
        Enter your selection : """))
        except ValueError:
            print("""
        ## Invalid input ##
            """)
            time.sleep(3)
            continue

        if selection == 1:
            user_login()
            break
        elif selection == 2:
            admin_login()
        elif selection == 3:
            register()
            break
        elif selection == 0:
            break
        else:
            print("""
        Invalid input
            """)
            time.sleep(3)
            continue


def user_login():
    db = open("user.txt", "r")
    os.system("clear")
    print("""
        ======== User Login =======""")
    login = str(input("""
        Enter User name : """))
    password = str(input("""
        Enter Password : """))

    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password == data[login]:
        os.system("clear")
        print("""
        ==== Success ====
        
        ## Welcome """ + login + """ ##""")
        time.sleep(2)
        user_dashboard()
    else:
        print("""
        ==== Login Failed! ====
            
        0-Main manu
        1-Retry""")

        try:
            response = int(input())
            if response == 0:
                main()
            elif response == 1:
                user_login()
            else:
                os.system("clear")
                print("""
        ==== Invalid input1 ====
            
        0-Main manu
        1-Retry""")
                invalid_input()

        except ValueError:
            os.system("clear")
            print("""
        ==== Invalid input2 ====
    
        0-Main manu
        1-Retry""")
            invalid_input()


def admin_login():
    db = open("user.txt", "r")
    os.system("clear")
    print("""
        ======== Admin Login =======""")
    login = str(input("""
        Enter User name : """))
    password = str(input("""
        Enter Password : """))

    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    try:
        if data[login]:
            try:
                if password == data[login]:
                    os.system("clear")
                    print("""
        ==== Success ====
            
        ## Welcome """ + login + """ ##""")
                    time.sleep(2)
                    admin_dashboard()
                else:
                    os.system("clear")
                    print("""
        ==== Login Failed! ====
            
        0-Main manu
        99-Retry""")
                    invalid_input()

            except ValueError:
                os.system("clear")
                print("""
        ==== Invalid input ====

        0-Main manu
        99-Retry""")
                invalid_input()
        else:
            os.system("clear")
            print("""
        ==== Invalid input ====

        0-Main manu
        99-Retry""")
            invalid_input()

    except KeyError:
        os.system("clear")
        print("""
        ==== Invalid input ====
    
        0-Main manu
        99-Retry""")
        invalid_input()


def invalid_input():
    response = int(input())
    if response == 0:
        main()
    elif response == 1:
        user_login()
    elif response == 99:
        admin_login()
    elif response == 98:
        user_dashboard()
    else:
        invalid_input()


def register():
    db = open("user.txt", "r")

    os.system("clear")
    print("""
    ==== Registration ====""")

    username = str(input("""
    Enter user name :"""))
    password = str(input("""
    Enter password :"""))

    if username in db:
        print("""
        User name taken""")

    else:
        db = open("user.txt", "a")
        db.write(username + ", " + password + "\n")
        os.system("clear")
        print("""
        ==== Success! ====
        
            1-User login
            2-Admin login
            0-Main manu""")
        try:
            response = int(input())
            if response == 0:
                main()
            elif response == 1:
                user_login()
            elif response == 2:
                admin_login()
            else:
                os.system("clear")
                print("""
            ==== Invalid input ====
            
            0-Main manu
            1-Retry""")
                invalid_input()

        except ValueError:
            os.system("clear")
            print("""
            ==== Invalid input ====
        
            0-Main manu
            1-Retry""")
            invalid_input()


def user_dashboard():
    while True:
        os.system("clear")
        print("""
        ==============================
        |          Dashboard         |
        ==============================""")

        try:
            selection = int(input("""
            1-Booking a cab
            2-Availability
            3-My Account
            0-Main manu

            Enter your selection : """))
        except ValueError:
            print("""
            ## Invalid input ##
            """)
            time.sleep(3)
            continue

        if selection == 1:
            booking()
            break
        elif selection == 2:
            cab_list()
        elif selection == 3:
            my_account()
            break
        elif selection == 0:
            main()
            break
        else:
            print("""
            Invalid input
            """)
            time.sleep(3)
            continue


def booking():
    os.system("clear")
    print("""
        ====== Enter Vehicle Type ======
     
             1-Car
             2-Van
             3-Three-wheels
             4-Truck
             5-Lorry
             0-Back
             """)
    selection = int(input("""
        Enter your selection : """))
    if selection == 1:
        car()
    elif selection == 2:
        van()
    elif selection == 3:
        threewheel()
    elif selection == 4:
        truck()
    elif selection == 5:
        lorry()
    elif selection == 0:
        user_dashboard()
    else:
        print("""
        Invalid input""")
        user_dashboard()


def car():
    os.system("clear")
    print("""
    ====== Hire a Car =====""")
    selection = int(input("""
    1-AC
    0-Non-AC
    Enter your selection :  """))
    if selection == 1:
        selection = int(input("""
    1- 3 passengers
    0- 4 passengers
    Enter your selection : """))
        if selection == 1 or selection == 0:
            print("""
    Your request submitted !""")
            time.sleep(2)
            user_dashboard()

    elif selection == 0:
        selection = int(input("""
    1- 3 passengers
    0- 4 passengers
            Enter your selection : """))
        if selection == 1 or selection == 0:
            print("""
    Your request submitted !""")
            time.sleep(2)
            user_dashboard()


def van():
    os.system("clear")
    print("""
       ====== Hire a Van =====""")
    selection = int(input("""
       1-AC
       0-Non-AC
       Enter your selection :  """))
    if selection == 1:
        selection = int(input("""
       1- 3 passengers
       0- 4 passengers
       Enter your selection : """))
        if selection == 1 or selection == 0:
            print("""
       Your request submitted !""")
            time.sleep(2)
            user_dashboard()

    elif selection == 0:
        selection = int(input("""
       1- 3 passengers
       0- 4 passengers
               Enter your selection : """))
        if selection == 1 or selection == 0:
            print("""
       Your request submitted !""")
            time.sleep(2)
            user_dashboard()


def threewheel():
    os.system("clear")
    print("""
       ====== Hire a Three-Wheeler =====""")

    selection = int(input("""
   1- 3 passengers
   Enter your selection : """))
    if selection == 1:
        print("""
   Your request submitted !""")
        time.sleep(2)
        user_dashboard()


def truck():
    os.system("clear")
    print("""
    ====== Hire a Truck =====""")
    selection = int(input("""
    1- 7 ft
    0- 12 ft
    Enter your selection : """))
    if selection == 1 or selection == 0:
        print("""
    Your request submitted !""")
        time.sleep(2)
        user_dashboard()


def lorry():
    os.system("clear")
    print("""
       ====== Hire a Lorry =====""")
    selection = int(input("""
       1- 2500 KG
       0- 3500 KG
       Enter your selection : """))
    if selection == 1 or selection == 0:
        print("""
       Your request submitted !""")
        time.sleep(2)
        user_dashboard()


def my_account():
    os.system("clear")
    print("""
    ========== My Account =========
    
    User name : bob
    Phone : 0123456789
    Email : example@ex.com""")
    response = int(input("""
    0-Back
    """))
    if response == 0:
        user_dashboard()
    else:
        invalid_input()


def admin_dashboard():
    os.system("clear")
    print("""
    ==============================
    |        Admin Dashboard     |
    ==============================""")

    selection1 = int(input("""
    1-Car List
    2-User list
    3-Add a cab
    4-Remove a cab
    5-Remove user
    0-Main menu

    Enter your selection : """))

    if selection1 == 1:
        cab_list()
    elif selection1 == 2:
        user_list()
    elif selection1 == 3:
        add_cab()
    elif selection1 == 4:
        del_cab()
    elif selection1 == 5:
        del_user()
    elif selection1 == 0:
        main()

    else:
        print("""
        Invalid input
        """)
        time.sleep(3)
        admin_dashboard()


def add_cab():
    os.system("clear")
    print("""
    ========== Add a Cab =========
    """)
    with open("cabs.txt", "a") as text:
        cab_type = input("""
        Type: """)
        model = input("""
        Brand: """)
        color = input("""
        Color: """)
        year = input("""
        Year: """)
        text.write("""%s , %s , %s , %s \n""" % (cab_type, model, color, year))

        response = int(input("""
            1-Add another
            0-Back
            """))
        if response == 0:
            admin_dashboard()
        elif response == 1:
            add_cab()
        else:
            invalid_input()


def cab_list():
    os.system("clear")
    print("""
    ========== Available Cab List =========
    """)
    with open("cabs.txt", mode="r") as text_file:
        for iline, line in enumerate(text_file, 1):
            print(iline, line)
    response = int(input("""
    0-Back
    """))
    if response == 0:
        admin_dashboard()
    else:
        invalid_input()


def user_list():
    os.system("clear")

    with open("user.txt", mode="r") as text_file:
        for iline, line in enumerate(text_file, 1):
            print(iline, line)
    response = int(input("""
    0-Back
    """))
    if response == 0:
        admin_dashboard()
    else:
        invalid_input()


def del_cab():
    os.system("clear")
    delete_value = input("""
    ====== Remove a Cab =======
    
    Enter car model: """)

    with open("cabs.txt", "r") as f:
        file = f.readlines()
    with open("cabs.txt", "w") as f:
        for line in file:
            words = line.strip("\n").lower().split(' ')
            if delete_value.lower() not in words:
                f.write(line)
    print("""Successfully removed""")
    time.sleep(2)
    admin_dashboard()


def del_user():
    os.system("clear")
    print("""
    ===== Delete user ======""")
    delete_value = input("""
    Enter user name: """)

    with open("user.txt", "r") as f:
        file = f.readlines()
    with open("user.txt", "w") as f:
        for line in file:
            words = line.strip("\n").lower().split(' ')
            if delete_value.lower() not in words:
                f.write(line)
    print("""
    User removed successfully""")
    time.sleep(2)
    admin_dashboard()


main()
