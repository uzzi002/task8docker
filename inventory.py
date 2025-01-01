#========The beginning of the class==========

class Shoe:
    """Represents a shoe in the inventory."""

    def __init__(self, country, code, product, cost, quantity):
        """Initialize the attributes for the Shoe class."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Returns the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """Returns a formatted string representation of a shoe."""
        return (f"Country: {self.country}, Code: {self.code}, Product: {self.product}, "
                f"Cost: {self.cost:.2f}, Quantity: {self.quantity}")


#=============Shoe list===========
shoe_list = []


#==========Functions outside the class==============

def read_shoes_data():
    """Reads data from inventory.txt, creates Shoe objects, and appends them to shoe_list."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe_list.append(Shoe(country, code, product, cost, quantity))
        print(f"Loaded {len(shoe_list)} shoes.")
    except FileNotFoundError:
        print("Error: 'inventory.txt' file not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def write_shoes_data():
    """Writes the current shoe_list back to inventory.txt."""
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")  # Write the header
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Changes saved to 'inventory.txt'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def capture_shoes():
    """Allows the user to input new shoe data and adds it to shoe_list."""
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    write_shoes_data()
    print("Shoe captured successfully!")


def view_all():
    """Displays all the shoes in shoe_list in an easy-to-read, aligned format."""
    if not shoe_list:
        print("No shoe data available.")
        return

    print("\nAll Shoes:")
    for shoe in shoe_list:
        print(f"-------------------------------------")
        print(f"Country:      {shoe.country}")
        print(f"Code:         {shoe.code}")
        print(f"Product:      {shoe.product}")
        print(f"Cost:         {shoe.cost:.2f}")
        print(f"Quantity:     {shoe.quantity}")
        print(f"-------------------------------------")


def re_stock():
    """Finds the shoe with the lowest quantity and allows the user to restock it."""
    if not shoe_list:
        print("No shoe data available.")
        return

    lowest_stock = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Lowest stock item: {lowest_stock}")
    restock = int(input("Enter quantity to add: "))
    lowest_stock.quantity += restock
    write_shoes_data()
    print("Stock updated successfully!")


def search_shoe():
    """Searches for a shoe by its code."""
    code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")


def value_per_item():
    """Calculates and displays the total value for each shoe."""
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Code: {shoe.code}, Product: {shoe.product}, Total Value: {value:.2f}")


def highest_qty():
    """Finds and displays the shoe with the highest quantity."""
    if not shoe_list:
        print("No shoe data available.")
        return

    highest_stock = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"Product with the highest quantity (For Sale): {highest_stock}")


#==========Main Menu=============

def main_menu():
    """Menu-driven interface for the inventory management system."""
    read_shoes_data()  # Load data initially

    while True:
        print("\nSelect an option:")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Restock lowest quantity shoe")
        print("4. Search for a shoe by code")
        print("5. Calculate total value per item")
        print("6. View highest quantity product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
