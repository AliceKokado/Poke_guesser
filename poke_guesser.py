"""
POKE-GUESSER game by Alice Kokado
"""


import requests
import webbrowser
import random


api_url = "https://pokeapi.co/api/v2/pokemon/"  # link to the api


# function that returns the sprite of pokemon using its name
def get_pokemon_sprite(name):
    search = api_url + name
    response = requests.get(search)
    return response.json()["sprites"]["front_default"]


# function that returns the name of pokemon using its pokedex number
def get_pokemon_name(number):
    search = api_url + number
    response = requests.get(search)
    return response.json()["name"]


if __name__ == '__main__':
    while True:
        rand_pokemon = str(random.randint(1, 151))  # generate a random number for a random pokemon. currently Kanto
        print(get_pokemon_sprite(rand_pokemon))  # prints the link to the pokemon sprite
        pokemon_name = get_pokemon_name(rand_pokemon)  # set the name of the pokemon

        # open link in web browser. comment this out if you don't want it
        webbrowser.open('{}'.format(get_pokemon_sprite(rand_pokemon)))

        # Guessing part
        guess = input("What pokemon is this?: ")
        if guess.lower() == pokemon_name:
            print("THAT IS CORRECT!")
        else:
            print("WRONG! it was {}".format(pokemon_name))
