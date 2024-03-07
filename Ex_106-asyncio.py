import asyncio
from random import randrange


async def generate_random():
    await asyncio.sleep(5)
    rand = randrange(5, 10)
    print(f'Рандомное число: {rand}')
    return rand


async def mult_by_2():
    number = await generate_random()
    result = number * 2
    print(f'Результат: {result}')
    return result


async def print1():
    print(1)


async def print2():
    await asyncio.sleep(10)
    print(2)


async def main():
    task2 = asyncio.create_task(mult_by_2())
    task3 = asyncio.create_task(print1())
    task4 = asyncio.create_task(print2())
    await asyncio.gather(task2, task3, task4)


asyncio.run(main())
