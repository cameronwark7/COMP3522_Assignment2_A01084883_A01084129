import math

import pandas as pd
from pandas import isnull

from Order import Order


class OrderProcessor:
    def __init__(self):
        pass

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
            product_details = {}

            # for y in range(total_columns):
            #     if isnull(spreadsheet.iloc[x, y]) == False:
            #         print(spreadsheet.iloc[x, y])

            factory_ref = None
            order = Order(order_num, product_id, item_type, item_name, product_details, factory_ref)
            orders.append(order)

        return orders