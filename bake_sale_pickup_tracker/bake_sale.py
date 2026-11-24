from datetime import datetime #if 3.14 or newer, can import date and omit the .date() at the end of the strptime(). Use datetime of possibility of older python version
from pathlib import Path
import csv

DATE_FORMAT = "%d/%m/%y"
CSV_PATH = Path(__file__).parent/"bake_sale_orders.csv"
FIELDNAMES = ["order_id","customer_name","item", "quantity", "pickup_date", "collected", "order_type", "gift_message"]

class BakeSaleOrder:
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool)->None:
        if quantity <=0:
            raise ValueError("Quantity must be a positive whole number.")

        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.pickup_date = pickup_date
        self.collected = collected

    def __str__(self)->str:
        #collected value of True means"collected" otherwise "Awaiting pickup"
        status = "Collected" if self.collected else "Awaiting pickup"
        return f"{self.order_id} | {self.customer_name} | {self.quantity} x {self.item} | {self.pickup_date.strftime(DATE_FORMAT)} | {status}"

    #Method to create a dictionary so we can use Dictionary Writer to write to the file
    def to_csv_row(self) ->dict[str,str | int]:
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "item": self.item,
            "quantity": self.quantity,
            "pickup_date": self.pickup_date.strftime(DATE_FORMAT),
            "collected": "yes" if self.collected else "no",
            "order_type": "regular",
            "gift_message": ""
        }

  
class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message: str)->None:
        super().__init__(order_id, customer_name, item, quantity, pickup_date, collected)
        # if not gift_message.strip():#OOPS GOT THIS BACKWORDS! NEED TO FIX!
        #     self.gift_message = gift_message
        #FIXED - SORRY FOLKS! :)
        if not gift_message.strip():
            raise ValueError("A gift order needs a gift message.")
        self.gift_message = gift_message

    def __str__(self)->str:
        return f"{super().__str__()} | Gift message: {self.gift_message}"

    def to_csv_row(self)-> dict[str, str|int]:
        row = super().to_csv_row()
        row["order_type"] = "gift"
        row["gift_message"] = self.gift_message 
        return row

        
    

class BakeSale:
    def __init__(self)->None:
        #list of BakeSaleOrder objects
        self.orders: list[BakeSaleOrder] = []

    def load_orders(self, csv_path: Path):
        try:
            with open(csv_path, 'r', newline = "", encoding = "utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:                    
                        order_id = row["order_id"]                       
                        customer_name = row["customer_name"]
                        item = row["item"]
                        quantity = int(row["quantity"])
                        pickup_date = datetime.strptime(row["pickup_date"],DATE_FORMAT).date()
                        collected = row["collected"] == "yes"
                        #evaluate the gift type to see if we are creating a regular or gift order
                        order_type = row["order_type"]
                        if order_type =="regular":
                            order = BakeSaleOrder(order_id,customer_name, item, quantity, pickup_date, collected)
                        else:
                            order = GiftOrder(order_id,customer_name, item, quantity, pickup_date, collected, row["gift_message"])
                        self.add_order(order)
                        #if the valueError is raised from add_order, print the error and continue to the next loop iteration
                    except ValueError as error:
                        print(f"{error}")
                        continue                                                                       
        except FileNotFoundError:                   
            print("File not found")                                                                    

    def add_order(self, order: BakeSaleOrder) -> None:
        # Search for an order with the same ID before changing the list.
        if self.find_order(order.order_id) is not None:
            raise ValueError(f"Order ID {order.order_id} is already in use.")
        self.orders.append(order)

    # Return the first matching order object, or None when the search finds no match.
    def find_order(self, order_id: str) -> BakeSaleOrder | None:
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def list_orders(self)->None:
        if not self.orders:
            print("There are no orders")
        else:
            for order in self.orders:
                print(order)
    
    #Write the list of order objects to the file
    def save_order(self, csv_path: Path)-> None:
        with open(csv_path,'w',newline ='',encoding = 'utf-8') as file:
            writer = csv.DictWriter(file,FIELDNAMES) 
            writer.writeheader()           
            for order in self.orders:
                writer.writerow(order.to_csv_row())


def show_pickups(bake_sale: BakeSale) -> None:
    date_text = input("Pickup date (dd/mm/yy): ").strip()
    try:
        pickup_date = datetime.strptime(date_text, DATE_FORMAT)
    except ValueError:
        print("Enter a valid date in dd/mm/yy format.")
        return

    total_quantity = 0
    for order in bake_sale.orders:
        if order.pickup_date == pickup_date.date() and not order.collected:
            print(order)
            total_quantity += order.quantity

    if total_quantity:
        print(f"Total quantity: {total_quantity}")
    else:
        print("There are no pickups remaining for that date.")

def prompt_for_order(bake_sale: BakeSale) -> None:
    order_id = input("Order ID: ").strip()
    customer_name = input("Customer name: ").strip()
    item = input("Item: ").strip()

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Quantity must be a positive whole number.")
        return

    try:
        pickup_date = datetime.strptime(input("Pickup date (dd/mm/yy): ").strip(), DATE_FORMAT)
    except ValueError:
        print("Enter a valid date in dd/mm/yy format.")
        return

    try:
        order_type = input("Order type (regular/gift): ").strip().lower()
        if order_type == "regular":
            order = BakeSaleOrder(order_id, customer_name, item, quantity, pickup_date,False)
        elif order_type == "gift":
            gift_message = input("Gift message: ").strip()
            order = GiftOrder(order_id, customer_name, item, quantity, pickup_date, False, gift_message)
        else:
            raise ValueError("Order type must be regular or gift.")
        bake_sale.add_order(order)
    except ValueError as error:
        print(error)
        return

    print(f"Added order {order.order_id}.")

def mark_collected(bake_sale: BakeSale) -> None:
    order_id = input("Order ID: ").strip()
    order = bake_sale.find_order(order_id)
    if order is None:
        print(f"No order found with ID {order_id}.")
    elif order.collected:
        print(f"Order {order_id} has already been collected.")
    else:
        order.collected = True
        print(f"Marked {order_id} as collected.")



def main() -> None:
    bake_sale = BakeSale()
    try:
        bake_sale.load_orders(CSV_PATH)
    except (OSError, ValueError) as error:
        print(f"Could not load the orders: {error}")
        return

    while True:
        print(
            "\n=== Bake Sale Pickup Tracker ===\n"
            "1. List all orders\n"
            "2. Show pickups for a date\n"
            "3. Add an order\n"
            "4. Mark an order as collected\n"
            "5. Save and exit"
        )
        choice = input("Choice: ").strip()

        if choice == "1":
            bake_sale.list_orders()
        elif choice == "2":
            show_pickups(bake_sale)
        elif choice == "3":
            prompt_for_order(bake_sale)
        elif choice == "4":
            mark_collected(bake_sale)
        elif choice == "5":
            try:
                bake_sale.save_order(CSV_PATH)
            except OSError as error:
                print(f"Could not save the orders: {error}")
            else:
                print("Orders saved. Goodbye!")
                break
        else:
            print("Choose a menu option from 1 to 5.")

if __name__ == "__main__":
    main()






#test
# bake_sale = BakeSale()
# bake_sale.load_orders(CSV_PATH)
# bake_sale.list_orders()

# #create and add a new order to the orders list and save it to the file
# gift_order = GiftOrder("abc123","Bob","stuff",4,datetime.strptime("20/01/26",DATE_FORMAT),False,"Easy as 123")
# bake_sale.add_order(gift_order)

# bake_sale.list_orders()

# bake_sale.save_order(CSV_PATH)









#save_order
#rest is extra and will be posted

                            





                    # 
        




    
        

