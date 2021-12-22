from application.maintenance import MaintenanceClass
from application.product import ProductClass
from application.stock import StockClass
from application.helper import get_db_conx
from application.customer import CustomerClass
from config.admin_config import product_list, restock_list

# create connection to db
con = get_db_conx()

# initiating all class
product_init = ProductClass(con)
stock_init = StockClass(con)
maintenance_init = MaintenanceClass(con, product_init, stock_init)

# creating tables
stock_init.create_stock_table()
product_init.create_product_table()

# defining products to be sold
# maintenance_init.define_product_for_sale(product_list)

# restocking the machine
# maintenance_init.restock(restock_list)


# customer
customer_init = CustomerClass(con, product_init, stock_init)
list_available_product = customer_init.get_available_product_list()
val = input("do you want to buy one? (y/n): ")
if val == 'y':
    selection = input("select the product you want to buy")
    if selection not in list_available_product:
        raise ValueError('The product you have selected in is not in the list')
    product_id = product_init.get_product_id(selection)
    stock_qty = stock_init.get_current_product_qty(id)
    qty_check_ok = None
    while not qty_check_ok:
        purchase_qty = input("select the amount you want to buy")
        if purchase_qty > purchase_qty:
            print('You are trying to buy more than what is in stock')
            print('Please select a lower qty')
        else:
            print('enough of the product in stock')
            qty_check_ok = True
    money_inserted = input("select the amount of money inserted")







con.close()








