class Store:
    def __init__(self):
        self.orders = None
        self.inventory = []

    def process_orders(self):
        for x in range(len(self.orders)):
            occurrences = self.inventory.count(self.orders[x])

            if occurrences == 0:
                # self.inventory.append(factory.create_item('missing item'))
                # create 100 of missing item and put in self.inventory list
                print('zero occurrences')

    def create_transaction_report(self):
        pass