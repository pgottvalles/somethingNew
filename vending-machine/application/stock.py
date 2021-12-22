class StockClass:

    def __init__(self, con):
        self.con = con

    def create_stock_table(self):
        create_stock_table_sql = """CREATE TABLE IF NOT EXISTS stocks (product_id int, qty int)"""
        cur = self.con.cursor()
        cur.execute(create_stock_table_sql)

    def get_current_stock(self):
        cur = self.con.cursor()
        resp = cur.execute('select p.product_name, s.qty from products p, stocks s where p.product_id=s.product_id ')
        return resp

    def get_current_product_qty(self, product_id):
        product_exist_in_table_flag = None
        resp = self.con.cursor().execute(
            "select qty from stocks where product_id=:id",
            {"id": product_id}).fetchall()
        if len(resp) == 0:
            qty = 0
        else:
            qty = resp[0][0]
            product_exist_in_table_flag = True
        return qty, product_exist_in_table_flag
