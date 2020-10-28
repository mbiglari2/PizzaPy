from pizzapi import *

#Objects exists in a class

#Classes examples:
#Customer is a class
#Object examples: my_store and my_menu

customer = Customer('Blade', 'Nelson', 'powderblock@gmail.com', '4157588103')
address = Address('75 Westover Ave', 'Ann Arbor', "mi", "48104")

my_store = address.closest_store()

my_menu = my_store.get_menu()

result = my_menu.search(Name = 'Meat')

print(result)
