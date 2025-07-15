
def read_info(file_name):
    # Initialize an empty list to store land information
    lands = []
    
    # Open the file in read mode
    with open(file_name, 'r') as file:
        
        # Read the first line of the file which contains the headers
        headers = file.readline().strip().split(', ')

        # Iterate through the remaining lines in the file
        for line in file:
            land_data = line.strip().split(', ')
            # Create a dictionary by zipping headers and land_data together
            land = dict(zip(headers, land_data))
            lands.append(land)

    # Return the list of land dictionaries
    return lands
