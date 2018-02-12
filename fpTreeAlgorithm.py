#!/usr/bin/python3

#-*- coding: utf-8 -*-

import sys
from utils import *

class TreeNodes:

    def __init__(self,value):
        self.value = value
        self.frequence = 0
        self.nextEl = []

    def getVal(self):
        return self.value

    def getNext(self):
        return self.nextEl

    def addNode(self, node):
        self.nextEl.append(node)

def isInTree(tree, value):
    return 0

def fpTreeAlgorithm(liste, data):

    liste.sort(key=lambda x: x[1], reverse=True)
    print("On a construit la liste \"triée\" suivante: ", liste)
    print(data)

    tree = TreeNodes(None)

    # passe des données
    for datas in data:
        #print(data[datas])
        for l in liste:
            #print(l, data[datas])
            if l[0] in data[datas]:
                if not isInTree(tree,l[0]):
                    print(l)




    """
    print(tree.getVal())
    print(tree.getNext())

    tree.addNode(tree)
    tree.addNode(tree)
    tree.addNode(tree)
    print(tree.getNext()[2].getVal())
    """

    return

if __name__ == '__main__':

    if len(sys.argv) > 2:
        file = sys.argv[1]
        confidence = int(sys.argv[2])
        tid, itemSeen, itemSort, L, D, level = initFromFile(file, confidence)
        print()
        print("k itemset fréquents:", fpTreeAlgorithm(L,D))
        print()

    else:
        print("ERREUR ARGUMENT\nUsage:", sys.argv[0], "fichier min_support\n")
        sys.exit(1)