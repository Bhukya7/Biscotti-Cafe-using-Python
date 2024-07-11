class MenuItem:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Order:
  def __init__(self, table_number):
    self.table_number = table_number
    self.items = []
    self.is_open = True

  def add_item(self, item, quantity):
    if not self.is_open:
      print(f"Table {self.table_number} is closed. Cannot add items.")
      return
    self.items.append({"item": item, "quantity": quantity})

  def get_total_price(self, menu):
    if not self.is_open:
      return 0.0
    total_price = 0
    for item in self.items:
      item_price = menu.get_item_price(item["item"])
      total_price += item_price * item["quantity"]
    return total_price

  def close_order(self):
    self.is_open = False

class Menu:
  def __init__(self):
    self.items = {
      "coffee": 100,
      "tea": 80,
      "sandwich": 150,
      "burger": 200,
      "fries": 70,
      "cake": 120
    }

  def get_item_price(self, item_name):
    return self.items.get(item_name)

def main():
  menu = Menu()
  active_orders = {}

  print("~"*50)
  print("       Hi, my name is Bhukya Ganesh       ")
  print("         welcome to Biscotti Cafe         ")
  print("~"*50)

  while True:
    print("")
    print("Choose:")
    print("1. Open a new order")
    print("2. Add item to an order")
    print("3. Close an order")
    print("4. Exit")
    print("")
    choice = int(input("Enter your choice: "))

    if choice == 4:
      break

    if choice not in (1, 2, 3, 4):
      print("Invalid choice. Please enter a number between 1 and 4.")
      continue

    if choice == 1:
      print("")
      table_number = int(input("Enter table number to open a order: "))
      if table_number in active_orders and active_orders[table_number].is_open:
        print(f"Table {table_number} already has an open order.")
        continue
      active_orders[table_number] = Order(table_number)
      print(f"Order opened for table {table_number}")

    elif choice == 2:
      print("")
      table_number = int(input("Enter table number to add items: "))
      if table_number not in active_orders or not active_orders[table_number].is_open:
        print(f"Table {table_number} does not have an open order.")
        continue
      order = active_orders[table_number]

      print("")
      print("Menu:")
      for item, price in menu.items.items():
        print(f"{item} - ₹{price}")
      print("")
      item_name = input(f"Enter item name for Table {table_number}: ").lower()

      try:
        quantity = int(input(f"Enter quantity for {item_name} for Table {table_number}: "))
      except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

      if menu.get_item_price(item_name) is None:
        print(f">>>>>Item '{item_name}' not found in menu.")
        continue

      order.add_item(item_name, quantity)
      print("")
      print(f"{item_name} x {quantity} for Table {table_number} is added")

    elif choice == 3:
      print("")
      table_number = int(input("Enter table number to close: "))
      if table_number not in active_orders or not active_orders[table_number].is_open:
        print(f"----Table {table_number} does not have an open order.")
        continue
      print("")
      total_price = order.get_total_price(menu)
      print(f"Order for table {order.table_number}:")
      for item in order.items:
        print(f"{item['item']} x {item['quantity']}")
      print("")
      print(f"Total Price for {table_number} is : ₹{total_price}")
      print("")
      active_orders[table_number].close_order()
      print(f"~~~~~Order closed for table {table_number}")

  for table_number, order in active_orders.items():
    if order.is_open:
      print(f"Warning: Order for table {table_number} is still open.")

if __name__ == "__main__":
  main()