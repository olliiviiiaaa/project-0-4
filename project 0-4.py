# Define the list of authorized vehicles
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]
4

# Function to print the list of authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to search for a vehicle in the allowed list
def search_vehicle():
    vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()
    if vehicle_to_search in AllowedVehiclesList:
        print(f"{vehicle_to_search} is an authorized vehicle")
    else:
        print(f"{vehicle_to_search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Function to add a new vehicle to the allowed list
def add_vehicle():
    vehicle_to_add = input("Please Enter the full Vehicle name you would like to add: ").strip()
    AllowedVehiclesList.append(vehicle_to_add)
    print(f'You have added "{vehicle_to_add}" as an authorized vehicle')

# Function to remove a vehicle from the allowed list
def remove_vehicle():
    vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
    if vehicle_to_remove in AllowedVehiclesList:
        confirmation = input(f'Are you sure you want to remove "{vehicle_to_remove}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            AllowedVehiclesList.remove(vehicle_to_remove)
            print(f'You have REMOVED "{vehicle_to_remove}" as an authorized vehicle')
        else:
            print("Vehicle removal canceled.")
    else:
        print(f'"{vehicle_to_remove}" is not in the Authorized Vehicles List.')

# Function to display the main menu and handle user input
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")
        
        # Get user input
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ").strip()
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            search_vehicle()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            remove_vehicle()
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3, 4, or 5.")

# Start the program
menu()
