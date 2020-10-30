from pizzapi import *

customer = Customer('Mazda', 'Biglari', 'mbiglari@yahoo.ca', '6308283854')
address = Address('2562 Salem Heights Ln SW', 'Rochester', 'MN', '55902')

store = address.closest_store()

menu = store.get_menu()

result = menu.search(Name = 'Pepperoni') # 'Chicken' P10ITHTC     'Pepperoni' 10TPFEAST
# 'Meat' 14SCMEATZA    'Coke' 2LCOKE     'Cheese' P10IGFCZ

order = Order(store, customer, address)
order.add_item('P10IGFCZ')   #Cheese
order.add_item('P10ITHTC')   #Chicken
order.add_item('10TPFEAST')  #Pepperoni
#order.add_item('2LCOKE')    #Coke

#print(order)




