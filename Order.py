class Order:
    def __init__(self, order_num, product_id, item_type, item_name, product_details, factory_ref, quantity):
        self.order_num = order_num
        self.product_id = product_id
        self.item_type = item_type
        self.item_name = item_name
        self.product_details = product_details
        self.factory_ref = factory_ref
        self.quantity = quantity