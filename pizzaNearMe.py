from pizzapi import *

customer = Customer('Mazda', 'Biglari', 'mbiglari@yahoo.ca', '6308283854')
address = Address('2562 Salem Heights Ln SW', 'Rochester', 'MN', '55902')

store = address.closest_store()

menu = store.get_menu()

#result = menu.search(Name = 'Bread') # 'Chicken' P10ITHTC     'Pepperoni' 10TPFEAST
# 'Meat' 14SCMEATZA    'Coke' 2LCOKE     'Cheese' P10IGFCZ
# 'Parmesan' B8PCPT        
order1 = Order(store, customer, address)
order1.add_item('P10IGFCZ')   #Cheese
order1.add_item('P10ITHTC')   #Chicken
order1.add_item('10TPFEAST')  #Pepperoni
order1.add_item('2LCOKE')    #Coke

#'customer': <pizzapi.customer.Customer object at 0x00000186E350DDC0>

print(order1.__dict__['data']['Products'])




