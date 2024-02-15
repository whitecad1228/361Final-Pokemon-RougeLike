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
    _currentPokemon = 0
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def addPokemon(self, pokeNum):
        pokemon = Pokemon(pokeNum)
        self._pokemon.append(pokemon)

    def getPokemon(self):
        return self._pokemon

    def getCurrentPokemon(self):
        return self._pokemon[self._currentPokemon]

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

    def getHealth(self):
        return self._stats["hp"]


class Game():
    _textSpeed = 0.5
    _tutorial = True
    _map = ['G','G','T','C','G','S','T','G','G','C','B']
    _mapDict = {
        "G" : "wild pokemon",
        "T" : "Trainer",
        "C" : "Pokemon Center",
        "S" : "Poke Mart",
        "B" : "Gym Battle"
    }
    _step = 0
    _player = Player()
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
        self._player.setName(name)
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
                    self._player.addPokemon(pokeNum)

            elif userInput == "2":
                print("1.[Chikorita, the grass type pokemon]")
                print("2.[Cyndaquil, the fire type pokemon]")
                print("3.[Totodile, the water type pokemon]")
                pokemonChoice = input("Choice:")
                if pokemonChoice.isnumeric():
                    pokeNum = int(pokemonChoice) + (3 * (int(pokemonChoice) - 1) + 151)
                    self._player.addPokemon(pokeNum)
            else:
                print("not a valid input")
        pokemon = self._player.getPokemon()
        print(self._player.getName() + " " + pokemon[0].getName() + " " + pokemon[0].getAbility())
        print(pokemon[0].getStats())
        self.mapArea()

    def mapArea(self):
        print("Your first match up is a " + self._mapDict[self._map[self._step]])
        self.battle()

    def battle(self):
        battle = self._map[self._step]
        if battle == "G":
            if self._tutorial:
                print("Welcome to your first battle.")
                time.sleep(self._textSpeed)
                print("When you are in a battle you will have four options, fight, bag, run or pokemon.")
                time.sleep(self._textSpeed)
                print("To fight you click fight and it will give you up to four options of moves.")
                time.sleep(self._textSpeed)
                print("Next to each move will be its Name, its type, and its PP or Power Points, which is how many times you can use it.")
                time.sleep(self._textSpeed)
                print("In your bag you will have access to items that you either bought in stores or picked up on the road.")
                time.sleep(self._textSpeed)
                print("Run allows you to escape from only a wild Pokemon battle but is unadvised.")
                time.sleep(self._textSpeed)
                print("Pokemon will gain valuable experience and money from wining a pokemon battle.")
                time.sleep(self._textSpeed)
                print("Lastly pokemon will give you the option of taking a turn to change your pokemon.")
                time.sleep(self._textSpeed)
                print("To start your first battle i will provide you with some pokeballs. Pokeballs will avalible in the items section.")
                time.sleep(self._textSpeed)
            opponent = Pokemon(17)
            print("***************************************************************************************************")
            print(opponent.getName())
            print("Health:" + opponent.getHealth())
            print("")
            print("")
            print("")
            print(self._player.getCurrentPokemon().getName())
            print("Health:" + self._player.getCurrentPokemon().getHealth())
            print("***************************************************************************************************")
            print("1.[Fight]")
            print("2.[Bag]")
            print("3.[run]")
            print("4.[Pokemon]")
            choice = input("Choice:")
        if battle == "T":
            print("Welcome to your first trainer battle.")
            print("When you are in a battle you will be able ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.runGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
