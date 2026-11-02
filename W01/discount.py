import datetime
from datetime import datetime
day = datetime.now().weekday()

subtotal = 0
quantity = 1
while quantity != 0:
    price = float(input('Product price: $'))
    quantity = int(input('Product quantity (if finished put 0): '))
    subtotal = subtotal + (price * quantity)

if day == 1 or day == 2:
    if subtotal >= 50:
        subtotal *= 0.9
        print('10% discount applied')
    else:
        print(f'Spend ${(50 - subtotal):.2f} more to apply 10% discount')

print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales tax: ${(subtotal * .06):.2f}')
subtotal *= 1.06
print(f'Total: ${subtotal:.2f}')
