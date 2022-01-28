# from random import randint
# my_random_number = randint (0,10)
# print(my_random_number)
# for i in range (10):
#     unser_input = input ('Shkruaj nje numer:')
#     try:
#         if int (unser_input) == my_random_number:
#             print ('Bravo')
#             break
#         else:
#             print ('Sorry')
#     except Exception as my_error:
#         print ('Ju lutem perdorni vetem numra te plot nga 0 deri 10')


# lista = [1,2,3]
# try:
#     print (lista[2])
# except Exception as my_error:
#     print ('NONONO')
# else:
#     print ('try eshte ekzekutu me sukses')
# finally:
#     print('jena lodh me lista')


my_dict = {'emri':'hello','mbiemri':'world'}
print (my_dict['emri'])
try:
    print (my_dict['mbiemri'])
except KeyError as err:
    print ('uups',err)

print ('mesazh shum i mire')

print (my_dict.get('world'))
