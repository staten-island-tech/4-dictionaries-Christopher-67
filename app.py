
best_buy_items = [
{
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55 inch Ultra HD Smart TV with HDR and built in streaming apps."
},
{
    "name": "25$ Apple Gift Card (Prepaid)",
    "price": 25.00,
    "department": "Gift Cards",
    "description": "Prepaid card redeemable at Apple Store and other Apple retail locations."
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
    "description": "13 inch laptop with InfinityEdge display, Intel i7 processor, and 16GB RAM."
},
{
    "name": "Iphone 16 Pro Max",
    "price": 1099.00,
    "department": "Smartphones",
    "description": "6.7 inch display, A15 Bionic chip, Pro camera system with LiDAR scanner."
},
{
    "name": "Playstation 5",
    "price": 499.00,
    "department": "Gaming",
    "description": "Gaming console with controller, games not included."
},
{
    "name": "Nintendo Switch 2",
    "price": 399.00,
    "department": "Gaming",
    "description": "Handheld gaming console. Two controllers included."
},
{
    "name": "Mario kart World",
    "price": 70.00,
    "department": "Gaming",
    "description": "Physical copy of a game that can be played on the switch"
},
{
    "name": "Roblox Gift Card",
    "price": 100.00,
    "department": "Gift Cards",
    "description": "Prepaid Card redeemable on the app or website."
},
{
    "name": "",
    "price": 1099.00,
    "department": "",
    "description": ""
},
{
    "name": "",
    "price": 1099.00,
    "department": "",
    "description": ""
},
]

for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
