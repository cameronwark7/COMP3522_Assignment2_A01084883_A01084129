import pandas as pd
from pandas import isnull

from Order import Order
from FactoryMapping import FactoryMapping


class OrderProcessor:
    def __init__(self):
        self.factory_mapping = FactoryMapping()

    def create_order(self, excel_file):
        spreadsheet = pd.read_excel(excel_file)
        orders = []
        total_rows = len(spreadsheet.index)
        total_columns = len(spreadsheet.columns)

        for x in range(total_rows):
            order_num = spreadsheet.loc[x, 'order_number']
            product_id = spreadsheet.loc[x, 'product_id']
            item_type = spreadsheet.loc[x, 'item']
            item_name = spreadsheet.loc[x, 'name']
            holiday = spreadsheet.loc[x, 'holiday']
            skip_values = [order_num, product_id, item_type, item_name, holiday]
            self.factory_mapping.order_num = order_num
            self.factory_mapping.product_id = product_id
            self.factory_mapping.item_type = item_type
            self.factory_mapping.item_name = item_name
            self.factory_mapping.holiday = holiday

            product_details = {}

            # initializing the product_details dictionary
            for y in range(total_columns):
                if (isnull(spreadsheet.iloc[x, y]) == False) & (spreadsheet.iloc[x, y] in skip_values == False):
                    col_name = spreadsheet.columns[x]
                    product_details[str(col_name)] = str(spreadsheet.iloc[x, y])

            factory_ref = self.factory_mapping.determine_factory(holiday, item_type, product_details)
            order = Order(order_num, product_id, item_type, item_name, product_details, factory_ref, product_details.get('quantity', None))
            orders.append(order)

        return orders