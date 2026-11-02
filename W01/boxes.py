import math

items = int(input("What is the number of manufactured items? "))
items_per_box = int(input("How many items will be packed per box? "))

box_total = math.ceil(items / items_per_box)

print(f"For {items} items, packing {items_per_box} items in each box, you will need {box_total} boxes.")