database = {}
password = "qwert"
BILL_FILE = "Activahouse_bill.txt"


def get_int(message):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def active(rent):

    def tern_and_condition():
        print("Term and Condition")
        print(""" 
                    1.Aadhaar Card is Mandatory.
                    2.Driving Licence is Mandatory.
                    3.One Activa for One Day: 500/-
                    """)

    def bill(name, phone, aadhar, address, licenses, days, no_rent_activa, p):
        bill_text = f'''
================================================================
                    * ACTIVA RENT BILL *
________________________________________________________________
NAME               :-  {name}
ADDRESS            :-  {address}
AADHAR NUMBER      :-  {aadhar}
LICENSES           :-  {licenses}
PHONE              :-  {phone}
DAYS               :-  {days}
________________________________________________________________
QUANTITY           :-  {no_rent_activa}
________________________________________________________________
PRICE              :-  {p}
________________________________________________________________
                      * THANK YOU *
================================================================
'''
        print(bill_text)
        with open(BILL_FILE, "a") as bills:
            bills.write(bill_text)

    def rent_activa():
        nonlocal rent
        tern_and_condition()

        a = input("Y/N : ")
        if a == "y" or a == "Y":
            print("Welcome to Rent Activa ")
            print("No of Activa Available: ", rent)
            name = input("Enter Your Name :- ")
            phone = input("Enter Your Phone Number :- ")
            address = input("Enter Your Address :- ")
            aadhar = input("Enter Your Aadhar Number :- ")

            if aadhar in database and database[aadhar]["no_rent_activa"] > 0:
                print("You already have a rented Activa. Please return it first.")
                return

            licenses = input("Enter Your License :- ")
            days = get_int("Enter Your days :- ")
            price = 500
            no_rent_activa = get_int("Enter Your Number of Activa in Rent :- ")

            if no_rent_activa <= rent:
                rent -= no_rent_activa
                database[aadhar] = {
                    "name": name,
                    "phone": phone,
                    "address": address,
                    "licenses": licenses,
                    "days": days,
                    "no_rent_activa": no_rent_activa
                }

                p = price * no_rent_activa * days
                bill(name, phone, aadhar, address, licenses, days, no_rent_activa, p)
                print("Booked ")
            else:
                print(f"Only {rent} Activa available.")
        else:
            print("Please give permission: Y or N")

        print("No of Activa Available: ", rent)

    def activa_return():
        nonlocal rent
        print("Welcome to the Return Activa ")
        aadhar = input("Enter Aadhar Number :- ")
        if aadhar in database and database[aadhar]["no_rent_activa"] > 0:
            booked = database[aadhar]["no_rent_activa"]
            retur = get_int("Enter Return Activa : ")
            if retur <= booked:
                rent += retur
                database[aadhar]["no_rent_activa"] = booked - retur
                with open(BILL_FILE, "a") as bills:
                    bills.write(
                        f"\n[RETURN] Aadhar: {aadhar}, "
                        f"Name: {database[aadhar]['name']}, "
                        f"Returned: {retur}, "
                        f"Still rented: {database[aadhar]['no_rent_activa']}\n"
                    )
                print("Successfully Return ")
            else:
                print(f"You are booked only {booked}")
        else:
            print("Invalid Aadhar Number or no Activa rented!")

    def owner_part():
        print("Welcome to Owner Access ")
        entered = input("Enter your Password : ")
        if entered == password:
            if database:
                for aadhar, details in database.items():
                    print(aadhar, "->", details)
            else:
                print("No records yet.")
            print("No of Activa Available: ", rent)
        else:
            print("Wrong password ")

    print("Welcome To Activa Rental House.")
    while True:
        var = input("""
        1. Rent 
        2. Return 
        3. Owner
        4. Exit ____""")
        if var == "1":
            rent_activa()
        elif var == "2":
            activa_return()
        elif var == "3":
            owner_part()
        elif var == "4":
            print("Thank you! Visit again.")
            break
        else:
            print(" Please Enter Correct Option no")


active(20)
