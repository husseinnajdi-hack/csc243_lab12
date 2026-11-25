class hall:    
    def __init__ (self,name,seats):
        self.name = name
        self.__seats=int(seats)
    def get_seats(self):
        return self.__seats
    def __has_seats(self):
        return self.__seats>0 
    def has_seats(self):
        return self.__has_seats()
    def set_seats(self,n):
        
        if n>100 or n<0:
            print("Invalid seats")
        else:
            self.__seats=n
    def __str__(self):
        n=self.name
        s=self.__seats
        return (f"hall {n}:{s} seats")
class guest:
    def __init__(self,name,tickets):
        self.name=name
        self.__tickets=int(tickets)
    def get_tickets(self):
        return self.__tickets
    def add_tickets(self,n):
        if n>0:
            self.__tickets+=n
        else:
            print("Invalid amount")
         
    def __str__(self):
        n=self.name
        t=self.__tickets
        return(f"{n}: {t} tickets")
def reserve(hall,guest,n):
    if hall.has_seats():
        guest.add_tickets(n)
    else:
        print("Hall is full")
hall=hall("A",0)
maya=guest("maya",11)
print ( hall . has_seats () )
reserve ( hall , maya , 5)
print ( maya . get_tickets () )
hall . set_seats (40)
reserve ( hall , maya , 5)
print ( maya )
print ( hall )       