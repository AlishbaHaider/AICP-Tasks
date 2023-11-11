# Lists for each category
category_list = ["Case", "RAM", "Main Hard Disk Drive",
                 "Solid State Drive", "Second Hard Disk Drive", "Optical Drive",
                  "Operating System"]

itemcode_list = [
    ["A1", "A2"],  # Case
    ["B1", "B2", "B3"],  # RAM
    ["C1", "C2", "C3"],  # Main Hard Disk Drive
    ["D1", "D2"],  # Solid State Drive
    ["E1", "E2", "E3"],  # Second Hard Disk Drive
    ["F1", "F2"],  # Optical Drive
    ["G1", "G2"]  # Operating System
]

description_list = [
    ["Compact", "Tower"],  # Case
    ["8 GB", "16 GB", "32 GB"],  # RAM
    ["1 TB HDD", "2 TB HDD", "4 TB HDD"],  # Main Hard Disk Drive
    ["240 GB SSD", "480 GB SSD"],  # Solid State Drive
    ["1 TB HDD", "2 TB HDD", "4 TB HDD"],  # Second Hard Disk Drive
    ["DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer"],  # Optical Drive
    ["Standard Version", "Professional Version"]  # Operating System
]

price_list = [
    [75.00, 150.00],  # Case
    [79.99, 149.99, 299.99],  # RAM
    [49.99, 89.99, 129.99],  # Main Hard Disk Drive
    [59.99, 119.99],  # Solid State Drive
    [49.99, 89.99, 129.99],  # Second Hard Disk Drive
    [50.00, 100.00],  # Optical Drive
    [100.00, 175.00]  # Operating System
]

# Function to display available items and get user's choice
def choose_item(category, items):
    print('Available ' , category, ' items')
    for i, item in enumerate(items):
        print(itemcode_list[category_list.index(category)][i] ,"-",description_list[category_list.index(category)][i],'$', price_list[category_list.index(category)][i])

    while True:
        print('Choose a ',category, 'item (Enter item code): ')
        choice = input().upper()
        if choice in itemcode_list[category_list.index(category)]:
            index = itemcode_list[category_list.index(category)].index(choice)
            return (itemcode_list[category_list.index(category)][index], items[index],
                    price_list[category_list.index(category)][index])
        print("Invalid item code. Please try again.")


def calculate_price( additional_items):
    total_price = 0
    chosen_items = []
    for category, item in additional_items.items():
        total_price += item[2]
        chosen_items.append(category + ": " + str(item[1]))
    return total_price, chosen_items

# Basic set of components
basic_price = 200.00

#TASK1
print("---welcome to online computer store---")
print("---select required essential components for your computer---")
case = choose_item("Case", description_list[category_list.index("Case")])
ram = choose_item("RAM", description_list[category_list.index("RAM")])
hdd = choose_item("Main Hard Disk Drive", description_list[category_list.index("Main Hard Disk Drive")])

# Display chosen items and calculate computer price
additional_items = {"Case": case, "RAM": ram, "Main Hard Disk Drive": hdd}
total_price, chosen_items = calculate_price(additional_items)

# Output chosen items and price
print("Chosen items:")
print("\n".join(chosen_items))
print('Total price: $' , total_price)

#TASK2
additional_items = {}
while True:
        choice = input("Do you want to purchase additional items? (yes/no): ").lower()
        if choice != 'yes':
            break

        category = input("Enter the category of additional item (e.g., SSD, Optical Drive): ")
        items = description_list[category_list.index(category)]

        if items:
            additional_item = choose_item(category, items)
            additional_items[category] = additional_item
additional_price = calculate_price( additional_items)
total_price = total_price+additional_price[0]+basic_price



#TASK3
discount = 0
if len(additional_items) == 1:
        discount = 0.05 * total_price
elif len(additional_items) >= 2:
        discount = 0.10 * total_price

discounted_price = total_price - discount

# Output final bill
print("--------------------------------------")
print("Discount applied: $",discount)
print("Final price before discount: $",total_price)
print("Final price after discount: $",discounted_price)
print("Thankyou for shopping :)")
print("--------------------------------------")



