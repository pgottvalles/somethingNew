from application.helper import cursor_list_dict


class StockClass:

    def __init__(self, con):
        self.con = con

    def create_stock_table(self):
        create_stock_table_sql = """CREATE TABLE IF NOT EXISTS stocks (product_id int, qty int)"""
        cur = self.con.cursor()
        cur.execute(create_stock_table_sql)

    def get_current_stock(self):
        """
        Get current stock overall situation
        :return: overall stock situation
        """
        cur = self.con.cursor()
        resp = cur.execute('select p.product_name, s.qty from products p, stocks s where p.product_id=s.product_id ')
        return resp

    def get_current_product_qty(self, product_id):
        """
        Get stock quantity for a given product id
        :param product_id: product id
        :return: stock quantity for the given product id
        """
        product_exist_in_table_flag = None
        resp = self.con.cursor().execute(
            "select qty from stocks where product_id=:id",
            {"id": int(product_id)})
        dict_resp = cursor_list_dict(resp)
        if len(dict_resp) == 0:
            qty = 0
        else:
            qty = dict_resp[0]['qty']
            product_exist_in_table_flag = True
        return qty, product_exist_in_table_flag

    def update_product_stock_after_purchase(self, product_id, qty_before_purchase, qty_purchased):
        """
        Updtae product stock quantity after purchase
        :param product_id: id of the product
        :param qty_before_purchase: product quantity before purchase
        :param qty_purchased: purchased product quantity
        :return:
        """
        cur = self.con.cursor()
        updated_qty = qty_before_purchase - qty_purchased
        cur.execute(
            """update stocks
            set qty = ?
            where product_id = ?""",
            (updated_qty, product_id))
        self.con.commit()
        print('The stock quantity of the given product has been updated. It is now: {}'.format(updated_qty))
