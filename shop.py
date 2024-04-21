# Define a dictionary of barcodes and their corresponding items and prices
inventory = {
    '1234567890': {'item': 'apple', 'price': 0.5},
    '2345678901': {'item': 'banana', 'price': 0.25},
    '3456789012': {'item': 'orange', 'price': 0.75},
    '4567890123': {'item': 'grape', 'price': 1.0},
    '5678901234': {'item': 'watermelon', 'price': 5.0}
}

# Initialize an empty list to store the items and prices
items = []

# Ask for the barcode number, return the item and the price, and ask for the number of items
while True:
    barcode = input('Please enter the barcode number (or "done" to finish): ')
    if barcode == 'done':
        break
    elif barcode not in inventory:
        print('Invalid barcode number')
    else:
        item = inventory[barcode]['item']
        price = inventory[barcode]['price']
        print(f'{item}: ${price:.2f}')
        num_items = int(input('Please enter the number of items: '))
        items.extend([price] * num_items)

# Calculate the total price of all the items
total = sum(items)
print(f'Total price: ${total:.2f}')

