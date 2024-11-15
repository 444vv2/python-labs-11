class Conference:
    name = None
    num_of_par = None
    ticket_price = None
    city = None

    def __init__(self, name, num_of_par, ticket_price, city):
        self.__name = name
        self.__num_of_par = num_of_par
        self.__ticket_price = ticket_price
        self.__city = city

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_num_of_par(self):
        return self.__num_of_par
    
    def set_num_of_par(self, num_of_par):
        self.__num_of_par = num_of_par

    def get_ticket_price(self):
        return self.__ticket_price
    
    def set_ticket(self, ticket_price):
        self.__ticket_price = ticket_price

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def __str__(self):
        return (f"Conference(Name: {self.__name}, Number of participants: {self.__num_of_par}, "
                f"Ticket Price: {self.__ticket_price}, City: {self.__city})")

    def __repr__(self):
        return (f"Conference(name='{self.__name}', num_of_pat='{self.__num_of_par}', "
                f"ticket_price='{self.__ticket_price}',city='{self.__city}')")

    def __del__(self):
        print("Deleted")

def main():
    conf1 = Conference('IT_arena', 5000 , "147$", "Lviv")
    conf2 = Conference('LXХІІІ Міжнародна інтернет — конференція', 1500, '30$',
                       'Vancouver')
    conf3 = Conference('III Міжнародна науково-практична конференція', 1000 , "10$" ,
                       'London')

    print(conf1)
    print(conf2)
    print(conf3)
    print(repr(conf1))
    print(repr(conf2))
    print(repr(conf3))

if __name__ == '__main__':
    main()
print("Done")
