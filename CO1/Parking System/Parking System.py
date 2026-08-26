# ==========================================
#       PARKING MANAGEMENT SYSTEM
# ==========================================

from datetime import datetime

# Total parking slots
TOTAL_SLOTS = 10

# Dictionary to store parked vehicles
parking_slots = {i: None for i in range(1, TOTAL_SLOTS + 1)}

# Store vehicle details
vehicles = {}


# ------------------------------------------
# Display Parking Slots
# ------------------------------------------
def display_slots():
    print("\n========== PARKING SLOTS ==========")

    for slot, vehicle in parking_slots.items():

        if vehicle is None:
            print(f"Slot {slot}: Available")
        else:
            print(f"Slot {slot}: Occupied - {vehicle}")

    print("===================================")


# ------------------------------------------
# Park Vehicle
# ------------------------------------------
def park_vehicle():

    print("\n========== VEHICLE ENTRY ==========")

    vehicle_number = input("Enter vehicle number: ").upper()
    vehicle_type = input("Enter vehicle type (Car/Bike): ").capitalize()

    # Check if vehicle already exists
    if vehicle_number in vehicles:
        print("Vehicle is already parked!")
        return

    # Find available slot
    available_slot = None

    for slot, vehicle in parking_slots.items():
        if vehicle is None:
            available_slot = slot
            break

    if available_slot is None:
        print("Sorry! Parking is full.")
        return

    # Store vehicle information
    entry_time = datetime.now()

    parking_slots[available_slot] = vehicle_number

    vehicles[vehicle_number] = {
        "type": vehicle_type,
        "slot": available_slot,
        "entry_time": entry_time
    }

    print("\nVehicle parked successfully!")
    print("Vehicle Number:", vehicle_number)
    print("Vehicle Type:", vehicle_type)
    print("Parking Slot:", available_slot)
    print("Entry Time:", entry_time.strftime("%Y-%m-%d %H:%M:%S"))


# ------------------------------------------
# Vehicle Exit
# ------------------------------------------
def exit_vehicle():

    print("\n========== VEHICLE EXIT ==========")

    vehicle_number = input("Enter vehicle number: ").upper()

    if vehicle_number not in vehicles:
        print("Vehicle not found!")
        return

    vehicle = vehicles[vehicle_number]

    exit_time = datetime.now()
    entry_time = vehicle["entry_time"]

    # Calculate parking duration
    duration = exit_time - entry_time

    hours = duration.total_seconds() / 3600

    # Minimum chargeable time = 1 hour
    chargeable_hours = max(1, int(hours + 0.99))

    # Parking charges
    if vehicle["type"] == "Car":
        rate = 50
    else:
        rate = 20

    total_fee = chargeable_hours * rate

    # Free the parking slot
    slot = vehicle["slot"]
    parking_slots[slot] = None

    # Remove vehicle
    del vehicles[vehicle_number]

    print("\n========== PARKING BILL ==========")
    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle["type"])
    print("Parking Slot   :", slot)
    print("Entry Time     :", entry_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Exit Time      :", exit_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Duration       :", chargeable_hours, "hour(s)")
    print("Rate           : ₹", rate, "/hour")
    print("Total Fee      : ₹", total_fee)
    print("==================================")


# ------------------------------------------
# Search Vehicle
# ------------------------------------------
def search_vehicle():

    print("\n========== SEARCH VEHICLE ==========")

    vehicle_number = input("Enter vehicle number: ").upper()

    if vehicle_number not in vehicles:
        print("Vehicle is not currently parked.")
        return

    vehicle = vehicles[vehicle_number]

    print("\nVehicle Details")
    print("---------------------------")
    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle["type"])
    print("Parking Slot   :", vehicle["slot"])
    print(
        "Entry Time     :",
        vehicle["entry_time"].strftime("%Y-%m-%d %H:%M:%S")
    )


# ------------------------------------------
# Display Parked Vehicles
# ------------------------------------------
def display_vehicles():

    print("\n========== PARKED VEHICLES ==========")

    if not vehicles:
        print("No vehicles are currently parked.")
        return

    for vehicle_number, details in vehicles.items():

        print("-----------------------------")
        print("Vehicle Number :", vehicle_number)
        print("Vehicle Type   :", details["type"])
        print("Parking Slot   :", details["slot"])
        print(
            "Entry Time     :",
            details["entry_time"].strftime("%Y-%m-%d %H:%M:%S")
        )


# ------------------------------------------
# Main Menu
# ------------------------------------------
def main():

    while True:

        print("\n")
        print("======================================")
        print("       PARKING MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Park Vehicle")
        print("2. Vehicle Exit")
        print("3. Display Parking Slots")
        print("4. Search Vehicle")
        print("5. Display Parked Vehicles")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            park_vehicle()

        elif choice == "2":
            exit_vehicle()

        elif choice == "3":
            display_slots()

        elif choice == "4":
            search_vehicle()

        elif choice == "5":
            display_vehicles()

        elif choice == "6":
            print("\nThank you for using Parking Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ------------------------------------------
# Start Program
# ------------------------------------------
if __name__ == "__main__":
    main()
