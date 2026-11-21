pizza_prices = {
    "Cheese Pizza": 11.99,
    "Pepperoni Pizza": 14.99,
    "BBQ Chicken Pizza": 13.99,
    "Hawaiian Pizza": 12.99,
    "Meat Pizza": 16.99
}

def update_prices(pizza_prices):
    new_prices = {}

    for pizza, price in pizza_prices.items():
        new_prices[pizza] = round(price * 1.15, 2)

    return new_prices

print(update_prices(pizza_prices))