import collections
from random import choice
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2, 11)] + list('JQKA')


class Pocket:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def set_card(deck, position, card):
    deck._cards[position] = card


Pocket.__setitem__ = set_card


def initdict():
    suitdata = {
        'clubs': [],
        'diamonds': [],
        'spades': [],
        'hearts': []
    }
    rankdata = {rank: [] for rank in ranks}
    return suitdata, rankdata


def arrange(mycard, rdt):
    for c in mycard:
        #sdt[c.suit].append(c)
        rdt[c.rank].append(c)
    return rdt


def arrangesdt(mycard, sdt):
    for c in mycard:
        sdt[c.suit].append(c)
    return sdt


def getct(rdt, sdt):
    ct = {
        'samesuitstraight': [],
        'resamesuitstraight': [],
        'bomb': [],
        'hulu': [],
        'samesuit': [],
        'straight': [],
        'restraight': [],
        'triplets': [],
        'cpcp': [],
        'cp': [],
        'single': []

    }
    count = 0
    s = []
    # ranklist = [len(rdt[r]) for r in rdt]
    # print(ranklist)
    for r in rdt:
        # print(rdt[r])
        rlist = rdt[r]
        le = len(rlist)
        if le == 0:
            continue
        #print(rlist)
        if le == 4:
            ct['bomb'].append(rlist)
        elif le == 3:
            ct['triplets'].append(rlist)
        elif le == 2:
            ct['cp'].append(rlist)
        else:
            ct['single'].append(rlist)
    for s in sdt:
        if len(sdt[s]) >= 5:
            ct['samesuit'].append(sdt[s])
        elif len(sdt[s]) == 3:
            ct['samesuit'].append(sdt[s])
    ct = findstraight(rdt, ct)
    ct = findrestraight(rdt, ct)
    ct = findsamestraight(ct)
    ct = gethulu(ct)
    ct = getcpcp(ct)

    return ct
# cpcp
def getcpcp(card_type):
    l = len(card_type['cp'])
    if  l >= 2:
        if l % 2:
            card_type['cpcp'].append(card_type['cp'][-2] + card_type['cp'][-3])
        else:
            card_type['cpcp'].append(card_type['cp'][-1] + card_type['cp'][-2])
    return card_type
# hulu
def gethulu(card_type):
    if len(card_type['triplets']) and len(card_type['cp']):
        for st in card_type['triplets']:
            card_type['hulu'].append(st + card_type['cp'][0])
    return card_type


# resamestraight

# samestraight
def findsamestraight(card_type):
    for sunzi in card_type['straight']:
        suitnum = {
            'clubs': 0,
            'diamonds': 0,
            'spades': 0,
            'hearts': 0
        }
        for rank in sunzi:
            for c in rank:
                if c.suit == 'clubs':
                    suitnum['clubs'] += 1
                elif c.suit == 'diamonds':
                    suitnum['diamonds'] += 1
                elif c.suit == 'spades':
                    suitnum['spades'] += 1
                else:
                    suitnum['hearts'] += 1
        for sn in suitnum:
            if suitnum[sn] == 5:
                card_type['samesuitstraight'].append(sunzi)
    # reverse
    for sunzi in card_type['restraight']:
        suitnum = {
            'clubs': 0,
            'diamonds': 0,
            'spades': 0,
            'hearts': 0
        }
        for rank in sunzi:
            for c in rank:
                if c.suit == 'clubs':
                    suitnum['clubs'] += 1
                elif c.suit == 'diamonds':
                    suitnum['diamonds'] += 1
                elif c.suit == 'spades':
                    suitnum['spades'] += 1
                else:
                    suitnum['hearts'] += 1
        for sn in suitnum:
            if suitnum[sn] == 5:
                ths = (suitnum[sn], sunzi)
                card_type['resamesuitstraight'].append(ths)
    return card_type


# straight
def findstraight(rdt, ct):
    slist = []
    counts = 0

    for r in rdt:
        c = rdt[r]
        if len(c) == 0:
            if len(slist) == 3:
                ct['straight'].append(slist.copy())
            counts = 0
            slist.clear()
        else:
            slist.append(c)
            counts += 1
        if len(slist) == 5:
            ct['straight'].append(slist.copy())
            slist.clear()
            counts = 0
    if len(slist) == 3:
        # print(counts)
        ct['straight'].append(slist.copy())
    #print(ct['straight'])
    return ct


def findrestraight(rdt, ct):
    slist = []
    counts = 0
    rank = [r for r in rdt]
    for r in reversed(rank):
        c = rdt[r]
        # print(c)
        if len(c) == 0:
            if len(slist) == 3:
                ct['restraight'].append(slist.copy())
            counts = 0
            slist.clear()
        else:
            slist.append(c)
            counts += 1
        if counts == 5:
            ct['restraight'].append(slist.copy())
            slist.clear()
            counts = 0
    if len(slist) == 3:
        # print(counts)
        ct['restraight'].append(slist.copy())
    #print(ct['restraight'])
    return ct


def Licensing():
    deck = Pocket()
    shuffle(deck)
    mycard = deck[:13]
    return mycard


'''
def findstraight(mycard, ctype, rdt):

    ranklist = reversed([len(rdt[r]) for r in rdt])
    count = 0
    mc = 0
    s = []
    slist = []
    while(1):
        for rl,c in ranklist,mycard:
            if rl > 0:
                count += 1

                rl -= 1
            else:
                count = 0
            if count == 5:
                if rl > 0:

                    break

'''
'''



        if le == 0:

            if len(s) >= 5:
                slist.append(s)
                ct['straight'] += slist
                #print('-----------')
                #print(ct['straight'])
            elif len(s) >= 3:
                slist.append(s)
                ct['straight'] += slist
            count = 0
            s = []
            continue
        else:

            s.append(rlist)
            print(s)


    if len(s) >= 5:
        ct['straight'].append(s)
        print('-----------')
        print(ct['straight'])
    print(ct['straight'])
    for s in sdt:
        #print(sdt)
        slist = sdt[s]
        if len(slist) == 13:
            ct['samesuitstraight'].append(slist)
        if len(slist) >= 5:
            ct['samesuit'].append(slist)
        elif len(slist) == 3:
            ct['samesuit'].append(slist)
    '''

# result = sorted(mycard,key=lambda x:(x[1].lower(),x[0]))
