class Directory:

    def __init__(self):
        self.items = []

    def clearAll(self):
        self.items.clear()

    def addItem(self, item):
        self.items.append(item)

    def getSize(self):
        size = 0
        for item in enumerate(self.items):
            size += 1
        return size

    def showItem_(self, usearch):
        for x in enumerate(self.items):
            if self.items[x[0]].one == usearch:
                self.items[x[0]].showItem()
            elif self.items[x[0]].two == usearch:
                self.items[x[0]].showItem()
            elif self.items[x[0]].pastprinciple == usearch:
                self.items[x[0]].showItem()
            elif self.items[x[0]].four == usearch:
                self.items[x[0]].showItem()
            elif self.items[x[0]].five == usearch:
                self.items[x[0]].showItem()
            else:
                print('No corresponding item.')

    def deleteItem(self, oneSearch, twoSearch, threeSearch, fourSearch, fiveSearch):
        for x in range(0, self.getSize()):
            if self.items[x][0] == oneSearch:
                if self.items[x][1] == twoSearch:
                    if self.items[x][2] == threeSearch:
                        if self.items[x][3] == fourSearch:
                            if self.items[x][4] == fiveSearch:
                                self.items.pop(x)
                                print('(Found item, item deleted.)')
                                break
                            else:
                                print('(Fifth element, no match)')
                        else:
                            print('(Fourth element, no match)')
                    else:
                        print('(Third element, no match)')
                else:
                    print('(Second element, no match)')
            else:
                print('(First element, no match)')

    def print(self):
        for elem in enumerate(self.items):
            print(elem)


class Item:

    def __init__(self, one='', two='', three='', four='', five=''):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five

    def setOne(self, one):
        self.one = one

    def setTwo(self, two):
        self.two = two

    def setThree(self, three):
        self.three = three

    def setFour(self, four):
        self.four = four

    def setFive(self, five):
        self.five = five