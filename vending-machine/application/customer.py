from application.helper import cursor_list_dict


class CustomerClass:

    def __init__(self, con, product_init, stock_init):
        self.con = con
        self.product_init = product_init
        self.stock_init = stock_init

    def get_available_product_list(self):
        resp = self.product_init.get_available_product()
        print('### Hello! the available product are: ')
        list_dict_resp = cursor_list_dict(resp)
        list_available_product = list()
        for i in list_dict_resp:
            list_available_product.append(i['product_name'])
            print(i['product_name'] + ' (price: ' + str(i['price']) + ')')
        return list_available_product

    def get_user_input(self):
        list_available_product = self.get_available_product_list()
        val = input("\nDo you want to buy one of our product? (y/n): ")
        if val not in ['y', 'n']:
            print('Please select y (yes) or n (no')
            raise ValueError('Wrong selection. You can only choose between y and n')
        if val == 'y':
            selection = input("select the product you want to buy: ")
            print("You have selected: {}".format(selection))
            if selection not in list_available_product:
                raise ValueError('\n### The product you have selected is not available at the moment.')
            product_id, product_price = self.product_init.get_product_id(selection)
            stock_qty, product_exist_in_table_flag = self.stock_init.get_current_product_qty(product_id)
            print('The current stock is: {}'.format(stock_qty))

            purchase_qty_ok = None
            purchase_qty = 0
            while not purchase_qty_ok:
                purchase_qty_input = input("\nselect the amount you want to buy: ")
                purchase_qty = int(purchase_qty_input)
                if purchase_qty > stock_qty:
                    print('### You are trying to purchase more than what we have in stock for that product currently ...')
                    print('### => Please select a lower qty')
                else:
                    print('We have enough of the selected product in stock!!')
                    purchase_qty_ok = True
                    # purchase_qty = purchase_qty_input
            purchase_price = int(purchase_qty) * float(product_price)

            enough_money = None
            money_inserted = 0
            money_due = 0
            while not enough_money:
                money_inserted_input = input("\nselect or add some amount of money to pay with: ")
                money_inserted += float(money_inserted_input)
                if money_inserted < purchase_price:
                    print('\n### You havent given enough money')
                    print('### => Please add some more as you still need to pay {} euro(s).'.
                          format(float(purchase_price) - float(money_inserted)))
                else:
                    print('you have paid enough!')
                    print('you will get back {} euro(s)'.
                          format(float(money_inserted) - float(purchase_price)))
                    enough_money = True
                    money_due = float(money_inserted) - float(purchase_price)
        return product_id, stock_qty, purchase_qty