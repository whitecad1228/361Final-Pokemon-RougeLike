"""
This is a test version of Pokelike, a Pokemon rouge like based on the two games Pokemon and slay the spire
combing the two concepts. this is a fully texted based game for the time being.

"""
import math
import time
import sys
from Pokemon import Pokemon
import requests
from random import randint
from Map import Map


"""
Class: Player
contains the player class containing basic info like inventory, pokemon and name
"""
class Player:

    def __init__(self):
        self._pokemon = list()
        self._items = {}
        self._name = ""
        self._currentPokemon = 0
        self._bag = [[],[],[],[]]

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

    #used to set current pokemon or in case of traniner will progress to next pokemon
    def setCurrentPokemon(self, num):
        if num == "next":
            self._currentPokemon += 1
        else:
            self._currentPokemon = num
    #gets if there is a pokemon avalible
    def getAvailablePokemon(self):
        available = False
        for i in range(0,len(self._pokemon)):
            if self._pokemon[i].getHealth() > 0:
                available = True
        return available

    def getBag(self):
        return self._bag


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
    #dev
    _devMode = False
    _achievements = True
    #options
    _textSpeed = 0.2
    _intro = True
    _combatTutorial = True
    #game
    _mapDict = {
        "G" : "wild pokemon",
        "T" : "Trainer",
        "C" : "Pokemon Center",
        "S" : "Poke Mart",
        "B" : "Gym Battle"
    }
    _typeDict = {
        "normal": 0,
        "fire": 1,
        "water": 2,
        "electric": 3,
        "grass": 4,
        "ice": 5,
        "fighting": 6,
        "poison": 7,
        "ground": 8,
        "flying": 9,
        "psychic": 10,
        "bug": 11,
        "rock": 12,
        "ghost": 13,
        "dragon": 14,
        "dark": 15,
        "steel": 16
    }
    _typeChart =    [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "0.5", "0", "1", "1","0.5"],
                    ["1", "0.5", "0.5", "1", "2", "2", "1", "1", "1", "1","1", "2", "0.5", "1", "0.5", "1","2"],
                    ["1", "2", "0.5", "1", "0.5", "1", "1", "1", "2", "1","1", "1", "2", "1", "0.5", "1","1"],
                    ["1", "1", "2", "0.5", "0.5", "1", "1", "1", "0", "2","1", "1", "1", "1", "0.5", "1","1"],
                    ["1", "0.5", "2", "1", "0.5", "1", "1", "0.5", "2", "0.5","1", "0.5", "2", "1", "0.5", "1","0.5"],
                    ["1", "0.5", "0.5", "1", "2", "0.5", "1", "1", "2", "2","1", "1", "1", "1", "2", "1","0.5"],
                    ["2", "1", "1", "1", "1", "2", "1", "0.5", "1", "0.5","0.5", "0.5", "2", "0", "1", "2","2"],
                    ["1", "1", "1", "1", "2", "1", "1", "0.5", "0.5", "1","1", "1", "0.5", "0.5", "1", "1","0"],
                    ["1", "2", "1", "2", "0.5", "1", "1", "2", "1", "0","1", "0.5", "2", "1", "1", "1","2"],
                    ["1", "1", "1", "0.5", "2", "1", "2", "1", "1", "1","1", "2", "0.5", "1", "1", "1","0.5"],
                    ["1", "1", "1", "1", "1", "1", "2", "2", "1", "1","0.5", "1", "1", "1", "1", "0","0.5"],
                    ["1", "0.5", "1", "1", "2", "1", "0.5", "0.5", "1", "0.5","2", "1", "1", "0.5", "1", "2","0.5"],
                    ["1", "2", "1", "1", "1", "2", "0.5", "1", "0.5", "2","1", "2", "1", "1", "1", "1","0.5"],
                    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1","2", "1", "1", "2", "1", "0.5","0.5"],
                    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "2", "1","0.5"],
                    ["1", "1", "1", "1", "1", "1", "0.5", "1", "1", "1","2", "1", "1", "2", "1", "0.5","0.5"],
                    ["1", "0.5", "0.5", "0.5", "1", "2", "1", "1", "1", "1","1", "1", "2", "1", "1", "1","0.5"],]
    _player = Player()

    def __init__(self):
        self._map = Map()
        self._map.createMap()

    # may not be necessary needs testing
    def optionsMenu(self):
        print("1.[Go back]")
        print("2.[Quit]")
        userInput = input("Choose an option: ")
        if userInput.isnumeric():
            if userInput == 1:
                return;
            elif userInput == 2:
                print("Exiting... Are you sure.")
                print("1.[Go back]")
                print("2.[Quit]")
                userInput = input("Choose an option: ")
                if userInput.isnumeric():
                    if userInput == 2:
                        sys.exit(0)

                        #self.optionsMenu()
            else:
                print("please enter appropriate value")
                self.optionsMenu()

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
                    if self._achievements:
                        url = 'http://127.0.0.1:5000/achievements'
                        response = requests.get(url)

                        data = response.json()
                        print("Achievements:\r\n")
                        if len(data["achievements"]) > 0:
                            for i in range(0,len(data["achievements"])):
                                print(data["achievements"][i])
                        else:
                            print("No achievements currently.")

                        print("Opponents Defeated:\r\n")
                        if len(data["opponents_defeated"]) > 0:
                            for i in range(0, len(data["opponents_defeated"])):
                                print(data["opponents_defeated"][i])
                        else:
                            print("No opponents defeated currently.")
                    else:
                        print("Unavailable at this time, returning")

                elif userInput == "4":
                    print("Quiting... Are you sure")
                    print("1.[Go back]")
                    print("2.[Quit]")
                    userInput = input("Choose an option: ")
                    if userInput.isnumeric():
                        if userInput == "2":
                            quit = True
                else:
                    print("error, returning to main menu")

    #runs the tutorial and begining of new game, may need to be changed to the setting
    #include tutorial, getting choice like starter pokemon,
    def newGame(self):
        if not self._devMode:
            if self._intro:
                print("To exit at any time enter zero at any input to go to the options menu.")
                time.sleep(self._textSpeed)
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
                if name.isnumeric() and name == "0":
                    return
                else:
                    self._player.setName(name)
                print(name + "... what a fantastic name.")
                time.sleep(self._textSpeed)
                print(name + " I wish you the best of luck out there.")
                time.sleep(self._textSpeed)
                print("Ohh i forgot, you will also need a pokemon. For the tournament we will provide a pokemon based on your choice.")
                time.sleep(self._textSpeed)
            else:
                name = input("what is your name?")
                if name.isnumeric() and name == "0":
                    return
                else:
                    self._player.setName(name)
                print("Choose a pokemon:")
            selectedPokemon = False
            while not selectedPokemon:
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
                        print("4.[Go back]")
                        pokemonChoice = input("Choice:")
                        if pokemonChoice.isnumeric():
                            if pokemonChoice != "4":
                                pokeNum = int(pokemonChoice) + (2 * (int(pokemonChoice) - 1))
                                pokemon = Pokemon(pokeNum, 5)
                                self._player.addPokemon(pokemon)
                                selectedPokemon = True
                                if self._achievements:
                                    url = 'http://127.0.0.1:5000/pokemon_added'
                                    data = {"pokemon_inventory": [{"name": pokemon.getName(), "level": pokemon.getLevel()}]}
                                    requests.post(url, json=data)
                    elif userInput == "2":
                        print("Great choice! please make your choice.")
                        print("1.[Chikorita, the grass type pokemon]")
                        print("2.[Cyndaquil, the fire type pokemon]")
                        print("3.[Totodile, the water type pokemon]")
                        print("4.[Go back]")
                        pokemonChoice = input("Choice:")
                        if pokemonChoice.isnumeric():
                            if pokemonChoice != "4":
                                pokeNum = int(pokemonChoice) + (2 * (int(pokemonChoice) - 1) + 151)
                                pokemon = Pokemon(pokeNum, 5)
                                self._player.addPokemon(pokemon)
                                selectedPokemon = True
                                if self._achievements:
                                    url = 'http://127.0.0.1:5000/pokemon_added'
                                    data = {"pokemon_inventory": [{"name": pokemon.getName(), "level": pokemon.getLevel()}]}
                                    requests.post(url, json=data)
                    else:
                        print("not a valid input")
        else:
            self._player.setName("C")
            self._player.addPokemon(Pokemon(4,5))
            print("DEV MODE: " + self._player.getName())
            selectedPokemon = True
        if selectedPokemon == True:
            self.mapArea()

    #call the Map area will be used for displaying the map, and getting the players choice on direction
    def mapArea(self):
        print(self._map.returnMap())
        for i in range(0,len(self._map.getNextMoves())):
            print(str(i + 1) + ".[" + str(self._map.getNextMoves()[i]) + "]")
        choice = input("Choice:")
        if choice.isnumeric():
            if choice == "0":
                return
            elif int(choice) <= len(self._map.getNextMoves()):
                choiceMove = self._map.getNextMoves()[int(choice) - 1]
                self._map.moveToSpace(choiceMove)
                self.forest(choiceMove.getEncounter())
            else:
                pass

    #displays the information regarding each encounter and handles the encouter like pokemon in encounter
    def forest(self,encounter):
        if encounter == "G":
            if self._combatTutorial and not self._devMode:
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
                self._combatTutorial = False
            opponent = Player()
            opponent.setName("wild")
            opponent.addPokemon(Pokemon(16, 5))
            self.battle(opponent)
        if encounter == "T":
            print("Welcome to your first trainer battle.")
            print("When you are in a battle you will be able ")



    # runs the battle functionality currently could be updated to run all choices or reduced to only contain the
    # battle or wild pokemon encounter. Contains the tutorial section for the wild battle, may need to be correctly
    # attached to the tutorial option. could also use a system for creating opponents that are appropriate to level.

    def _checkWinConditon(self, opponent):
        avOpp = opponent.getAvailablePokemon()
        avPl = self._player.getAvailablePokemon()
        return avOpp and avPl


    def battle(self, opponent):
        currentPokemon = opponent.getCurrentPokemon()
        while self._checkWinConditon(opponent):
            print("***************************************************************************************************")
            print(currentPokemon.getName())
            print("Health:" + str(currentPokemon.getHealth()))
            print("")
            print("")
            print("")
            print(self._player.getCurrentPokemon().getName())
            print("Health:" + str(self._player.getCurrentPokemon().getHealth()))
            print("***************************************************************************************************")
            selectedChoice = False
            while not selectedChoice:
                print("1.[Fight]")
                print("2.[Bag]")
                print("3.[run]")
                print("4.[Pokemon]")
                choice = input("Choice:")
                if choice.isnumeric():
                    if choice == "0":
                        return
                    elif choice == "1":
                        moves = self._player.getCurrentPokemon().getMoves()
                        for i in range(0,len(moves)):
                            currentMove = self._player.getCurrentPokemon().getMoves()[i]
                            print(str(i + 1) + ".[" + currentMove["name"] + " Power:" + str(currentMove["data"]["power"]) + \
                                  " Type:" + currentMove["data"]["type"] + " PP:" + str(currentMove["data"]["pp"]) + "]\r")
                        print("5.[Go Back]")
                        choice = input("Choice:")
                        if choice.isnumeric():
                            if choice == "0":
                                return
                            elif choice == "5":
                                pass
                            elif int(choice) <= len(moves):
                                self.calculateDamage(int(choice) - 1,opponent)
                                selectedChoice = True
                            else:
                                #error
                                pass
                    elif choice == "2":
                        bagChoiceMade = True
                        while bagChoiceMade:
                            print("1.[HP/PP restore]")
                            print("2.[Poke Balls]")
                            print("3.[Status Restore]")
                            print("4.[Battle Items]")
                            print("5.[Go Back]")
                            bagChoice = input("Choice:")
                            if bagChoice.isnumeric():
                                if bagChoice == "0":
                                    return
                                elif bagChoice == "5":
                                    bagChoiceMade = False
                                elif int(bagChoice) <= 5:
                                    bagSelection = self._player.getBag()[int(bagChoice) - 1]
                                    if len(bagSelection) > 0:
                                        #needs work
                                        pass
                                    else:
                                        print("No available items in this bag.")
                                else:
                                    #error
                                    pass

                    elif choice == "3":
                        pass
                    elif choice == "4":
                        pass
                    else:
                        pass
        self.mapArea()

    #used for damage calculation on each pokemon
    def calculateDamage(self,moveChoice, opponent):
        playerPokemon = self._player.getCurrentPokemon()
        opponentPokemon = opponent.getCurrentPokemon()
        playerMove = playerPokemon.getMoves()[moveChoice]
        moveLen = len(opponentPokemon.getMoves())
        rand = randint(0,moveLen - 1)
        opponentMove = opponentPokemon.getMoves()[rand]

        turnLine =[]
        if playerPokemon.getStats()["speed"] >= opponentPokemon.getStats()["speed"]:
            turnLine.append((playerPokemon, opponentPokemon, playerMove))
            turnLine.append((opponentPokemon, playerPokemon, opponentMove))
        else:
            turnLine.append((opponentPokemon, playerPokemon, opponentMove))
            turnLine.append((playerPokemon, opponentPokemon, playerMove))

        for i in range(0,len(turnLine)):
            #getting attacker defense and move
            attacker = turnLine[i][0]
            defender = turnLine[i][1]
            move = turnLine[i][2]
            if move["data"]["power"] is not None:
                #damage
                attack = int(attacker.getStats()["attack"]) if move["data"]["damage_class"] == "physical" else int(
                    attacker.getStats()["sp_attack"])
                defense = int(defender.getStats()["defense"]) if move["data"]["damage_class"] == "physical" else int(
                    defender.getStats()["sp_defense"])
                damage = ((((2 * int(attacker.getLevel()) / 5) + 2) * (
                            int(move["data"]["power"]) * (attack / defense)) / 50) + 2)
                # variables
                type1 = int(
                    self._typeChart[self._typeDict[move["data"]["type"]]][self._typeDict[defender.getStats()["type1"]]])
                if defender.getStats()["type2"] != '':
                    type2 = int(self._typeChart[self._typeDict[move["data"]["type"]]][self._typeDict[defender.getStats()["type2"]]])
                else:
                    type2 = 1
                stab = 1.5 if move["data"]["type"] == attacker.getStats()["type1"] or move["data"]["type"] == \
                              attacker.getStats()["type2"] else 1
                randomVal = randint(85, 100)
                damage *= type1 * type2 * stab * (randomVal / 100)
                damage = math.floor(damage)
            else:
                damage = 0
            #dealing damage
            print(attacker.getName() + " used " + move["name"])
            accuracy = randint(0,100)
            if accuracy <= move["data"]["accuracy"]:
                defender.dealDamage(damage)
                print(attacker.getName() + " dealt " + str(damage) + " damage to " + defender.getName())
            else:
                print(attacker.getName() + " missed.")
            if int(defender.getHealth()) <= 0:
                print(defender.getName() + " fainted.")
                if self._player.getCurrentPokemon() == defender:
                    if self._player.getAvailablePokemon():
                        #needs fixing
                        pokemon = self._player.getPokemon()
                        for i in range(0,len(pokemon)):
                            print(str(i + 1) + ".[" + pokemon[i].getName() + "]")
                        choice = input("Choice:")
                        if choice.isnumeric():
                            if choice == "0":
                                return
                            elif int(choice) <= len(pokemon):
                                self._player.setCurrentPokemon(int(choice) - 1)
                            else:
                                #error
                                pass
                    else:
                        print("You have no available Pokemon left.")
                        print("You have lost the tournament.")

                else:
                    if opponent.getAvailablePokemon():
                        opponent.setCurrentPokemon("next")
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.runGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
