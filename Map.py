import math
from random import randint

class Node:
    def __init__(self, encounter, position):
        self.next = []
        self.encounter = encounter
        self.position = position

    def __str__(self):
        return "encounter:" + self.encounter + " " + str(self.position)

    def __lt__(self, other):
        return self.position < other.position

    def getEncounter(self):
        return self.encounter
    def addNext(self, next):
        self.next.append(next)
    def getNext(self):
        return self.next

class Map:
    _mapList = ['G','T','C','S','B']
    _mapDict = {
        "G": "wild pokemon",
        "T": "Trainer",
        "C": "Pokemon Center",
        "S": "Poke Mart",
        "B": "Gym Battle"
    }
    _mapPercentages = [(100,0,0,0,0),(60,80,90,100,0),(40,70,90,100,0)]
    def __init__(self):
        self._distance = 9
        self._range = 4
        self._numPaths = 3
        self._sections = 3
        self._storedNode = [[],[],[],[],[],[],[],[],[]]
        self._map = []
        self._head = Node("head", (-1, -1))
        self._currentNode = self._head
        for i in range(0,self._distance):
            for j in range(0,self._range):
                rand = randint(0,100)
                for k in range(0,4):
                    if rand <= self._mapPercentages[math.floor(i/self._sections)][k]:
                        self._storedNode[i].append(Node(self._mapList[k], (i,j)))
                        break

        end = Node('B',(self._distance,0))
        for i in range(0,self._numPaths):
            #add starting nodes to head
            rand = randint(0,self._numPaths)
            self._head.addNext(self._storedNode[0][rand])
            #add end nodes to final node
            self._storedNode[self._distance-1][i].addNext(end)

        for j in range(0,self._numPaths):
            node = self._head.getNext()[j]
            for i in range(1, self._distance):
                lower = node.position[1] - 1 if node.position[1] - 1 >= 0 else 0
                upper = node.position[1] + 1 if node.position[1] + 1 <= self._range -1 else self._range -1
                rand = randint(lower,upper)
                newNode = self._storedNode[i][rand]
                node.addNext(newNode)
                node = newNode

    def createMap(self):
        bigList = []
        list = [self._head.getNext()[0], self._head.getNext()[1], self._head.getNext()[2]]
        for i in range(0, self._distance + 1):
            newList = []
            for object in list:
                newList.extend(object.getNext())
            fill = []
            [fill.append(x) for x in list if x not in fill]
            fill.sort()
            direction = []
            #needs fixing
            for object in fill:
                for nextObj in object.getNext():
                    if object.position[1] < nextObj.position[1]:
                        direction.append("          \\      ")
                    elif object.position[1] == nextObj.position[1]:
                        direction.append("          |       ")
                    else:
                        direction.append("          /       ")
            bigList.append(fill)
            bigList.append(direction)
            list = newList
            self._map = bigList

    def printMap(self):
        for i in range(0,self._distance):
            print("\r\n")
            for j in range(0,self._range):
                print(self._storedNode[i][j])
        print("\r\n")

    def returnMap(self):
        #test
        text = ""
        for list in self._map:
            for object in list:
                text += str(object)
            text += "\n"
        return text

    def displayMap(self):
        # test
        bigList = []
        list = [self._head.getNext()[0], self._head.getNext()[1], self._head.getNext()[2]]
        for i in range(0, self._distance + 1):
            newList = []
            for object in list:
                newList.extend(object.getNext())
            fill = []
            [fill.append(x) for x in list if x not in fill]
            fill.sort()
            direction = []
            for object in fill:
                for nextObj in object.getNext():
                    if object.position[1] < nextObj.position[1]:
                        direction.append("\t\\\t  ")
                    elif object.position[1] == nextObj.position[1]:
                        direction.append("\t|\t   ")
                    else:
                        direction.append("\t/\t   ")
            bigList.append(fill)
            bigList.append(direction)
            list = newList

        for list in bigList:
            text = ""
            for object in list:
                text += str(object)
            print(text)

    def getNextMoves(self):
        moves = self._currentNode.getNext()
        moves = list(set(moves))
        moves.sort()
        return moves
    def moveToSpace(self,move):
        # for obj in self._currentNode.getNext():
        #     print(move == obj)
        self._currentNode = move

