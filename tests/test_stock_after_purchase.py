from vendingmachine.application.maintenance import MaintenanceClass
from vendingmachine.application.product import ProductClass
from vendingmachine.application.stock import StockClass
from vendingmachine.application.helper import get_db_conx
import unittest

fake_product_list = [('orange', 2.5), ('apple', 2)]
fake_restock_list = [('orange', 10), ('apple', 10)]
fake_product_purchases = {'orange': 2, 'apple': 3}


class TestStockAfterPurchase(unittest.TestCase):

    def test_after_purchases(self):
        # create connection to db
        con = get_db_conx()

        # initiating all class
        product_init = ProductClass(con)
        stock_init = StockClass(con)
        maintenance_init = MaintenanceClass(con, product_init, stock_init)

        # adding fake products
        maintenance_init.define_product_for_sale(fake_product_list)
        # stocking up fake products
        maintenance_init.restock(fake_restock_list)

        for product, qty in fake_product_purchases.items():
            print('### proceeding with testing for {}'.format(product))
            print('### purchase quantity is: {}'.format(qty))
            product_id, product_price = product_init.get_product_id(product)
            qty_before, product_exist_flag_before = stock_init.get_current_product_qty(product_id)
            stock_init.update_product_stock_after_purchase(product_id, qty)
            qty_after, product_exist_flag_after = stock_init.get_current_product_qty(product_id)
            self.assertEqual(qty_before, qty_after + qty)


if __name__ == '__main__':
    unittest.main()
