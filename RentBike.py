class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def DisplayBikes(self):
        print("total bikes", self.stock)
    def rentForBike(self,q):

        if q<=0:
            print("enter the positive value or grather tahn zero ")
        elif q>self.stock:
            print("enter the value (less then stock)")
        else:
            print("total prices",q*100)
            print("total bikes",self.stock)
while True:
    uc=int(input('''1 diaplay stock
    2 rent a bike 
    3 exit '''))
    if uc==1:
        obj=BikeShop(100)
        obj.DisplayBikes()
    elif uc==2:
        n=int(input("enter the qty:---"))
        obj.rentForBike(n)
    else:
        break



