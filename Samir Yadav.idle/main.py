from operations import * # Import all functions from the operations module

# Import the datetime module to work with dates and times
import datetime
#Getting current date and time
x = datetime.datetime.now()

#print welcome message
print("+"*100)
print("\t\t\t Hello and Welcome to Techno-Nepal Land Management System")
print("+"*100)


def main():
    while True:
        # Display the current land data
        display_land_data()
        
        # Display menu options to the user
        print("\nEnter '1' to rent a land")
        print("Enter '2' to return the land")
        print("Enter '3' to exit")

        # Get user input for the menu choice
        choice = input("Enter the numbers to rent, return or exit: ")

        # Handle user choice for renting land
        if choice == "1":
            rent_land()
            loop_()

        # Handle user choice for returning land
        elif choice == "2":
            return_land()
            loop_return()

         # Handle user choice for exiting the program
        elif choice == "3":
            exit()
            break
        else:
            print("-"*80)
            print("Invalid choice, Please enter the options from above.")
            print("-"*80)

# Check if the script is being run directly and not imported as a module
if __name__ == "__main__":
    main()  # Call the main function to start the program
