from pocket import *




def getcard(key, ct):
    '''
    aaa
    if key == 'samesuitstraight' or key == 'resamesuitstraight':
    suit = ct[key][-1][0]
    list = []
    for ths in ct[key]:
        if len(ths[1]) == 5:
            for rank in ths[1]:
                for c in rank:
                    if c.suit == suit:
                        list += c
            if key == 'samesuitstraight':
                return list.copy(), list[-1].rank
            else:
                return list.copy(), list[0].rank
        else:
            return None, None
    elif key == 'straight' or key == 'restraight':
    list = []
    for sz in ct[key]:
        if len(sz) == 5:
            for rank in sz:

                for c in rank:

                    list.append(c)

                    break
            #print(list)
            if key == 'straight':
                return list.copy(), list[-1].rank
            else:
                return list.copy(), list[0].rank
        else:
            return None, None
    '''

    if key == 'samesuit':
        list = []
        for th in ct[key]:
            if len(th) >= 5:
                for i in range(5):
                    list.append(th[-(i+1)])
                    #print(list)
                return list.copy(), list[-1].rank
            else:
                return None, None
    elif key == 'cp':
        return ct[key][-1].copy(), ct[key][-1][-1].rank
    else:
        return ct[key][0].copy(), ct[key][0][-1].rank

def updata(mycard, list):

    for c in list:
        #print(c)
        mycard.remove(c)
        #print(mycard)
    sdt, rdt = initdict()
    rdt = arrange(mycard, rdt)
    sdt = arrangesdt(mycard, sdt)
    ct = getct(rdt, sdt)
    ct = findstraight(rdt, ct)
    ct = findrestraight(rdt, ct)
    ct = findsamestraight(ct)
    return ct, mycard
def getctpoint(key):

    if key == 'samesuitstraight' or key == 'resamesuitstraight':
        return 90
    elif key == 'bomb':
        return 80
    elif key == 'hulu':
        return 70
    elif key == 'samesuit':
        return 60
    elif key == 'straight' or key == 'restraight':
        return 50
    elif key == 'triplets':
        return 40
    elif key == 'cpcp':
        return 30
    elif key == 'cp':
        return 20
    else:
        return 10
def getrankpoint(rank):
    if rank == None:
        return 0
    elif rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    else:
        return int(rank)

def getPile(mycard, rdt, sdt,ct):
    qbtm = []
    qbsc = []
    fb = []
    fm = []
    fh = []
    fsc = 0

    for key in ct:
        sc = 0
        if len(ct[key]):
            # 顺子
            if key == 'straight':
                dsz1 = []

                for i in range(len(ct[key])):
                    dsz1.clear()
                    sz = ct[key][i]
                    if len(sz) == 3:
                        continue
                    for rank in sz:
                        dsz1.append(rank)
                    sz = ct['restraight'][-(i+1)]
                    for j in range(len(sz)):

                        if sz[-j-1] in dsz1:
                            continue
                        else:
                            dsz1.append(sz[-j-1])
                    print('hhhhhhhh')
                    print(dsz1)
                    slist = []
                    for j in range(len(dsz1)):
                        for k in range(5):
                            for c in dsz1[j+k]:
                                slist.append(c)
                                break
                        qbtm.append(slist.copy())
                        brank = dsz1[j+4][0].rank
                        sc += getctpoint(key)
                        sc += getrankpoint(brank) * 0.1
                        qbsc.append(sc)
                        slist.clear()
                        sc = 0
                        if j == len(dsz1) - 5:
                            break
            elif key == 'samesuitstraight':
                dsz1 = []

                for i in range(len(ct[key])):
                    dsz1.clear()
                    sz = ct[key][i]
                    if len(sz) == 3:
                        continue
                    for rank in sz:
                        dsz1.append(rank)
                    sz = ct['resamesuitstraight'][-(i + 1)]
                    for j in range(len(sz)):

                        if sz[-j - 1] in dsz1:
                            continue
                        else:
                            dsz1.append(sz[-j - 1])
                    print('hhhhhhhh')
                    print(dsz1)
                    slist = []

                    for j in range(len(dsz1)):
                        for k in range(5):
                            for c in dsz1[j + k]:
                                slist.append(c)
                                break
                        qbtm.append(slist.copy())
                        brank = dsz1[j + 4][0].rank
                        sc += getctpoint(key)
                        sc += getrankpoint(brank) * 0.1
                        qbsc.append(sc)
                        slist.clear()
                        sc = 0
                        if j == len(dsz1) - 5:
                            break
            elif key == 'restraight' or key == 'resamesuitstraight':
                continue
            elif key == 'samesuit':
                for th in ct[key]:
                    if len(th) >= 5:
                        print('tonhhuaaaaaaaaaaaaaaaaaaaaaaa')

                        l = len(th)
                        sc = 0
                        tlist = []

                        for a in range(l-4):
                            tlist.append(th[a])
                            for b in range(a+1, l-3):
                                tlist.append(th[b])
                                for c in range(b+1, l-2):
                                    tlist.append(th[c])
                                    for d in range(c+1, l-1):
                                        tlist.append(th[d])
                                        for e in range(d+1, l):
                                            ecard = th[e]
                                            tlist.append(ecard)
                                            print('------------kkkkkkkkkkkkkkk---------')
                                            print(tlist)
                                            qbtm.append(tlist.copy())
                                            brank = ecard.rank
                                            sc += getctpoint(key)
                                            sc += getrankpoint(brank) * 0.1
                                            qbsc.append(sc)
                                            sc = 0
                                            tlist.pop()
                                        tlist.pop()
                                    tlist.pop()
                                tlist.pop()
                            tlist.pop()
            elif key == 'cpcp':
                cp = ct['cp']
                clist = []
                sc = 0
                for a in range(len(cp)-1):
                    clist += cp[a]
                    arank = cp[a][0].rank
                    for b in range(a+1, len(cp)):
                        clist += cp[b]
                        print('--------ccccc-------')
                        print(clist)
                        brank = cp[b][0].rank
                        clist += ct['single'][0]
                        qbtm.append(clist.copy())
                        sc += getctpoint(key)
                        bc = getrankpoint(brank)
                        sc += bc * 0.1
                        ac = getrankpoint(arank)
                        if bc - ac == 1:
                            sc += 2
                        qbsc.append(sc)
                        sc = 0
                        clist = clist[:2]
                    clist.clear()
            elif key == 'hulu':
                hlist = []

                for st in ct['triplets']:
                    hrank = st[0].rank
                    for cp in ct['cp']:
                        hlist = st + cp
                        print('-------ttttttttttttt----------')
                        print(hlist)
                        qbtm.append(hlist.copy())
                        qbsc.append(70 + getrankpoint(hrank)*0.1)
            else:
                bottom, brank = getcard(key, ct)

                if not bottom == None:
                    sc += getctpoint(key)
                    sc += getrankpoint(brank)*0.1
                    qbsc.append(sc)
                    if len(bottom) < 5:
                        for i in range(5-len(bottom)):
                            bottom += ct['single'][i]
                    qbtm.append(bottom.copy())
                    bottom.clear()
            if key == 'bomb':
                for st in ct['bomb']:
                    blist = []
                    hrank = st[0].rank
                    for a in range(2):
                        blist.append(st[a])
                        for b in range(a + 1, 3):
                            blist.append(st[b])
                            for c in range(b + 1, 4):
                                blist.append(st[c])

                                for cp in ct['cp']:
                                    hlist = blist + cp
                                    print('-------bbbbbbbbbbbbbbbbb----------')
                                    print(hlist)
                                    qbtm.append(hlist.copy())
                                    qbsc.append(70+getrankpoint(hrank)*0.1)
                                blist.pop()
                            blist.pop()
                        blist.pop()

        if key == 'cpcp':
            break
    print(qbsc)
    print(qbtm)
    for i in range(len(qbtm)):
        bsc = qbsc[i]
        bottom = qbtm[i]
        #print(bsc)
        mmcard = mycard.copy()
        print('----------aaaaaaaaa-----------')
        print(bottom)

        ct, mmcard = updata(mmcard, bottom)
        print('---------mct------')
        print(ct)
        qmd = []
        qmsc = []
        for key in ct:
            sc = 0
            if len(ct[key]):
                # 顺子
                if key == 'straight':
                    dsz1 = []

                    for i in range(len(ct[key])):
                        dsz1.clear()
                        sz = ct[key][i]
                        if len(sz) == 3:
                            continue
                        for rank in sz:
                            dsz1.append(rank)
                        sz = ct['restraight'][-(i + 1)]
                        for j in range(len(sz)):

                            if sz[-j - 1] in dsz1:
                                continue
                            else:
                                dsz1.append(sz[-j - 1])
                        #print('hhhhhhhh')
                        #print(dsz1)
                        slist = []
                        print('----mdsz-------')
                        print(dsz1)

                        print('111111111111')
                        for j in range(len(dsz1)):
                            print('222222222222222')
                            for k in range(5):
                                for c in dsz1[j + k]:
                                    slist.append(c)
                                    break
                            print('-------slist-----')
                            print(slist)
                            qmd.append(slist.copy())
                            mrank = dsz1[j + 4][0].rank
                            sc += getctpoint(key)
                            sc += getrankpoint(mrank) * 0.1
                            qmsc.append(sc)
                            slist.clear()
                            sc = 0
                            if j == len(dsz1) - 5:
                                break
                elif key == 'samesuitstraight':
                    dsz1 = []

                    for i in range(len(ct[key])):
                        dsz1.clear()
                        sz = ct[key][i]
                        if len(sz) == 3:
                            continue
                        for rank in sz:
                            dsz1.append(rank)
                        sz = ct['resamesuitstraight'][-(i + 1)]
                        for j in range(len(sz)):

                            if sz[-j - 1] in dsz1:
                                continue
                            else:
                                dsz1.append(sz[-j - 1])
                        print('hhhhhhhh')
                        print(dsz1)
                        slist = []
                        for j in range(len(dsz1)):
                            for k in range(5):
                                for c in dsz1[j + k]:
                                    slist.append(c)
                                    break

                            qmd.append(slist.copy())
                            mrank = dsz1[j + 4][0].rank
                            sc += getctpoint(key)
                            sc += getrankpoint(mrank) * 0.1
                            qmsc.append(sc)
                            slist.clear()
                            sc = 0
                            if j == len(dsz1) - 5:
                                break
                elif key == 'restraight' or key == 'resamesuitstraight':
                    continue
                elif key == 'samesuit':
                    for th in ct[key]:
                        if len(th) >= 5:
                            print('tonhhuaaaaaaaaaaaaaaaaaaaaaaa')

                            l = len(th)
                            sc = 0
                            tlist = []

                            for a in range(l - 4):
                                tlist.append(th[a])
                                for b in range(a + 1, l - 3):
                                    tlist.append(th[b])
                                    for c in range(b + 1, l - 2):
                                        tlist.append(th[c])
                                        for d in range(c + 1, l - 1):
                                            tlist.append(th[d])
                                            for e in range(d + 1, l):
                                                ecard = th[e]
                                                tlist.append(ecard)
                                                print('------------kkkkkkkkkkkkkkk---------')
                                                print(tlist)
                                                qmd.append(tlist.copy())
                                                mrank = ecard.rank
                                                sc += getctpoint(key)
                                                sc += getrankpoint(mrank) * 0.1
                                                qmsc.append(sc)
                                                sc = 0
                                                tlist.pop()
                                            tlist.pop()
                                        tlist.pop()
                                    tlist.pop()
                                tlist.pop()
                elif key == 'cpcp':
                    cp = ct['cp']
                    clist = []
                    sc = 0
                    for a in range(len(cp) - 1):
                        clist += cp[a]
                        arank = cp[a][0].rank
                        for b in range(a + 1, len(cp)):
                            clist += cp[b]
                            print('--------ccccc-------')
                            print(clist)
                            brank = cp[b][0].rank
                            if len(ct['single']):
                                clist += ct['single'][0]
                            else:
                                for ocp in ct['cp']:
                                    for oc in ocp:
                                        if oc not in clist:
                                            clist.append(oc)
                                            break
                                        if len(clist) == 5:
                                            break
                                    if len(clist) == 5:
                                        break
                            qmd.append(clist.copy())
                            sc += getctpoint(key)
                            bc = getrankpoint(brank)
                            sc += bc * 0.1
                            ac = getrankpoint(arank)
                            if bc - ac == 1:
                                sc += 2
                            qmsc.append(sc)
                            sc = 0
                            clist = clist[:2]
                        clist.clear()
                elif key == 'hulu':
                    hlist = []

                    for st in ct['triplets']:
                        hrank = st[0].rank
                        for cp in ct['cp']:
                            hlist = st + cp
                            print('-------ttttttttttttt----------')
                            print(hlist)
                            qmd.append(hlist.copy())
                            qmsc.append(70+getrankpoint(hrank)*0.1)
                else:
                    middle, mrank = getcard(key, ct)
                    print(middle)
                    if not middle == None:
                        sc += getctpoint(key)
                        sc += getrankpoint(mrank) * 0.1
                        if sc >= bsc:
                            print('---BIG---')
                            continue
                        qmsc.append(sc)
                        if len(middle) < 5:
                            if len(ct['single']) < 5 - len(middle):
                                continue
                            for i in range(5 - len(middle)):
                                middle += ct['single'][i]
                        qmd.append(middle.copy())
                        middle.clear()
                if key == 'bomb':
                    for st in ct['bomb']:
                        blist = []
                        hrank = st[0].rank
                        for a in range(2):
                            blist.append(st[a])
                            for b in range(a + 1, 3):
                                blist.append(st[b])
                                for c in range(b + 1, 4):
                                    blist.append(st[c])

                                    for cp in ct['cp']:
                                        hlist = blist + cp
                                        print('-------bbbbbbbbbbbbbbbbb----------')
                                        print(hlist)
                                        qmd.append(hlist.copy())
                                        qmsc.append(70 + getrankpoint(hrank) * 0.1)
                                    blist.pop()
                                blist.pop()
                            blist.pop()
            if key == 'cp':
                break
        print('---qmd---')
        print(qmd)
        for m in range(len(qmd)):
            middle = qmd[m]
            msc = qmsc[m]
            print(msc)
            print(bsc)
            if msc > bsc:
                continue
            mmmcard = mmcard.copy()
            #print('mmmmmmmm')
            #print(middle)
            #print('mmmmmmmmmm')
            '''
            for c in middle:
                mmmcard.remove(c)
            '''
            ct, mmmcard = updata(mmmcard, middle)
            head = mmmcard
            hrank = head[2].rank
            sc = 0
            for key in ct:
                sc = 0
                if key == 'cp':
                    if len(ct[key]):
                        hrank = head[1].rank
                        sc += getctpoint(key)
                        sc += getrankpoint(hrank) * 0.1
                        break
                if key == 'single':
                    hrank = head[2].rank
                    sc += getctpoint(key)
                    sc += getrankpoint(hrank) * 0.1
                    break
                if key == 'resamesuitstraight' or key == 'restraight':
                    continue
                if len(ct[key]):
                    sc += getctpoint(key)
                    #sc += getrankpoint(hrank) * 0.1
                    if sc > msc:
                        card = head[0]
                        head[0] = middle[4]
                        middle[4] = card
                        '''
                        wrong
                        '''
                    else:
                        break


            scroce = bsc + msc + sc
            if scroce > fsc:
                fb = bottom
                fm = middle
                fh = head
                fsc = scroce

            #print('----------')
            print('outcome:')
            print('后墩：')
            print(bottom)
            print('中墩：')
            print(middle)
            print('头墩：')
            print(head)
            print(scroce)
    print('--------final-------')
    print('后墩：')
    print(fb)
    print('中墩：')
    print(fm)
    print('头墩：')
    print(fh)
    print(fsc)
    return fh, fm, fb