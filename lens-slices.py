#!/usr/bin/env python3

#Len's Slices
#Charles Murray
#ITP270

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms" ]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_pizzas = prices.count(2)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]]

print(*pizza_and_prices, sep="\n")

sorted_list = sorted(pizza_and_prices, key=lambda row: (row[0], row[1]))
print("\n")
print(*sorted_list, sep="\n")

cheapest_pizza = sorted_list[0]
priciest_pizza = sorted_list[-1]
sorted_list.remove(sorted_list[-1])
sorted_list.append([2.5, "peppers"])
sorted_list.sort(key=lambda row: (row[0], row[1]))
three_cheapest=sorted_list[:3]
print("\n", *three_cheapest, sep="\n")

