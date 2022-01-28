import random
from datetime import datetime 

def my_func(lista):
    items = []
    for i in lista:
        items.append(i+1)
    return items


def my_gen(lista):
    for i in lista:
        yield i+1

randomlist = random.sample(range(1, 5000001), 5000000)
start = datetime.now()
my_gen(randomlist)
end = datetime.now()

print (end - start)