from application.maintenance import MaintenanceClass
from application.product import ProductClass
from application.stock import StockClass
from application.helper import get_db_conx, list_of_dict_nice_display, cursor_list_dict
from application.customer import CustomerClass

# create connection to db
con = get_db_conx()

# initiating all class
product_init = ProductClass(con)
stock_init = StockClass(con)
print('\n#####################################################')
print('#### - The current stock situation is as follow:')
list_of_dict_nice_display(cursor_list_dict(stock_init.get_current_stock()))
print('#####################################################\n')

customer_init = CustomerClass(con, product_init, stock_init)
product_id, stock_qty, purchase_qty = customer_init.get_user_input()
stock_init.update_product_stock_after_purchase(product_id, purchase_qty)

print('\n#####################################################')
print('#### - After the purchase the overall stock situation is:')
list_of_dict_nice_display(cursor_list_dict(stock_init.get_current_stock()))
print('#####################################################\n\n')

print('Bye!')

con.close()
