
# def example(items:str)->str:
#     print(items)
#     items=items + "pdp"
#     return items



import asyncio

# async def async_example(number: int)-> str:
#     print(type(number))
#     await asyncio.sleep(0.5)
#     return str(number)


# async def main():
#     print("Hello...")
#     await async_example(10)
#     print("...World")



# if __name__ == '__main__':
#     asyncio.run(main(), debug=True)


async def async_example(number: int)-> str:
    print(f"starting example function {number}")
    await asyncio.sleep(2)
    print(f"Finished example function {number}")


async def main():
    print("Hello...")
    tasks = [async_example(i) for i in range(1,6)]
    await asyncio.gather(*tasks)
    print("...World")



if __name__ == '__main__':
    asyncio.run(main(), debug=True)


