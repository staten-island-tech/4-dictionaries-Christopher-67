
best_buy_items = [
{
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
},
{
    "name":"25$ apple gift card\" Prepaid Card",
    "price": 25.00,
    "department": "Gift Cards",
    "description": "Prepaid card redeemable at app store and other apple retail locations"
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
}
]


for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
