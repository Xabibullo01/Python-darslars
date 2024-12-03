import asyncio

async def prepare_coffee(coffee_type: str, with_milk: bool, preparing_time: int) -> str:
    milk_status = "with milk" if with_milk else "without milk"
    print(f"Starting to prepare {coffee_type} ({milk_status}), this will take {preparing_time} seconds.")
    await asyncio.sleep(preparing_time)
    result = f"{coffee_type} ({milk_status}) is ready!"
    print(result)
    return result


async def main():
    coffee_orders = [
        ("Cappuccino", True, 3),
        ("Espresso", False, 5),
        ("Latte", True, 2),
        ("Americano", False, 4),
        ("Mocha", True, 1),
        ("Macchiato", False, 3),
        ("Flat White", True, 2)
    ]
    
    print("Welcome to the Coffee Shop! Preparing your orders...\n")
    
    tasks = [prepare_coffee(coffee, with_milk, time) for coffee, with_milk, time in coffee_orders]
    prepared_coffees = await asyncio.gather(*tasks)
    
    print("\nAll coffees are ready!")
    for coffee in prepared_coffees:
        print(coffee)

if __name__ == "__main__":
    asyncio.run(main())



