def print_practice():
    print("A 'single quote' inside a double quote")
    print('A "double quote" inside a single quote')
    print("Alternatively you can just \"escape\" the quote")
    print(len(input()))


def swap_variables():
    # There are two variables, a and b from input
    a = input()
    b = input()
    c = a
    a = b
    b = c
    print("a: " + a)
    print("b: " + b)


def band_name_generator():
    print("Welcome to the Band Name Generator.\n")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print("Your band name could be " + city_name + " " + pet_name)
