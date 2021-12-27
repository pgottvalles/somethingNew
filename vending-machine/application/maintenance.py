from application.helper import cursor_list_dict, list_of_dict_nice_display


class MaintenanceClass:

    def __init__(self, con, product_init, stock_init):
        self.con = con
        self.product_init = product_init
        self.stock_init = stock_init

    def restock(self, stock_list):
        """
        re-stock the vending machine
        :param stock_list: python list of tuple of product name and qty to be restocked
        """
        cur = self.con.cursor()
        for i in stock_list:
            product_name = i[0]
            qty = i[1]
            product_id, product_price = self.product_init.get_product_id(product_name)
            current_qty, product_exist_in_table_flag = self.stock_init.get_current_product_qty(product_id)
            if product_exist_in_table_flag:
                cur.execute(
                    """update stocks
                    set qty = ?
                    where product_id = ?""",
                    (current_qty + qty, product_id))
            else:
                cur.execute(
                    "insert into stocks values (?, ?)",
                    (product_id, current_qty + qty))
            self.con.commit()
        print('The machine has been restocked, the current situation is as follow:')
        list_of_dict_nice_display(cursor_list_dict(self.stock_init.get_current_stock()))

    def define_product_for_sale(self, product_list):
        """
        define product for sale
        :param product_list: list of tuple of product name and their price
        """
        cur = self.con.cursor()
        for product in product_list:
            product_name = product[0]
            product_price = product[1]
            cur.execute("select product_id from products where product_name=:prod", {"prod": product_name})
            resp = cur.fetchall()
            print()
            if len(resp) == 0:
                print('inserting product')
                max_product_id = cur.execute('select max(product_id) from products').fetchone()[0]
                if not max_product_id:
                    max_product_id = 1
                cur.execute(
                    "insert into products values (?, ?, ?)",
                    (max_product_id + 1, product_name, product_price))
            else:
                retreived_product_id = resp[0][0]
                cur.execute(
                    """update products
                    set product_name = ? ,
                        price = ?
                    where product_id = ?""",
                    (product_name, product_price, retreived_product_id))
            self.con.commit()

        print('### -- products table has been updated as follow:\n')
        list_of_dict_nice_display(cursor_list_dict(cur.execute('select * from products')))
