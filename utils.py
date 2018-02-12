import re


def deleteInfrequent(L, itemset, confidence):
    """
    Renvoie l'ensemble des items fréquent
    :param L:
    :param itemset:
    :return:
    """
    CL = []
    infrequent = []
    itemset.clear()
    for i in L:
        if i[1] >= confidence:
            CL.append(i)
            if len(i[0]) > 1:
                for j in i[0]:
                    if j not in itemset:
                        itemset.append(j)
            else:
                itemset.append(i[0])
        else:
            infrequent.append(i)
    if itemset:
        itemset.sort()
    return CL, itemset, infrequent


def initFromFile(filename, confidence):
    """
    Initialise la Base D et Effectue le premier Scan
    :param filename:
    :return:
    """
    id = []
    item = []
    itemSort = []
    itemSeen = []
    itemSupport = []
    L = []
    D = {}
    level = 1
    print("\nlecture du fichier...")
    with open(filename, 'r') as jeu:
        content = jeu.read().split('\n')
        for i in range(content.__len__()):
            # itération sur chaque ligne
            line = re.split("[, \-:;]+", content[i])

            flag = 1
            key = 0

            #print(line.__len__())

            for l in range(line.__len__()):
                # itération sur chaque élément d'une ligne
                if flag == 1:
                    id.append(line[l])
                    key = line[l]
                    flag = 0
                else:
                    item.append(line[l])
                    itemSeen.append(line[l])
                    if line[l] not in itemSort:
                        itemSort.append(line[l])

            D[key] = tuple(item)
            item.clear()

        itemSort.sort()

        for tab in itemSort:
            support = itemSeen.count(tab)
            itemSupport.append(support)



        for a, b in zip(itemSort, itemSupport):
            L.append((a, b))

        scan, itemSort, inf = deleteInfrequent(L, itemSort, confidence)
        print("\nData: ", D, "\nC%s: " % level, L)

    return id, itemSeen, itemSort, L, D, level
