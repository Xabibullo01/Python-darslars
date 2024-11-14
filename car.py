car_types = ["Sedan", "Hatchback", "Coupe", "Minivan", "SUV"]
print("""
1. Sedan
2. Hatchback
3. Coupe 
4. Minivan
5. SUV
""")

while True:
    try:
        car_type = int(input("Moshina turini tanlang: "))
        if 1 <= car_type <= len(car_types):
            selected_type = car_type - 1  
            break
        else:
            print("Bunday turdagi avtomobil mavjud emas.")
    except ValueError:
        print("Iltimos, raqam kiriting.")

car_colors = ["White", "Black", "Gray"]
print("""
1. White
2. Black
3. Gray
""")

while True:
    try:
        car_color = int(input("Rang tanlang: "))
        if 1 <= car_color <= len(car_colors):
            selected_color = car_color - 1 
            break
        else:
            print("Bunday rang mavjud emas.")
    except ValueError:
        print("Iltimos, raqam kiriting.")

def return_price(color_index, type_index, car_types, car_colors):
    base_price = 20000
    type_price_modifier = 1000 * (type_index + 1)
    color_price_modifier = 500 * (color_index + 1)
    total_price = base_price + type_price_modifier + color_price_modifier
    return f"{car_colors[color_index]} {car_types[type_index]}", total_price

car_description, price = return_price(selected_color, selected_type, car_types, car_colors)
print(f"Tanlangan avtomobil: {car_description}\nNarxi: ${price}")
