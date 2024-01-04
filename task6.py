
# Task 1 - Check the contents and weight of a single sack
def check_sack(contents, weight):
    if contents not in ['C', 'G', 'S']:
        return "Rejected: Invalid contents. Please use 'C' for cement, 'G' for gravel, or 'S' for sand."
    if (contents == 'C' and not (24.9 < weight < 25.1)) or ((contents == 'G' or contents == 'S') and not (49.9 < weight < 50.1)):
        return "Rejected: Invalid weight for the contents."
    return f"Accepted: Sack contains {contents} and weighs {weight} kilograms."

# Task 2 - Check a customer’s order for delivery
def check_order():
    sacks_required = {'C': 0, 'G': 0, 'S': 0}
    sacks_rejected = 0

    for sack_type in sacks_required:
        num_sacks = int(input(f"Enter number of {sack_type} sacks required: "))
        for _ in range(num_sacks):
            weight = float(input(f"Enter weight for {_ + 1} {sack_type} sack: "))
            result = check_sack(sack_type, weight)
            if "Rejected" in result:
                print(result)
                sacks_rejected += 1
            else:
                sacks_required[sack_type] += 1

    total_weight = sum(sacks_required.values()) * 50
    print(f"Total weight of the order: {total_weight} kilograms")
    print(f"Number of sacks rejected from the order: {sacks_rejected}")

    return sacks_required
# Task 3 - Function to calculate the price for a customer's order
def calculate_price(order):
    sack_prices = {
        'C': 3,
        'G': 2,
        'S': 2
    }

    special_pack = {
        'C': 1,
        'G': 2,
        'S': 2
    }
    special_pack_price = 10

    regular_price = sum(order[sack_type] * sack_prices[sack_type] for sack_type in order)

    num_special_packs = min(order.get(sack_type, 0) // special_pack[sack_type] for sack_type in special_pack)

    if num_special_packs > 0:
        discount_price = num_special_packs * special_pack_price
        amount_saved = regular_price - discount_price
        print(f"Regular price for the order: ${regular_price}")
        print(f"Special packs in the order: {num_special_packs}")
        print(f"New price for the order after discount: ${discount_price}")
        print(f"Amount saved: ${amount_saved}")
    else:
        print(f"Regular price for the order: ${regular_price}")
        print("No special packs in the order. No discount applied.")
# Task 1
print("TASK 1 - Check a single sack:")
contents = input("Enter contents (C for cement, G for gravel, S for sand): ")
weight = float(input("Enter weight of the sack: "))
print(check_sack(contents, weight))

# Task 2
print("\nTASK 2 - Check a customer's order:")
order = check_order()

# Task 3
print("\nTASK 3 - Calculate price for the order:")
calculate_price(order)
