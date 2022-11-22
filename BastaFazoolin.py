#!/usr/bin/env python3

from datetime import time

class Menu:
	
	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items = items
		self.start_time = start_time
		self.end_time = end_time
		
	def __str__(self):
		return f"{self.name} menu is available from {self.start_time} to {self.end_time}"
		
	def calculate_bill(self, purchased_items):
		fSpec = ".2f"
		bill = [self.items[item] for item in purchased_items if item in self.items.keys()]
		print(f"Subtotal: ${format(sum(bill), fSpec)}")
		return sum(bill)
		
class Franchise:
	def __init__(self, address, menus):
		self.address = address
		self.menus = menus
	
	def __str__(self):
		return self.address['Street']
	
	def available_menus(self, time):
		global Menus
		available_menus = []
		for menu in Menus:
			if time >= menu.start_time and time <= menu.end_time:
				available_menus.append(menu.name)
		return available_menus
		
class Business:
	def __init__(self, name, franchises):
		self.name = name
		self.franchises = []

def init_brunch_menu():
	Brunch_Items = {
		'pancakes': 7.50,
		'waffles': 9.00,
		'burger': 11.00,
		'home fries': 4.50,
		'coffee': 1.50,
		'espresso': 3.00,
		'tea': 1.00,
		'mimosa': 10.50,
		'orange juice': 3.50}
	return Menu("Brunch", Brunch_Items, time(11, 0), time(16, 0))

def init_earlybird_menu():
	EarlyBird_Items = {
		'salumeria plate': 8.00, 
		'salad and breadsticks (serves 2, no refills)': 14.00, 
		'pizza with quattro formaggi': 9.00, 
		'duck ragu': 17.50, 
		'mushroom ravioli (vegan)': 13.50, 
		'coffee': 1.50, 'espresso': 3.00}
	return Menu("Early Bird", EarlyBird_Items, time(15, 0), time(18, 0))

def init_dinner_menu():
	Dinner_Items = {
		'crostini with eggplant caponata': 13.00,
		'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
		'duck ragu': 19.50,
		'mushroom ravioli (vegan)': 13.50,
		'coffee': 2.00,
		'espresso': 3.00}
	return Menu("Dinner", Dinner_Items, time(17, 0),  time(23, 0))

def init_kids_menu():
	Kids_Items = {
		'chicken nuggets': 6.50,
		'fusilli with wild mushrooms': 12.00,
		'apple juice': 3.00}
	return Menu("Kids", Kids_Items, time(11, 0), time(21, 0))

def init_menus():
	global Brunch
	Brunch = init_brunch_menu()
	global EarlyBird
	EarlyBird = init_earlybird_menu()
	global Dinner
	Dinner = init_dinner_menu()
	global Kids
	Kids = init_kids_menu()
	global Menus
	Menus = [Brunch, EarlyBird, Dinner, Kids]
	
def init_arepa_menu():
	Arepa_Items = {
		'arepa pabellon': 7.00,
		'pernil arepa': 8.50,
		'guayanes arepa': 8.00,
		'jamon arepa': 7.50}
	return Menu("Arepas", Arepa_Items, time(10, 0), time(20, 0))

def print_menus():
	global Menus
	for menu in Menus:
		print(menu.__str__())
		print(Brunch.__repr__())

def subtotal(order, menu):
	return menu.calculate_bill(order)

init_menus()
print_menus()

print(Brunch.start_time.strftime("%H:%M"))
print(Brunch.end_time.strftime("%H:%M"))

Brunch_Purchase = ["pancakes", "home fries", "coffee"]
EarlyBird_Purchase = ["salumeria plate", "mushroom ravioli (vegan)"]
Brunch_Bill = subtotal(Brunch_Purchase, Brunch)
EarlyBird_Bill = subtotal(EarlyBird_Purchase, EarlyBird)

Flagship_Address = {'Street': "1232 West End Road"}
New_Installment_Address = {'Street': "12 East Mulberry Street"}
Flagship_Store = Franchise(Flagship_Address, Menus)
New_Installment = Franchise(New_Installment_Address, Menus)

print(Flagship_Store.__str__())
print(New_Installment.__str__())

for menu in Flagship_Store.available_menus(time(12, 0)):
	print(menu)
	
for menu in Flagship_Store.available_menus(time(17, 0)):
	print(menu)

for menu in Flagship_Store.available_menus(time(16, 0)):
	print(menu)

BastaFazoolin = Business("Basta Fazoolin' with my Heart", [Flagship_Store, New_Installment])

Arepas = init_arepa_menu()
Arepa_Address = {'Street': "189 Fitzgerald Avenue"}
Arepas_Place = Franchise(Arepa_Address, Arepas)
TakeaRepa = Business("Take a'Repa", Arepas_Place)

