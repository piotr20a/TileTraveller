print("Welcome to car rentals!")

program = True


b_charge = 40
d_charge = 60
mile_charge = 0.25


while program:
    question = input("Would you like to continue (y/n)? ")
    if question == "y":
        customer_code = input("Customer code (b or d): ")
        if customer_code == "b":
            days = int(input("Number of days: "))
            odometer_start_int = int(input("Odometer reading at the start: "))
            odometer_end_int = int(input("Odometer reading at the end: "))
            miles_diven = odometer_end_int - odometer_start_int
            amount_due = round(days * b_charge + miles_diven * mile_charge, 1)
            print("Miles driven: ", miles_diven)
            print(f"Amount due: {amount_due}")
        elif customer_code == "d":
            days = int(input("Number of days: "))
            odometer_start_int = int(input("Odometer reading at the start: "))
            odometer_end_int = int(input("Odometer reading at the end: "))
            miles_diven = odometer_end_int - odometer_start_int
            if miles_diven > 100 * days:  #check if car has been driven more than 100 miles a day
                amount_due = round(days * d_charge + (mile_charge * (miles_diven - (100 * days))), 1)
                print(f"Miles driven: {miles_diven}")
                print(f"Amount due: {amount_due}")
                continue
            else:
                amount_due = round(days * d_charge + miles_diven * mile_charge, 1)
                print(f"Miles driven: {miles_diven}")
                print(f"Amount due: {amount_due}")
                continue
        else:               #if input is different than b or d then go back to input
            program = True
    elif question == "n": #turn off the program after choosing "n" option
        program = False
    else:
        print("Invalid input!") #if input is other than "y" or "n"