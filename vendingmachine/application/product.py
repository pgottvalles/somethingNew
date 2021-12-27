from .helper import cursor_list_dict


class ProductClass:

    def __init__(self, con):
        self.con = con

    def create_product_table(self):
        create_product_table_sql = \
            """CREATE TABLE IF NOT EXISTS products (product_id int, product_name text, price real)"""
        cur = self.con.cursor()
        cur.execute(create_product_table_sql)

    def get_product_id(self, product_name):
        resp = self.con.cursor().execute(
            "select product_id, price from products where product_name=:prod",
            {"prod": product_name})
        dict_resp = cursor_list_dict(resp)
        if len(dict_resp) == 0:
            raise Exception('the product ({prod}) you are trying to stck up is not defined as product'.format(
                prod=product_name))
        id = dict_resp[0]['product_id']
        price = dict_resp[0]['price']
        return id, price

    def get_available_product(self):
        cur = self.con.cursor()
        resp = cur.execute(
            'select p.product_name, p.price from products p, stocks s where p.product_id=s.product_id and s.qty > 0')
        return resp
