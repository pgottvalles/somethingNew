# small and simple vending machine

# Overview
Very simple vending machine
based on python script

# Requirements
the following requirements have been selected:
- as admin/maintenance personnel I want to be able to check vending machine current product stock
- as admin/maintenance personnel I want to be able to stock up vending machine

- as user I want to be able to check available products
- as user I want to be able to select a certain quantity of product and pay for it accordingly
    - I want to be able to give some amount of money
        - The machine should tell me if the amount if sufficient
        - If I have given too much, I want to be able to get back the difference 
    - if an out of stock product is selected I should get a message accordingly
    - if a non existing product is selected, I should get a message accordingly
    
    - when a product is bought stock for considered product should be decreased by purchased quantity accordingly

# usage for maintenace personnel
in order to:
- initialize the database
- create the needed tables
- define the initial producta
- do the initial stock up of the machine
run the following command under vendingmachine folder
````
(cd vendingmachine)    
python main_admin.py
````

under the **vendingmachine/config/admin_config.py** folder, you can configure:
- the exact list of products
- the exact stock you want to have for each product.

## product
you can define your product as a list of tuples as follow:
````
product_list = [
    ('water', 2.5),
    ('chocolate', 2),
    ('nuts', 3.5),
    ('biscuits', 1.5)
]
````
the first attribute is the product name, the second is its price
if the product already exsist, the price will be updated, otherwize it will be added


## re-stock
you can define the additional stock you want to add in your machine by updating the restock_list as follow:
````
restock_list = [
    ('water', 11),
    ('nuts', 6),
    ('chocolate', 15),
    ('biscuits', 20)
]
````
- the first attribute is the product name. The second is the stock amount
- Stock will be updaded so that the qty defined in the configuration, will be added to the quantity pre-existing in the stock table
- if the product is hasn't been added yet in the stock, it will then inserted

Once both list are updated, you can just re-run the command:
````    
python main_admin.py
````


# usage for customer
in order to enter the customer interactive selection run the following command:
````
python main_customer.py
```` 
follow the instructions, you will be giuded through the purchase:

you will first receive the following welcoming message:
````text
#####################################################
#### - The current stock situation is as follow:
{'product_name': 'water', 'qty': 23}
{'product_name': 'chocolate', 'qty': 55}
{'product_name': 'nuts', 'qty': 20}
{'product_name': 'biscuits', 'qty': 180}
#####################################################

### Hello! the available product are:
water (price: 2.5)
nuts (price: 3.5)
chocolate (price: 2.0)
biscuits (price: 1.5)
````

- you will then be asked if you want to start purchasing something
````
Do you want to buy one of our product? (y/n):
````
- if you type y, you will be ask to enter the product you want to purchase
````text
select the product you want to buy: biscuits
You have selected: biscuits
The current stock is: 180
````

- you will then be asked for the quantity.
    - if you enter a quantity higher than the stock, you will get the following message
    ````text
      select the amount you want to buy: 190
      You are trying to purchase more than what we have in stock for that product currently ...
    => Please select a lower qty
    ````

  - you will be able to retry. This time if you select a relevant qty, you will get the following message
  ````text
    select the amount you want to buy: 180
    We have enough of the selected product in stock!!
  ````

- you will then be asked for the ammount of money you want to pay with
````text
select or add some amount of money to pay with:
````

- you will be asked to add up  some money until the correct amount is reached
````
select or add some amount of money to pay with: 180

You havent given enough money
=> Please add some more as you still need to pay 90.0 euro(s).

select or add some amount of money to pay with: 60

You havent given enough money
=> Please add some more as you still need to pay 30.0 euro(s).

select or add some amount of money to pay with: 15

You havent given enough money
=> Please add some more as you still need to pay 15.0 euro(s).

select or add some amount of money to pay with: 20
you have paid enough!

you have paid enough!

=> you will get back 5.0 euro(s)
````

- once the transaction is done, you will get updated on the product's situation
````text
The stock quantity of the given product has been updated. It is now: 0
````

- and finally you will get updated on the stock overall situation
````text
#####################################################
#### - After the purchase the stock situation is:
{'product_name': 'water', 'qty': 23}
{'product_name': 'chocolate', 'qty': 55}
{'product_name': 'nuts', 'qty': 20}
{'product_name': 'biscuits', 'qty': 0}
#####################################################
````

# unittest
in order to test transaction mechanism, please run the following command in the root of the repository
````text
python -m unittest discover -s tests
````
- This will run the python files begining with test_ located under the folder **tests**
- the test **test_stock_after_purchase.py** will verify for a list of predefined purchases (fake_product_purchases) that:
 ````text
    quantity after purchase = quantity before purchase - purchased quantity
````

