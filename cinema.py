class Hall:    
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
hall = Hall (" A", 40)
print ( hall )
hall . set_seats ( -5)
print ( hall . get_seats () )
hall . set_seats (150)
print ( hall . get_seats () )
hall . set_seats (0)
print ( hall )
  
        
    