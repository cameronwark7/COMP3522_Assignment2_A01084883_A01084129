import time
import datetime


class Store:
    def __init__(self):
        self.orders = None
        self.inventory = []
        self.transactions = []

    def process_orders(self):
        for x in range(len(self.orders)):
            occurrences = self.inventory.count(self.orders[x])

            if occurrences == 0:
                # self.inventory.append(factory.create_item('missing item'))
                # create 100 of missing item and put in self.inventory list
                print('zero occurrences')
                for y in range(100):
                    self.inventory.append(self.orders[x].factory_ref.create_item())
                # record the transaction
                self.define_buy_transaction('100', self.orders[x])
            else:
                print('occurrence detected')
                self.inventory.remove(self.orders[x])  # remove item from inventory list

    def define_buy_transaction(self, qty, order_obj):
        order_num = str(len(self.transactions) + 1)
        item_type = str(order_obj.item_type)
        product_id = str(order_obj.product_id)

        the_string = 'Order ' + order_num + ', Item ' + item_type + ', Product ID ' + product_id + \
                        ', Name "' + str(order_obj.item_name) + '", Quantity ' + qty
        self.transactions.append(the_string)

    def define_remove_transaction(self):
        pass

    def create_transaction_report(self):
        x = datetime.datetime.now()
        date = x.strftime('%d%m%Y_%H%M')
        date1 = date[:6]
        date2 = date[8:]
        final_date = date1 + date2
        file = open(final_date + '.txt', 'w')
        file.write('TESTINGINGIGNI')
        file.close()