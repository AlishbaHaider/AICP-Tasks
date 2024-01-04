# Function for Task 1: Set up the donation system
def setup_donation_system():
    charities = []
    charity_totals = [0, 0, 0]

    for i in range(3):
        charity_name = input(f"Enter name of Charity {i + 1}: ")
        charities.append(charity_name)

    for i, charity in enumerate(charities):
        print(f"{i + 1}. {charity}")

    while True:
        try:
            charity_choice = int(input("Choose a charity (1, 2, or 3): "))
            if charity_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            shopping_bill = float(input("Enter the shopping bill amount: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    donation = shopping_bill * 0.01
    charity_totals[charity_choice - 1] += donation

    return charities, charity_totals


# Function for Task 2: Record and total each donation
def record_donation(charities, charity_totals):
    while True:
        try:
            charity_choice = int(input("Choose a charity (1, 2, or 3), or enter -1 to show totals: "))
            if charity_choice == -1:
                break
            elif charity_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, 3, or -1.")
                continue
            shopping_bill = float(input("Enter the shopping bill amount: $"))
            donation = shopping_bill * 0.01
            charity_totals[charity_choice - 1] += donation
            print(f"Donated ${donation} to {charities[charity_choice - 1]}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return charity_totals


# Function for Task 3: Show the totals so far
def show_totals(charities, charity_totals):
    sorted_totals = sorted(zip(charities, charity_totals), key=lambda x: x[1], reverse=True)
    grand_total = sum(charity_totals)

    print("\nCharity Totals:")
    for charity, total in sorted_totals:
        print(f"{charity}: ${total:.2f}")

    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")



def main():
    print("TASK 1 - Set up the donation system:")
    charities, charity_totals = setup_donation_system()

    print("\nTASK 2 - Record and total each donation:")
    charity_totals = record_donation(charities, charity_totals)

    print("\nTASK 3 - Show the totals so far:")
    show_totals(charities, charity_totals)


main()
