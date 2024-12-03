import asyncio

async def fetch_data(name: str, delay: int) -> dict:
    print(f"Fetching data from {name}, it will take {delay} seconds...")
    await asyncio.sleep(delay)
    data = {name: f"Data from {name}"}
    print(f"Data fetched from {name}")
    return data

async def process_data(data: dict):
    print(f"Processing data: {data}...")
    await asyncio.sleep(2)
    print(f"Processed data: {data}")

apis = {
    "Review Api": 2,
    "User Api": 5,
    "Product Api": 4,
    "Owner Api": 3,
    "Orders Api": 6
}

async def main():
    print("Starting to fetch and process data from APIs...\n")
    
    fetch_tasks = [fetch_data(name, delay) for name, delay in apis.items()]
    fetched_data = await asyncio.gather(*fetch_tasks)

    process_tasks = [process_data(data) for data in fetched_data]
    await asyncio.gather(*process_tasks)

    print("\nAll data fetched and processed!")

if __name__ == "__main__":
    asyncio.run(main())


