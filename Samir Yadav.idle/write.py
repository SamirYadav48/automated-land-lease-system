import datetime # Import the datetime module to work with dates and times

def update_availability(file_name, kitta_number, status):
    # Initialize an empty list to store the updated lines of the file
    lines = []
    # Open the file in read mode
    with open(file_name, 'r') as file:
        headers = file.readline().strip().split(', ')
        lines.append(', '.join(headers) + '\n')
        # Iterate through each line in the file
        for line in file:
            land_data = line.strip().split(', ')
            # Check if the current land's kitta number matches the provided kitta number
            if int(land_data[0]) == kitta_number:
                land_data[-1] = status
                # Recreate the line with updated status
                line = ', '.join(land_data) + '\n'
            lines.append(line)
    # Open the file in write mode to overwrite with updated content
    with open(file_name, 'w') as file:
        file.writelines(lines)# Write all lines back to the file



def generate_rent_invoice(customer_name, rented_lands, rented_duration):
    # Calculate the total amount based on land prices and rented duration
    total_amount = sum(float(land.get("Price (NPR)", "0")) for land in rented_lands) * rented_duration
    invoice_name = f"{customer_name}_rent_invoice_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    
    with open(invoice_name, 'w') as file:
        file.write("Rent Invoice\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Date and Time of Rent: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("Rented Lands:\n")
        # Write details of each rented land to the invoice
        for land in rented_lands:
            file.write(f"Kitta Number: {land.get('Kitta Number', 'N/A')}, "
                       f"City/District: {land.get('City/District', 'N/A')}, "
                       f"Direction: {land.get('Direction', 'N/A')}, "
                       f"Area: {land.get('Area (anna)', 'N/A')} anna\n")
        file.write(f"Duration of Rent: {rented_duration} months\n")
        file.write(f"Total Amount: NPR {total_amount}\n")
    
    # Print invoice to terminal
    print("\nRent Invoice")
    print(f"Customer Name: {customer_name}")
    print(f"Date and Time of Rent: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Rented Lands:")
    for land in rented_lands:
        print(f"Kitta Number: {land.get('Kitta Number', 'N/A')}, "
              f"City/District: {land.get('City/District', 'N/A')}, "
              f"Direction: {land.get('Direction', 'N/A')}, "
              f"Area: {land.get('Area (anna)', 'N/A')} anna")
    print(f"Duration of Rent: {rented_duration} months")
    print(f"Total Amount: NPR {total_amount}")
    # Return the total amount for possible further use
    return total_amount

def generate_return_invoice(customer_name, returned_lands, fine_amount):
    invoice_name = f"{customer_name}_return_invoice_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(invoice_name, 'w') as file:
        file.write("Return Invoice\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Date and Time of Return: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("Returned Lands:\n")
        # Write details of each returned land to the invoice
        for land in returned_lands:
            file.write(f"Kitta Number: {land.get('Kitta Number', 'N/A')}, "
                       f"City/District: {land.get('City/District', 'N/A')}, "
                       f"Direction: {land.get('Direction', 'N/A')}, "
                       f"Area: {land.get('Area (anna)', 'N/A')} anna\n")
        # If there is a fine amount, include it in the invoice
        if fine_amount > 0:
            file.write(f"Fine Amount: NPR {fine_amount}\n")
            
    # Print invoice to terminal
    print("\nReturn Invoice")
    print(f"Customer Name: {customer_name}")
    print(f"Date and Time of Return: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Returned Lands:")
    for land in returned_lands:
        print(f"Kitta Number: {land.get('Kitta Number', 'N/A')}, "
              f"City/District: {land.get('City/District', 'N/A')}, "
              f"Direction: {land.get('Direction', 'N/A')}, "
              f"Area: {land.get('Area (anna)', 'N/A')} anna")
    # Print fine amount if applicable
    if fine_amount > 0:
        print(f"Fine Amount: NPR {fine_amount}\n")
        















