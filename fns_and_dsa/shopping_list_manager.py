def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Item: ")  # Fixed typo "Iten" to "Item"
            shopping_list.append(add_item)
            print(f"'{add_item}' added to the list.")  # Added confirmation
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("The list is empty!")
            else:
                remove_item = input("Item to remove: ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                    print(f"'{remove_item}' removed from the list.")
                else:
                    print(f"'{remove_item}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()  # Add empty line for better readability

if __name__ == "__main__":
    main()