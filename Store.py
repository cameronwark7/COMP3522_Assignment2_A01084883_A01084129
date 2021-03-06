import time
import datetime


class Store:
    def __init__(self):
        self.orders = None
        self.inventory = []
        self.transactions = []

    def process_orders(self):
        for x in range(len(self.orders)):
            product_id = self.orders[x].product_id
            count = 0
            for y in self.inventory:
                if y.product_id == product_id:
                    count = (count + 1)

            if count == 0:
                # self.inventory.append(factory.create_item('missing item'))
                # create 100 of missing item and put in self.inventory list
                for y in range(100):
                    self.inventory.append(self.orders[x].factory_ref.create_item())
                # record the transaction
                self.define_buy_transaction('100', self.orders[x])
            else:
                num_bought = self.orders[x].quantity
                original_num_bought = num_bought
                for z in self.inventory:
                    if num_bought == 0:
                        break
                    if z.product_id == product_id:
                        del self.inventory[self.inventory.index(z)]
                        num_bought = (num_bought - 1)
                self.define_buy_transaction(str(original_num_bought), self.orders[x])


    def define_buy_transaction(self, qty, order_obj):
        order_num = str(len(self.transactions) + 1)
        item_type = str(order_obj.item_type)
        product_id = str(order_obj.product_id)

        the_string = 'Order ' + order_num + ', Item ' + item_type + ', Product ID ' + product_id + \
                        ', Name "' + str(order_obj.item_name) + '", Quantity ' + qty
        self.transactions.append(the_string)

    def define_remove_transaction(self):
        pass

    def check_stock(self, product_id):
        product_id = product_id.upper()
        qty = 0
        for x in self.inventory:
            if x.product_id == product_id:
                qty = (qty + 1)
        if qty >= 10:
            print('In Stock')
        elif qty > 3 & qty < 10:
            print('Low')
        elif qty > 0 & qty < 3:
            print('Very Low')
        elif qty == 0:
            print('Out of Stock')
        print('----------------------')

    def create_transaction_report(self):
        x = datetime.datetime.now()
        y = datetime.datetime.now()
        top_date = y.strftime('%d-%m-%Y %H:%M')
        date = x.strftime('%d%m%Y_%H%M')
        date1 = date[:6]
        date2 = date[8:]
        final_date = date1 + date2
        file = open(final_date + '.txt', 'w')
        file.write('HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n' + str(top_date) + '\n\n')
        for x in self.transactions:
            file.write(x + '\n')
        file.close()