from datetime import datetime #if 3.14 or newer, can import date and omit the .date() at the end of the strptime(). Use datetime of possibility of older python version
from pathlib import Path
import csv

DATE_FORMAT = "%d/%m/%y"

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
                    

#List_orders
#to_csv_row for both order types
#save_order
#rest is extra and will be posted

                            





                    # 
        




    
        

