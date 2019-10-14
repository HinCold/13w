# 判断特殊牌
# 三同花
def triSamesuit(card_type):
    count = 0
    for ss in card_type['samesuit']:

        count += 5 * (int(len(ss)) / 5)
        if len(card_type['samesuit']) == 3:
            count += 3
    if count == 13:
        return True


# 三顺子

def triStraght(card_type):

    snum = len(card_type['straight'])
    if snum == 3:
        return True
    for sunzi in card_type['straight']:
        countone = 0
        countto = 0
        counttri = 0
        snum = 0
        for c in sunzi:
            if len(c) == 1:
                countone += 1
            elif len(c) == 2:
                countone += 1
                countto += 1
            elif len(c) == 3:
                countone += 1
                counttri += 1
                countto += 1
            else:
                countone = 0
                countto = 0
                counttri = 0
        if countone == 3 or countto == 3 or counttri == 3:
            snum += 1
        if countone == 5:
            snum += 1
        if countto == 5:
            snum += 1
    if snum == 3:
        return True


# 六对半
def sixCp(card_type):
    if len(card_type['bomb']) * 2 + len(card_type['cp']) == 6:
        return True


# 五对三条
def fiveCpAndTriplets(card_type):
    if len(card_type['bomb']) * 2 + len(card_type['cp']) == 5 and len(card_type['triplets']):
        return True


# 四套三条
def fourTriplets(card_type):
    if len(card_type['triplets']) == 3:
        return True


# 双怪双三
def twoHuluaCp(card_type):
    if ((len(card_type['triplets']) == 2 and len(card_type['bomb']) * 2 + len(card_type['cp']) == 3)
            or (len(card_type['triplets']) == 3 and len(card_type['bomb']) * 2 + len(card_type['cp']) == 2)):
        return True


# 凑一色
def sameColor(sdt):
    if len(sdt['clubs']) + len(sdt['spades']) == 13 or len(sdt['hearts']) + len(sdt['diamonds']) == 13:
        return True


# 全小
def allSmall(rdt):
    if len(rdt['2']) + len(rdt['3']) + len(rdt['4']) + len(rdt['5']) + len(rdt['6']) + len(rdt['7']) + len(
            rdt['8']) == 13:
        return True


# 全大
def allBig(rdt):
    if len(rdt['8']) + len(rdt['9']) + len(rdt['10']) + len(rdt['J']) + len(rdt['Q']) + len(rdt['K']) + len(
            rdt['A']) == 13:
        return True


# 三分天下
def triBomb(card_type):
    if len(card_type['bomb']) == 3:
        return True


# 三同花顺
'''
def triSameStraight(card_type):
    if triStraght(card_type):
        dict = {
            'clubs': 0,
            'diamonds': 0,
            'spades': 0,
            'hearts': 0
        }
        countsuit = 0
        for sz in card_type['straight']:
            mainsuit = ''
            vicesuit = ''
            thirdsuit = ''
            mainnum = 0
            vicenum = 0
            thirdnum = 0
            for rank in sz:
                if len(rank) == 1:
                    if mainsuit == '':
                        mainsuit = rank[0].suit
                        mainnum += 1
                    elif mainsuit == rank[0].suit:
                        mainnum += 1
                    else:
                        mainsuit = rank[0].suit
                        mainnum = 1
                elif len(rank) == 2:
                    if mainsuit == '':
                        mainsuit = rank[0].suit
                        mainnum += 1
                        vicesuit = rank[1].suit
                        vicenum += 1
                    elif mainsuit == rank[0].suit or mainsuit == rank[1].suit:
                        mainnum += 1
                        if mainsuit == rank[0].suit:
                            if vicesuit == '':
                                vicesuit = rank[1].suit
                                vicenum += 1
                            elif vicesuit == rank[1].suit:
                                vicenum += 1
                            else:
                                vicesuit = rank[1].suit
                                vicenum = 1
                        else:
                            if vicesuit == '':
                                vicesuit = rank[0].suit
                                vicenum += 1
                            elif vicesuit == rank[0].suit:
                                vicenum += 1
                            else:
                                vicesuit = rank[0].suit
                                vicenum = 1
                    else:
                        mainsuit = rank[0].suit
                        mainnum = 1
                        if vicesuit == '':
                            vicesuit = rank[1].suit
                            vicenum += 1
                        elif vicesuit == rank[1].suit:
                            vicenum += 1
                        else:
                            vicesuit = rank[1].suit
                            vicenum = 1
                elif len(rank) == 3:
                    if mainsuit == '':
                        mainsuit = rank[0].suit
                        mainnum += 1
                        vicesuit = rank[1].suit
                        vicenum += 1
                        thirdsuit = rank[2].suit
                        thirdnum += 1
                    elif mainsuit == rank[0].suit or mainsuit == rank[1].suit or mainsuit == rank[2].suit:
                        mainnum += 1
                        if mainsuit == rank[0].suit:
                            if vicesuit == rank[2].suit or vicesuit == rank[1].suit:
                                vicenum += 1
                                if vicesuit == rank[2].suit:
                                    if thirdsuit == '':
                                        thirdsuit = rank[1].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[1].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[1].suit
                                        thirdnum = 1
                                else:
                                    if thirdsuit == '':
                                        vicesuit = rank[2].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[2].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[2].suit
                                        thirdnum = 1
                            else:
                                vicesuit = rank[1].suit
                                vicenum += 1
                                if thirdsuit == '':
                                    thirdsuit = rank[1].suit
                                    thirdnum += 1
                                elif thirdsuit == rank[1].suit:
                                    thirdnum += 1
                                else:
                                    thirdsuit = rank[1].suit
                                    thirdnum = 1
                        elif mainsuit == rank[1].suit:
                            if vicesuit == rank[2].suit or mainsuit == rank[0].suit:
                                vicenum += 1
                                if vicesuit == rank[2].suit:
                                    if thirdsuit == '':
                                        thirdsuit = rank[0].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[0].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[0].suit
                                        thirdnum = 1
                                else:
                                    if thirdsuit == '':
                                        vicesuit = rank[2].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[2].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[2].suit
                                        thirdnum = 1
                            else:
                                vicesuit = rank[0].suit
                                vicenum += 1
                                if thirdsuit == '':
                                    thirdsuit = rank[2].suit
                                    thirdnum += 1
                                elif thirdsuit == rank[2].suit:
                                    thirdnum += 1
                                else:
                                    thirdsuit = rank[2].suit
                                    thirdnum = 1
                        else:
                            if vicesuit == rank[0].suit or vicesuit == rank[1].suit:
                                vicenum += 1
                                if vicesuit == rank[0].suit:
                                    if thirdsuit == '':
                                        thirdsuit = rank[1].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[1].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[1].suit
                                        thirdnum = 1
                                else:
                                    if thirdsuit == '':
                                        vicesuit = rank[0].suit
                                        thirdnum += 1
                                    elif thirdsuit == rank[0].suit:
                                        thirdnum += 1
                                    else:
                                        thirdsuit = rank[0].suit
                                        thirdnum = 1
                            else:
                                vicesuit = rank[0].suit
                                vicenum += 1
                                if thirdsuit == '':
                                    thirdsuit = rank[1].suit
                                    thirdnum += 1
                                elif thirdsuit == rank[1].suit:
                                    thirdnum += 1
                                else:
                                    thirdsuit = rank[1].suit
                                    thirdnum = 1
                    else:
                        mainsuit = rank[0].suit
                        mainnum += 1
                        if vicesuit == rank[2].suit or vicesuit == rank[1].suit:
                            vicenum += 1
                            if vicesuit == rank[2].suit:
                                if thirdsuit == '':
                                    thirdsuit = rank[1].suit
                                    thirdnum += 1
                                elif thirdsuit == rank[1].suit:
                                    thirdnum += 1
                                else:
                                    thirdsuit = rank[1].suit
                                    thirdnum = 1
                            else:
                                if thirdsuit == '':
                                    vicesuit = rank[2].suit
                                    thirdnum += 1
                                elif thirdsuit == rank[2].suit:
                                    thirdnum += 1
                                else:
                                    thirdsuit = rank[2].suit
                                    thirdnum = 1
                        else:
                            vicesuit = rank[1].suit
                            vicenum += 1
                            if thirdsuit == '':
                                thirdsuit = rank[1].suit
                                thirdnum += 1
                            elif thirdsuit == rank[1].suit:
                                thirdnum += 1
                            else:
                                thirdsuit = rank[1].suit
                                thirdnum = 1
            if not mainsuit == '':
                if mainnum - dict[mainsuit] == 1:
                    dict[mainsuit] = mainnum
            if (not vicesuit == ''):
                if vicenum - dict[vicesuit] == 1:
                    dict[vicesuit] = vicenum
            if (not thirdsuit == ''):
                if thirdnum - dict[thirdsuit] == 1:
                    dict[thirdsuit] = thirdnum
        for d in dict:
            if dict[d] >= 10:
                countsuit += 10
            elif dict[d] >= 5:
                countsuit += 5
            elif dict[d] >= 3:
                countsuit += 3
        if countsuit == 13:
            return True
'''


def triSameStraight(card_type):
    if triStraght(card_type):
        countss = 0
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
                if suitnum[sn] == 3 or suitnum[sn] == 5:
                    countss += 1
                else:
                    return False
        return True
    else:
        return False


# 十二皇族
def tweRayol(rdt):
    if len(rdt['10']) + len(rdt['J']) + len(rdt['Q']) + len(rdt['K']) + len(rdt['A']) >= 12:
        return True


# 一条龙
def aDragon(card_type):
    if len(card_type['straight']) == 13:
        return True


# 至尊青龙
def dragonKing(card_type):
    if len(card_type['samesuit']) == 13:
        return True


def special(card_type, rdt, sdt):
    special_type = ''
    if triSameStraight(card_type):
        special_type = 'triSameStraight'
    elif triStraght(card_type):
        special_type = 'triStraight'
    elif sixCp(card_type):
        special_type = 'sixCp'
    elif fiveCpAndTriplets(card_type):
        special_type = 'fiveCpAndTriplets'
    elif fourTriplets(card_type):
        special_type = 'fourTriplets'
    elif twoHuluaCp(card_type):
        special_type = 'twoHuluaCp'
    elif sameColor(sdt):
        special_type = 'sameColor'
    elif allSmall(rdt):
        special_type = 'allSmall'
    elif allBig(rdt):
        special_type = 'allBig'
    elif triBomb(card_type):
        special_type = 'triBomb'
    elif triSameStraight(card_type):
        special_type = 'triSameStraight'
    elif tweRayol(rdt):
        special_type = 'tweRayol'
    elif aDragon(card_type):
        special_type = 'aDragon'
    elif dragonKing(card_type):
        special_type = 'aDragon'
    return special_type
