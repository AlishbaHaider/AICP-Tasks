
BOAT_COUNT = 10
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_HOUR = 10
CLOSING_HOUR = 17


boats = {
    boat_num: {
        "money_taken": 0,
        "total_hours_hired": 0,
        "return_time": None
    } for boat_num in range(1, BOAT_COUNT + 1)
}


# Function for Task 1: Calculate the money taken in a day for one boat
def calculate_daily_profit_for_one_boat(boat_number, start_time, hire_duration):
    if start_time < OPENING_HOUR or start_time + hire_duration > CLOSING_HOUR:
        print("Boat cannot be hired before 10:00 or returned after 17:00.")
        return

    if hire_duration == 1:
        cost = HOURLY_RATE
    elif hire_duration == 0.5:
        cost = HALF_HOUR_RATE
    else:
        print("Invalid hire duration. Please enter 1 for 1 hour or 0.5 for half an hour.")
        return

    money_taken = cost * hire_duration
    boats[boat_number]["money_taken"] += money_taken
    boats[boat_number]["total_hours_hired"] += hire_duration
    boats[boat_number]["return_time"] = start_time + hire_duration
    print(
        f"Money taken for Boat {boat_number}: ${money_taken}, Total hours hired: {boats[boat_number]['total_hours_hired']}")


# Function for Task 2: Find the next available boat
def find_next_available_boat(current_time):
    available_boats = [boat_num for boat_num, boat_data in boats.items() if
                       boat_data["return_time"] is None or boat_data["return_time"] <= current_time]
    if not available_boats:
        earliest_return_time = min(boats.values(), key=lambda x: x["return_time"])["return_time"]
        print(f"No boats available. Next available time: {earliest_return_time}")
    else:
        print(f"Available boats: {available_boats}")


# Function for Task 3: Calculate the money taken for all the boats at the end of the day
def calculate_daily_profit_for_all_boats():
    total_money_taken = sum(boat_data["money_taken"] for boat_data in boats.values())
    total_hours_hired = sum(boat_data["total_hours_hired"] for boat_data in boats.values())
    unused_boats = [boat_num for boat_num, boat_data in boats.items() if boat_data["total_hours_hired"] == 0]
    most_used_boat = max(boats, key=lambda x: boats[x]["total_hours_hired"])

    print(f"Total money taken for all boats: ${total_money_taken}")
    print(f"Total hours boats were hired: {total_hours_hired}")
    print(f"Boats not used today: {unused_boats}")
    print(f"Boat used the most: Boat {most_used_boat}, Total hours hired: {boats[most_used_boat]['total_hours_hired']}")


while True:
        print("\n--- River Boat Hire Management System ---")
        print("1. Hire a Boat")
        print("2. Check Available Boats")
        print("3. End of Day Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            boat_num = int(input("Enter Boat Number (1-10): "))
            start_time = int(input("Enter Starting Time (between 10-17): "))
            hire_duration = float(input("Enter Hire Duration (1 for 1 hour, 0.5 for half an hour): "))
            calculate_daily_profit_for_one_boat(boat_num, start_time, hire_duration)

        elif choice == '2':
            current_time = int(input("Enter Current Time: "))
            find_next_available_boat(current_time)

        elif choice == '3':
            calculate_daily_profit_for_all_boats()

        elif choice == '4':
            print("Exiting Program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-4).")
