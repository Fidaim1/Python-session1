class CurrencyConverter:
    admin = False
    konvertimi = 1.2
    def register (self):
        username = input ('Username: ')
        self.username = username
        retry = True
        while retry:
            password = input ('Password: ')
            any_upper = ["wwww" for element in password if element .isupper()]
            any_digit = ['haha' for element in password if element .isdigit()]
            if any_upper and any_digit :
                print ('nice')
                retry = False      
            else:
                print ('not okey, try again')
        self.password = password
        return {'username': self.username, 'password': self.password, 'admin': False}
    
    def first_admin (self, user):
        user['admin'] = True
        self.admin = True

    def convert (self, vlera):
        return vlera*self.konvertimi
    
    def change_conv (self):
        if self.admin:
            self.konvertimi = 3
        else:
            print ('Ti nuk je admin')


user_1 = CurrencyConverter()

first_user = user_1.register()
print (first_user)
print ('a je admin', user_1.admin)

print (user_1.first_admin(first_user))
print ('a je admin', user_1.admin)

print ('para', user_1.convert(5))
print (user_1.change_conv())
print ('pass',user_1.convert(5))


