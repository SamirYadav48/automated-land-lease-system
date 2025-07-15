from read import read_info # Import the read_info function from the read module
from write import update_availability, generate_rent_invoice , generate_return_invoice


def display_land_data():
    # Read land data from the file and display it in a formatted table
    lands = read_info("info.txt")
    print("\nLand Information:")
    print("{:<15} {:<15} {:<10} {:<10} {:<15} {:<15}".format("Kitta Number", "City/District", "Direction", "Area (anna)", "Price (NPR)", "Availability"))
    for land in lands:
        kitta_number = land.get("Kitta Number", "N/A")
        city_district = land.get("City/District", "N/A")
        direction = land.get("Direction", "N/A")
        area = land.get("Area (anna)", "N/A")
        price = land.get("Price (NPR)", "N/A")
        availability = land.get("Availability", "N/A")
        print("{:<15} {:<15} {:<10} {:<10} {:<15} {:<15}".format(kitta_number, city_district, direction, area, price, availability))

def get_land_by_kitta_number(file_name, kitta_number):
    # Retrieves land information by Kitta Number from the specified file.
    lands= read_info(file_name)
    for land in lands:
        if int(land.get("Kitta Number", "-1"))== kitta_number:
            return land
    return None


def rent_land():
    # Handles the process of renting land, including user input and updating records.
    display_land_data()
    while True:
        try:
            kitta_number = int(input("\nEnter the Kitta Number of the land you want to rent: "))
            if 201 <= kitta_number <= 215:
                break  # Break out of the loop if the input is within the valid range
            else:
                print("-"*80)
                print("\t\tError: Please enter a number between 201 and 215.")
                print("-"*80)
        except ValueError:
            print("-"*80)
            print("\t\tError: Invalid input. Please enter a valid integer.")
            print("-"*80)
    while True:
        try:
            rented_duration = int(input("Enter the duration of land you want to rent (in months): "))
            if rented_duration>3:
                break # break out of the loop if duration is valid
            else:
                print("\t\tError: Duration must be above 3 months")
        except Exception:
            print("\t\tPlease enter the duration in months only!!!")
        
    customer_name = input("Enter your name: ")
    land = get_land_by_kitta_number("info.txt", kitta_number)
    if land and land.get("Availability", "N/A") == "Available":
        rented_lands = [land]
        generate_rent_invoice(customer_name, rented_lands, rented_duration)
        update_availability("info.txt", kitta_number, "Not Available")
        print("-"*100)
        print(f"\t\tLand with Kitta Number {kitta_number} has been rented successfully for {rented_duration} months.")
        print("-"*100)
    elif not land:
        print("-"*100)
        print("\t\tLand with the provided Kitta Number does not exist.")
        print("-"*100)
    else:
        print("-"*100)
        print("\t\tThe land is currently not available for renting.")
        print("-"*100)
    


def loop_():
    # Prompts the user to rent another land or view rental details.
    print("Do you want to rent another land?")
    Continue = input("Enter 'y' to continue or 'n' for rental details: ")
    if Continue == "y":
        rent_land()
    elif Continue == "n":
        return
    else:
        print("+"*80)
        print("\t\t\t Please provide value in 'y' or 'n' only!!")
        print("+"*80)
        return loop_()



def return_land( ):
    # Handles the process of returning rented land, including user input and updating records.
    display_land_data()
    while True:
        try:
            kitta_number = int(input("\nEnter the Kitta Number of the land you want to return: "))
            if 201 <= kitta_number <= 215:
                break  # Break out of the loop if the input is within the valid range
            else:
                print("+"*100)
                print("\t\tError: Please enter the kitta number correctly which you have rented.")
                print("+"*100)
        except ValueError:
            print("-"*100)
            print("\t\tError: Invalid input. Please enter a valid integer.")
            print("-"*100)

    customer_name = input("Enter your name: ")
    while True:
        try:
            rented_duration = int(input("Enter the duration of land you had taken for renting: "))
            if rented_duration>3:
                break # break out of the loop if duration is valid
            else:
                print("*"*100)
                print("\t\tError: Duration must be above 3 months")
                print("*"*100)
        except Exception:
            print("*"*100)
            print("\t\tPlease enter the duration in months only!!!")
            print("*"*100)

   
    while True:
        try:
            return_duration = int(input("Enter the duration of the land you have returned: "))
            if return_duration >3:
                break
            else:
                print("*"*100)
                print("\t\tError: Duration must be above 3 months")
                print("*"*100)  
        except Exception:
            print("-"*100)
            print("\t\tPlease enter the duration in months only!!!")
            print("-"*100)
    land = get_land_by_kitta_number("info.txt", kitta_number)
    if land and land.get("Availability", "N/A") == "Not Available":
        fine_amount_per_month = float(land.get("Price (NPR)","0"))*0.1
        if return_duration > rented_duration:
            months_late = return_duration - rented_duration
            total_fine = fine_amount_per_month * months_late
            print("*"*100)
            print(f"\t\tThe land was returned late by {months_late} months.")
            print(f"\t\tSo, fine of NPR {total_fine} was applied.")
            print("*"*100)
        else:
            total_fine = 0
            print("The land was returned on time or early. So, no fine was applied.")
        returned_lands = [land]
        generate_return_invoice(customer_name, returned_lands, fine_amount=0)
        update_availability("info.txt", kitta_number, "Available")
        print(f"Land with Kitta Number {kitta_number} has been returned successfully.")
    elif not land:
        print("-"*80)
        print("\t\tLand with the provided Kitta Number does not exist.")
        print("-"*80)
    else:
        print("-"*100)
        print("\t\tThe land is not currently rented.")
        print("-"*100)


    
def loop_return():
    # Prompts the user to return another land or exit the return process.
    print("Do you want to return another land?")
    continue_ = input("Enter 'y' or  'n' to continue: ")
    if continue_ =="y":
        return return_land()
    elif continue_ == "n":
        return
    else:
        print("+"*80)
        print("\t\t\t Please provide value in 'y' or 'n' only!!")
        print("+"*80)
        return loop_return()

def exit():
    # Displays a thank you message and exits the program.
    print()
    print("+" * 80)
    print("\t \t Thank you for using our Land management system")
    print("+" * 80)
    return exit







