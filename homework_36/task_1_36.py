import asyncio


async def fibonacci(n):
    if n <= 1:
        return n
    else:
        return await fibonacci(n - 1) + await fibonacci(n - 2)

async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n - 1)

async def square(n):
    return n**2

async def cube(n):
    return n**3

async def main():
    global res
    coroutines = []
    fib = []
    fact = []
    sq = []
    cub = []

    for _ in range(1, 11):
        coroutines.append(asyncio.create_task(fibonacci(_)))
        coroutines.append(asyncio.create_task(factorial(_)))
        coroutines.append(asyncio.create_task(square(_)))
        coroutines.append(asyncio.create_task(cube(_)))
        res = await asyncio.gather(*coroutines)

    for c in range(0, 20, 5):
        fib.append(res[c])
        fact.append(res[c+1])
        sq.append(res[c+2])
        cub.append(res[c+3])

    print(f'fibonacci {fib}')
    print(f'factorial {fact}')
    print(f'square {sq}')
    print(f'cube {cub}')

asyncio.run(main())