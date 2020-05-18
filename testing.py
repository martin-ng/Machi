import time
import asyncio


# def count():
# print("One")
# time.sleep(5)
# print("Two")
# print('Three')


async def count():
    print("One")
    await asyncio.sleep(2)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    main()
