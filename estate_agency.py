from custom_expection import NoHomeError  # Provide for exceptions
from all_homes import Home, HOMES  # There are all kind of homes for c


print(f'We are happy to see you in our estate agency! Here you can choose your home')


COLOR = input('Please choose color for your home:')
NUMBER_ROOMS = int(input('Please choose number of rooms for your home:'))
KIND = input('Please choose kind for your home:')


try:
    for home in HOMES:
        if COLOR == home.color and NUMBER_ROOMS == home.number_rooms and KIND == home.kind:
            home.give_home()
    else:
        raise NoHomeError
except NoHomeError:
    print('There are no home with such criteria')
