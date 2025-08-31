# ---------------- Food Menu ----------------
menu = {
    "Veg Thali": 120,
    "Non-Veg Thali": 150,
    "Biryani": 100,
    "Sandwich": 60,
    "Tea": 20,
    "Coffee": 30,
    "Soft Drink": 40
}

# ---------------- Orders Storage ----------------
orders = []

# ---------------- Recommendation Rules ----------------
def recommend_dishes(religion):
    if religion.lower() == "hindu":
        return ["Veg Thali", "Sandwich", "Tea", "Coffee", "Soft Drink"]
    elif religion.lower() == "muslim":
        return ["Biryani", "Thali", "Sandwich", "Tea", "Coffee", "Soft Drink"]
    elif religion.lower() == "jain":
        return ["Sandwich", "Tea", "Coffee", "Soft Drink"]
    elif religion.lower() == "christian":
        return list(menu.keys())
    else:
        return list(menu.keys())

# ---------------- Place an Order ----------------
def place_order():
    print("\n--- Place Your Order ---")
    train = input("Enter Train No: ").strip()
    coach = input("Enter Coach: ").strip()
    seat = input("Enter Seat No: ").strip()
    religion = input("Enter Religion/Diet: ").strip()

    recommended = recommend_dishes(religion)
    print("\nRecommended dishes for you:", ", ".join(recommended))

    print("\nMenu:")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item} - ₹{price}")

    selected_items = []
    while True:
        choice = input("Enter item number to add (or 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(menu):
            print("Invalid choice, try again.")
            continue
        item_name = list(menu.keys())[int(choice)-1]
        selected_items.append(item_name)
        print(f"Added: {item_name}")

    if not selected_items:
        print("No items selected. Order cancelled.")
        return

    total = sum(menu[item] for item in selected_items)
    order = {
        "Train": train,
        "Coach": coach,
        "Seat": seat,
        "Religion": religion,
        "Items": selected_items,
        "Total": total
    }
    orders.append(order)
    print(f"\nOrder placed! Total: ₹{total}")

# ---------------- View Orders ----------------
def view_orders():
    if not orders:
        print("\nNo orders placed yet.")
        return
    print("\n--- All Orders ---")
    for i, order in enumerate(orders, 1):
        print(f"\nOrder {i}:")
        print(f" Train: {order['Train']}")
        print(f" Coach: {order['Coach']}")
        print(f" Seat: {order['Seat']}")
        print(f" Religion: {order['Religion']}")
        print(f" Items: {', '.join(order['Items'])}")
        print(f" Total: ₹{order['Total']}")
        print("------------------------")

# ---------------- Main Loop ----------------
def main():
    while True:
        print("\n1. Place Order")
        print("2. View All Orders")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            place_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()
