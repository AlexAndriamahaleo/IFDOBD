#!/usr/bin/python3

#-*- coding: utf-8 -*-


import sys
from utils import *
import itertools



def seflJoinCandidat(item,level):
    """
    Jointure sur les itemsets fréquents
    :param item:
    :param level:
    :return:
    """
    join = []
    for tuple in itertools.combinations(item, level):
        join.append(tuple)
    return join


def tuplePossible(data,level):
    """
    Jointure à partir d'un nouvel item set
    :param data:
    :param level:
    :return:
    """
    generatePossibleTuple = []
    for i, k in data.items():
        generatePossibleTuple = generatePossibleTuple + seflJoinCandidat(list(k), level)
    return generatePossibleTuple


def isNotInLast(new, last):
    """
    Vérifie si un k-item est infréquent au niveau k-1
    :param new:
    :param last:
    :return:
    """
    for itmfq in last:
        if itmfq[0] in new:
            return False
    return True


def isInOldItemSet(inf, ci, level):
    """
    Génère les combinaisons pertinente
    :param inf:
    :param ci:
    :param level:
    :return:
    """
    isNotIn = []

    for couple in ci:
        new = seflJoinCandidat(couple, level - 1)

        if isNotInLast(new, inf):
            isNotIn.append(couple)
    return isNotIn




def unionKitemSetFrequent(freq, union):
    """
    Resultat final
    :param freq:
    :param union:
    :return:
    """
    for (itm, supp) in freq:
       union.append(itm)
    return union


def aprioriAlgorithm(level, itemSort, li):
    """
    Algorithme en lui même
    :param level:
    :param itemSort:
    :param li:
    :return:
    """
    delete = 0
    possibleTuple = []
    tupleSeen = []
    supportSeen = []
    allListi = []
    while li and level:
        scan, itemSort, notfrequent = deleteInfrequent(li, itemSort, confidence)
        level = level + 1
        li = seflJoinCandidat(itemSort, level)
        li = isInOldItemSet(notfrequent, li, level)
        allListi = unionKitemSetFrequent(scan, allListi)
        print("L%s: " % (level-1), scan)
        print("C%s: " % level, li )


        if delete:
            tupleSeen.clear()
            supportSeen.clear()
            possibleTuple.clear()
            scan.clear()

        possibleTuple = tuplePossible(D, level)

        print()
        # cherche si un élément existe dans Data (D)
        for elem in possibleTuple:
            if elem in li and elem not in tupleSeen:
                tupleSeen.append(elem)
                supportSeen.append(1)
            elif elem in li and elem in tupleSeen:
                supportSeen[tupleSeen.index(elem)] = supportSeen[tupleSeen.index(elem)] + 1
        delete = 1

        li.clear()
        for a, b in zip(tupleSeen, supportSeen):
            li.append((a, b))
    return allListi


if __name__ == '__main__':

    if len(sys.argv) > 2:
        file = sys.argv[1]
        confidence = int(sys.argv[2])
        tid, itemSeen, itemSort, L, D, level = initFromFile(file, confidence)
        print()
        print("k itemset fréquents:", aprioriAlgorithm(level, itemSort, L))
    else:
        print("ERREUR ARGUMENT\nUsage:", sys.argv[0], "fichier min_support\n")
        sys.exit(1)
