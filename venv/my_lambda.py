data = lambda a: a + 1

a = [1,2,3,4]

def my_func(a):
    b = []
    for item in a:
        b.append(item*item)
    return b

# def my_funcc(a):
#     b = []
#     for item in a:
#         b.append(item*item)
#     yield b


def my_funcc(a):
    for item in a:
       yield(item*item)
    

print(my_func(a))
my_gen = my_funcc(a)
print(list(my_funcc(a)))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))