
best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "25$ Apple Gift Card - Prepaid Card",
        "price": 25.00,
        "department": "Gift Cards",
        "description": "Prepaid card redeemable at App Store and other Apple retail locations."
    },
    {
        "name": "Apple AirPods Pro 2nd Generation",
        "price": 249.00,
        "department": "Headphones",
        "description": "Wireless earbuds with active noise cancellation and superior sound quality."
    },
    {
        "name": "Dell XPS 13 Laptop",
        "price": 999.99,
        "department": "Computers",
        "description": "13-inch laptop with InfinityEdge display, Intel i7 processor, and 16GB RAM."
    },
    {
        "name": "Iphone 16 Pro Max",
        "price": 1099.00,
        "department": "Smartphones",
        "description": "6.7-inch display, A15 Bionic chip, Pro camera system with LiDAR scanner."
    },
    {
        "name": "Google Nest Thermostat",
        "price": 129.99,
        "department": "Smart Home",
        "description": "Smart thermostat with energy-saving features and voice control compatibility."
    },
    {
        "name": "Sony WH-1000XM5 Headphones",
        "price": 349.99,
        "department": "Headphones",
        "description": "Industry-leading noise cancellation and long battery life."
    },
    {
        "name": "Kindle Paperwhite (11th Gen)",
        "price": 139.99,
        "department": "E-readers",
        "description": "Waterproof e-reader with high-resolution display and adjustable warm light."
    },
    {
        "name": "PlayStation 5 Console",
        "price": 499.99,
        "department": "Gaming",
        "description": "Next-gen console with ultra-high speed SSD and immersive gameplay."
    },
    {
        "name": "Instant Pot Duo 7-in-1",
        "price": 89.99,
        "department": "Kitchen",
        "description": "Multi-use programmable pressure cooker that replaces multiple appliances."
    }
]

print("best buy items")
print("items available:")
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])

choice = int(input("enter the number of item: "))
selected_item = best_buy_items[choice]
print("selected this item:", selected_item["name"])

cart = []
total_price = 0
shopping = True

while shopping:
    print("available items: ")
    for i, item in enumerate(best_buy_items):
        print(i, ":", item["name"], "- $", item["price"])

    choice = int(input("enter the number of items: "))
    selected_item = best_buy_items[choice]
    cart.append(selected_item)
    total_price += selected_item["price"]
    
    print("added to cart:", selected_item["name"])

    continue_shopping = input("do you want to continue shopping?: ").lower()
    if continue_shopping != "yes":
        shopping = False

print("your shopping cart:")
for item in cart:
    print("-", item["name"], "- $", item["price"])
print("total price: $", total_price)