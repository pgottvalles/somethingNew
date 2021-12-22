from application.helper import cursor_list_dict, list_of_dict_nice_display


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

    def def_customer_purchase(self):
        self.get_available_list()



