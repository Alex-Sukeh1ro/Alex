class Home:
    """This class simplify code, it is used to create examples of different homes.
    Attributes:
        color(str): color of home;
        number_rooms(int): the number of rooms in home
        kind(str): the kind of home
        name(str): the name of home
        price(str): price of home"""
    def __init__(self, color: str, number_rooms: int, kind: str, name: str, price: str):
        self.color = color
        self.number_rooms = number_rooms
        self.kind = kind
        self.name = name
        self.price = price

    def give_home(self):
        """This gives to client the best variant(name of home and price of it)"""
        print('You are lucky! This variant is the best for you: ' + self.name + ', it costs' + self.price)


Home_1 = Home('green', 5, 'house', 'beautiful house on the seaside', ' 14000$')
Home_2 = Home('black', 6, 'house', 'large house in the mountains', ' 16000$')
Home_3 = Home('blue', 3, 'flat', 'flat for typical family with blue wallpaper', ' 5000$')
Home_4 = Home('pink', 5, 'flat', 'penthouse for incendiary parties', ' 9000$')
Home_5 = Home('green', 3, 'flat', 'flat for typical family with green wallpaper', ' 5000$')

HOMES = [Home_1, Home_2, Home_3, Home_4, Home_5]

