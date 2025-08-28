from concurrent.futures import ThreadPoolExecutor
from time import sleep

def even_or_odd(n):
    sleep(1)  # Simulate work
    return f"{n} is EVEN" if n % 2 == 0 else f"{n} is ODD"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(even_or_odd, numbers)

for res in results:
    print(res)

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

def square(n):
    sleep(1)
    return n * n

numbers = [1, 2, 3, 4, 5]
futures = []

with ThreadPoolExecutor(max_workers=3) as executor:
    for num in numbers:
        futures.append(executor.submit(square, num))
    
    for future in as_completed(futures):
        print(future.result())
