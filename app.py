item = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}
item = {
    "name": "BBQ Chips\" Party Size",
    "price": 12.49,
    "department": "Snacks",
    "description": "Potato chips coated with a smoky barbecue seasoning."
}
item = {
    "name": "25$ apple gift card\" Prepaid Card",
    "price": 25.00,
    "department": "Gift Cards",
    "description": "Prepaid card redeemable at app store and other apple retail locations"
}
item = {
    "name": "Arizona iced tea\" Large can",
    "price": 0.99,
    "department": "Beverages",
    "description": "23 fl oz can of Arizona Brand Iced Tea with Lemon flavor."
}
item = {
    "name": "Milk\" 1 Gallon",
    "price": 3.99,
    "department": "Dairy",
    "description": "1 gallon of whole milk."
}

for index, item in enumerate(Walmart_items):
    print(index, ":", item["name"])
    Walmart_items = []