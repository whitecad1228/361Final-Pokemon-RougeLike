"""
This is a test version of Pokelike, a Pokemon rouge like based on the two games Pokemon and slay the spire
combing the two concepts. this is a fully texted based game for the time being.

"""
import time
import csv
import random
import re

class Player:
    _name = ""
    _pokemon = []
    _items = {}

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def addPokemon(self, pokeNum):
        pokemon = Pokemon(pokeNum)
        self._pokemon.append(pokemon)

    def getPokemon(self):
        return self._pokemon

class Pokemon:

    _stats = {}

    def __init__(self, pokedexNum):
        print(pokedexNum)
        with open('pokemon_database.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #one for start at one, one for titles
            line_count = 2
            for row in csv_reader:
                if line_count == pokedexNum:
                    self._stats = row
                    print(self._stats)
                    line_count += 1
                else:
                    line_count += 1
        # giving them a random ability
        dummyVar = self._stats["abilities"]
        #splits from the list to give a list
        abilities = dummyVar.split(", ")
        listNum = 0
        #takes away the extra stuff like [] and '
        for ability in abilities:
            abilities[listNum] = re.sub(r'[^a-zA-Z ]+', '', ability)
            listNum += 1
        randomNum = random.randint(0, len(abilities) - 1)
        self._stats["abilities"] = abilities[randomNum]

    def getStats(self):
        return self._stats
    def getName(self):
        return self._stats["name"]

    def getAbility(self):
        return self._stats["abilities"]


class Game():
    _textSpeed = 0.5

    def runGame(self):
        quit = False
        while not quit:
            print("Welcome to Pokelike.")
            print("1.[new game]")
            print("2.[Options]")
            print("3.[Achievements]")
            print("4.[quit]")
            userInput = input("Choose an option: ")
            if userInput.isnumeric():
                if userInput == "1":
                    self.newGame()
                elif userInput == "2":
                    print("Unavailable at this time, returning")
                elif userInput == "3":
                    print("Unavailable at this time, returning")
                elif userInput == "4":
                    print("Quiting...")
                    quit = True
                else:
                    print("error, returning to main menu")

    def newGame(self):
        newPlayer = Player()
        #intro:
        print("Welcome to the world of Pokemon, My name is professor Oak but everyone calls me the Pokemon Professor.")
        time.sleep(self._textSpeed)
        print("Before we go any further I'd like to tell you a few things you should Know about this world.")
        time.sleep(self._textSpeed)
        print("This world is widely inhabited by creatures known as Pokemon.")
        time.sleep(self._textSpeed)
        print("We humans live alongside Pokemon as Friends, at other time play together and at other times we work together")
        time.sleep(self._textSpeed)
        print("Some people use their pokemon to battle and develop closer bonds with them, and you are one of them.")
        time.sleep(self._textSpeed)
        print("You are one of our tournament contenders, who will face wild pokemon, wild trainers, and gym leaders.")
        time.sleep(self._textSpeed)
        print("In completion of this Tournament, you will be crowned the champion.")
        time.sleep(self._textSpeed)
        print("But should all of you pokemon faint even once, you will be dropped out of the tournament.")
        time.sleep(self._textSpeed)
        name = input("Now why dont you tell me what your name is?")
        newPlayer.setName(name)
        print(name + "... what a fantastic name.")
        time.sleep(self._textSpeed)
        print(name + " I wish you the best of luck out there.")
        time.sleep(self._textSpeed)
        print("Ohh i forgot, you will also need a pokemon. For the tournament we will provide a pokemon based on your choice")
        time.sleep(self._textSpeed)
        print("1.[Choose 1 of 3 gen 1 starters]")
        print("2.[Choose 1 of 3 gen 2 starters]")
        userInput = input("Choice:")
        if userInput.isnumeric():
            if userInput == "1":
                print("Great choice! please make your choice.")
                print("1.[Bulbasaur, the grass type pokemon]")
                print("2.[Charmander, the fire type pokemon]")
                print("3.[Squirtle, the water type pokemon]")
                pokemonChoice = input("Choice:")
                if pokemonChoice.isnumeric():
                    pokeNum = int(pokemonChoice) + (3 * (int(pokemonChoice) - 1))
                    newPlayer.addPokemon(pokeNum)

            elif userInput == "2":
                print("1.[Chikorita, the grass type pokemon]")
                print("2.[Cyndaquil, the fire type pokemon]")
                print("3.[Totodile, the water type pokemon]")
                pokemonChoice = input("Choice:")
                if pokemonChoice.isnumeric():
                    pokeNum = int(pokemonChoice) + (3 * (int(pokemonChoice) - 1) + 151)
                    newPlayer.addPokemon(pokeNum)
            else:
                print("not a valid input")
        pokemon = newPlayer.getPokemon()
        print(newPlayer.getName() + " " + pokemon[0].getName() + " " + pokemon[0].getAbility())
        print(pokemon[0].getStats())

    def

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.runGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
