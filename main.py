from datetime import date

class User:
    def __init__(self, user_id, name, email, phone):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    def get_contact(self):
        return "Email: "+self._email+", Phone: "+self._phone
    def login(self):
        pass

    def logout(self):
        pass

class Customer(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone)
        self._address = address
        self._order_history = []

    def place_order(self, order):
        self._order_history.append(order)
        pass
    def get_address(self):
        return self._address
    def track_order(self, order_id):
        pass
    def request_refund(self, order_id):
        pass

class Admin(User):
    def __init__(self, user_id, name, email, phone, admin_id):
        super().__init__(user_id, name, email, phone)
        self._admin_id = admin_id

    def assign_courier(self, order, courier):
        pass

    def update_order_status(self, order_id, status):
        pass

class Admin(User):
    def __init__(self, user_id, name, email, phone, admin_id):
        super().__init__(user_id, name, email, phone)
        self._admin_id = admin_id

    def assign_courier(self, order, courier):
        pass

    def update_order_status(self, order_id, status):
        pass

class Order:
    def __init__(self, order_id, customer, order_date, delivery_status):
        self._order_id = order_id
        self._customer = customer
        self._order_date = order_date
        self._delivery_status = delivery_status
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def calculate_total(self):
        return sum(item.calculate_item_total() for item in self._items)

    def generate_delivery_note(self):
        note = f"Delivery Note: Order {self._order_id}\n"
        note += f"Customer: {self._customer.get_name()}\n"
        note += f"Contact: {self._customer.get_contact()}\n"
        note += f"Delivery Address: {self._customer.get_address()}\n"
        note += f"Order Date: {self._order_date}\n"
        note += f"Delivery Status: {self._delivery_status}\n\n"
        note += "Items:\n"
        for item in self._items:
            note += f"- {item.get_description()} (x{item.get_quantity()}) - {item.get_unit_price()} AED each\n"
        note += f"Total Price: {self.calculate_total()} AED\n"
        return note

    def update_status(self, status):
        self._delivery_status = status


class OrderItem:
    def __init__(self, item_code, description, quantity, unit_price):
        self._item_code = item_code
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price
    def get_description(self):
        return self._description
    def get_unit_price(self):
        return self._unit_price
    def get_quantity(self):
        return self._quantity
    def calculate_item_total(self):
        return self._quantity * self._unit_price

class Courier:
    def __init__(self, courier_id, name, phone):
        self._courier_id = courier_id
        self._name = name
        self._phone = phone

    def update_delivery_status(self, order_id, status):
        pass

class Payment:
    def __init__(self, payment_id, order, payment_method, amount):
        self._payment_id = payment_id
        self._order = order
        self._payment_method = payment_method
        self._amount = amount

    def process_payment(self):
        pass

    def refund_payment(self):
        pass


customer = Customer(1, "Sarah Johnson", "sarah.johnson@example.com", "+971-555-1234", "45 Knowledge Avenue, Dubai, UAE")
order = Order("DEL123456789", customer, date(2025, 1, 25), "Pending")
order.add_item(OrderItem("ITM001", "Wireless Keyboard", 1, 100.00))
order.add_item(OrderItem("ITM002", "Wireless Mouse & Pad Set", 1, 75.00))
order.add_item(OrderItem("ITM003", "Laptop Cooling Pad", 1, 120.00))
order.add_item(OrderItem("ITM004", "Camera Lock", 3, 15.00))

print(order.generate_delivery_note())
print(f"Total Price: AED {order.calculate_total()}")
