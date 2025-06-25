class Mobile:
    def __init__ (self):
        self.__price=0

    def update_price(self,amount):
        if 0<amount<=200:
            self.__price += 200
    def get_price(self):
        print(self.__price)
m1=Mobile()
m1.get_price()
       