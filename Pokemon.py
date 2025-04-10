"""
Class: Pokemon
used to hold all the information regarding one pokemon. contains a lot of info like stats obtained from the csv file,
using the parser, potential moves again obtained from the parser, level of the pokemon and current moves.

will need function to level up, check evolutions and learned moves on level up, possibly function to check damage or
deal damage, add moves for opponents.
IVs and EVs are not currently included

"""
import csv
import random
import re
import json
import math

class Pokemon:

    def __init__(self, pokedexNum, level):
        #local vars
        self._stats = {}
        self._moves = []
        self._level = 1
        self._potentialMoves = []
        self._health = 0

        parser = Parser()
        #gets and set stats via parser
        self._stats = parser.getStats(pokedexNum)
        # gets and set potential moves via parser
        self._potentialMoves = parser.getPotentialMoves(pokedexNum)
        quickSort(self._potentialMoves,0,len(self._potentialMoves)-1)
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
        #ivs and evs not included
        self._health = math.floor(0.01 * (2 * int(self._stats["hp"]) * self._level)) + self._level + 10
        #moves
        for i in range(0,len(self._potentialMoves)):
            if self._potentialMoves[i]["level"] <= self._level:
                if len(self._moves) >= 4:
                    self._moves.pop(0)
                dict = {}
                move = parser.getMove(self._potentialMoves[i]["name"])
                dict["power"] = move["power"]
                dict["priority"] = move["priority"]
                dict["type"] = move["type"]
                dict["damage_class"] = move["damage_class"]
                dict["pp"] = move["pp"]
                dict["accuracy"] = move["accuracy"]
                self._moves.append({"name": move["name"] , "data" : dict})

    def getStats(self):
        return self._stats
    def getName(self):
        return self._stats["name"]

    def getAbility(self):
        return self._stats["abilities"]

    def getHealth(self):
        return self._health

    def getLevel(self):
        return self._level

    def setLevel(self, level):
        self._level = level

    def getMoves(self,):
        return self._moves

    def getPotentialMoves(self):
        return self._potentialMoves

    def dealDamage(self, damage):
        self._health -= damage


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
        return data[pokeNum - 1]["moves"]

    def getMove(self, name):
        f = open('movesData.json', encoding="utf8")
        data = json.load(f)
        for i in range(len(data)):
            if data[i]["name"] == name:
                return data[i]



    # Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]["level"]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j]["level"] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort

def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)