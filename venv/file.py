# my_new_file = open ('loreta.txt','w')
# my_new_file.write ('hello Loreta')
# # my_new_file.close()
# my_new_file_read = open('loreta.txt','r')
# my_new_file_read.read()

with open ('loreta.txt','r')as my_file:
    print (my_file.read())

