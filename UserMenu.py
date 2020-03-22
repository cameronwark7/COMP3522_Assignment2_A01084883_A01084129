from OrderProcessor import OrderProcessor


class UserMenu:
    def __init__(self):
        self.order_processor = OrderProcessor()

    def main_menu(self):
        print('1. Process Web Orders')
        print('2. Check Inventory')
        print('3. Exit')
        user_input = input('Choose 1-3: ')

        if user_input == '1':
            file = input('Please enter name of excel file: ')
            self.order_processor.create_order(file)
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        else:
            print('INVALID INPUT')
            print('----------------------')
            self.main_menu()

    def process_web_orders(self):
        pass

    def check_inventory(self):
        pass

    def exit(self):
        pass

def main():
    user_menu = UserMenu()
    user_menu.main_menu()

if __name__ == '__main__':
    main()