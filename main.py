"""
This is a test version of Pokelike, a Pokemon rouge like based on the two games Pokemon and slay the spire
combing the two concepts. this is a fully texted based game for the time being.

"""
import time
import csv
import random
import re
import json

"""
Class: Parser
used for parsing the two types of data files that we have, both .csv and .json
getStats uses the .csv 
getPotentialMoves uses the .json

could be changed to just def parseCSV but that is for later
"""
class Parser:

    def getStats(self, pokedexNum):
        with open('pokemon_database.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #one for start at one, one for titles
            line_count = 1
            for row in csv_reader:
                if line_count == pokedexNum:
                    return row
                else:
                    line_count += 1
    def getPotentialMoves(self, pokeNum):
        f = open('movesByLevel.json')
        data = json.load(f)
        #print(data[pokeNum - 1])
        return data[pokeNum - 1]["moves"]

"""
Class: Player
contains the player class containing basic info like inventory, pokemon and name


"""
class Player:
    _name = ""
    _pokemon = []
    _items = {}
    _currentPokemon = 0

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def addPokemon(self, pokemon):
        self._pokemon.append(pokemon)

    def getPokemon(self):
        return self._pokemon

    #used in battle for the pokemon out in battle
    def getCurrentPokemon(self):
        return self._pokemon[self._currentPokemon]


"""
Class: Pokemon
used to hold all the information regarding one pokemon. contains a lot of info like stats obtained from the csv file,
using the parser, potential moves again obtained from the parser, level of the pokemon and current moves.

will need function to level up, check evolutions and learned moves on level up, possibly function to check damage or 
deal damage, add moves for opponents.


"""
class Pokemon:

    _stats = {}
    _moves = []
    _level = 1
    _potential_moves = []
    def __init__(self, pokedexNum, level):
        print(pokedexNum)
        parser = Parser()
        #gets and set stats via parser
        self._stats = parser.getStats(pokedexNum)
        # gets and set potential moves via parser
        self._potential_moves = parser.getPotentialMoves(pokedexNum)
        self._level = level

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
    def getLevel(self):
        return self._level
    def setLevel(self, level):
        self._level = level



"""
Class: Game
this is the class that contains overall game information like settings such as _textSpeed, _tutorial and other things
like the map and steps into the map.

all the text could be put in a service of some sort, map functionality needs to be added - slay the spire type, 
exit functionality needs to be added to allow for exiting at any point(?), game loop needs to be created, 

intro -> map -> battle/center/shop/ -> check death or levels + evolutions -> map -> continue

battle options need to be created, opposition pokemon and move selection need to be made, damage calculation needs to
be made could be calculated in pokemon class, more options could be added for inclusivity, more options for cycles.



"""
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

    #Runs the inital main menu screen, could be updated to reflect that
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

    #runs the tutorial and begining of new game, may need to be changed to the setting
    #include tutorial, getting choice like starter pokemon,
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

        #starter pokemon
        if userInput.isnumeric():
            if userInput == "0":
                return
            elif userInput == "1":
                print("Great choice! please make your choice.")
                print("1.[Bulbasaur, the grass type pokemon]")
                print("2.[Charmander, the fire type pokemon]")
                print("3.[Squirtle, the water type pokemon]")
                pokemonChoice = input("Choice:")
                if pokemonChoice.isnumeric():
                    pokeNum = int(pokemonChoice) + (2 * (int(pokemonChoice) - 1))
                    print(pokeNum)
                    pokemon = Pokemon(pokeNum, 5)
                    self._player.addPokemon(pokemon)

            elif userInput == "2":
                print("1.[Chikorita, the grass type pokemon]")
                print("2.[Cyndaquil, the fire type pokemon]")
                print("3.[Totodile, the water type pokemon]")
                pokemonChoice = input("Choice:")
                if pokemonChoice.isnumeric():
                    pokeNum = int(pokemonChoice) + (2 * (int(pokemonChoice) - 1) + 151)
                    pokemon = Pokemon(pokeNum, 5)
                    self._player.addPokemon(pokemon)
            else:
                print("not a valid input")
        self.mapArea()

    #call the Map area will be used for displaying the map, and getting the players choice on direction
    def mapArea(self):
        print("Your first match up is a " + self._mapDict[self._map[self._step]])
        self.battle()

    # runs the battle functionality currently could be updated to run all choices or reduced to only contain the
    # battle or wild pokemon encounter. Contains the tutorial section for the wild battle, may need to be correctly
    # attached to the tutorial option. could also use a system for creating opponents that are appropriate to level.
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
            opponent = Pokemon(17, 5)
            while opponent.getHealth() > 0:
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
                if choice.isnumeric():
                    if choice == "0":
                        return
                    elif choice == "1":
                        print("choose a move:")
                        # print("1.[" + )
                        # print("2.[" + )
                        # print("3.[" + )
                        # print("4.[" + )
                    elif choice == "2":
                        pass
                    elif choice == "3":
                        pass
                    elif choice == "4":
                        pass
                    else:
                        pass
        if battle == "T":
            print("Welcome to your first trainer battle.")
            print("When you are in a battle you will be able ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.runGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
