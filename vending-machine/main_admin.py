from application.maintenance import MaintenanceClass
from application.product import ProductClass
from application.stock import StockClass
from application.helper import get_db_conx
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
maintenance_init.define_product_for_sale(product_list)

# restocking the machine
maintenance_init.restock(restock_list)

con.close()








