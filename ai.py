from pocket import *
from is_special import *
from choosethree import *
from httpfunction import *
import time

print('1111111111')


username = 'x'
password = '123456'
status, pid = login(username, password)

# validate(header)
for times in range(1):
    gid, card = open(header)
    print(gid)
    t1 = time.time()
    clist = card.split(' ')
    print(clist)
    mycard = []
    for c in clist:
        suit = c[0]
        s = ''
        if suit == '$':
            s = 'clubs'
        elif suit == '#':
            s = 'diamonds'
        elif suit == '*':
            s = 'spades'
        elif suit == '&':
            s = 'hearts'
        mycard.append(Card(rank=c[1:], suit=s))
    print(mycard)
    # history(header)
    #logout(header)
    # print(mycard)
    # #mycard = Licensing()
    #mycard = [Card(rank='5', suit='spades'), Card(rank='Q', suit='diamonds'), Card(rank='5', suit='clubs'), Card(rank='8', suit='spades'), Card(rank='4', suit='diamonds'), Card(rank='10', suit='spades'), Card(rank='2', suit='spades'), Card(rank='8', suit='diamonds'), Card(rank='Q', suit='spades'), Card(rank='J', suit='clubs'), Card(rank='Q', suit='hearts'), Card(rank='10', suit='clubs'), Card(rank='J', suit='diamonds')]

    print('********************')
    sdt, rdt = initdict()
    rdt = arrange(mycard, rdt)
    mycard = [] + [c for r in rdt for c in rdt[r]]
    sdt = arrangesdt(mycard, sdt)
    remycard = [c for c in reversed(mycard)]
    print('mycard:')
    print(remycard)
    print('********************')
    # print(rdt)
    ct = getct(rdt, sdt)
    print('card_tyoe:')
    print(ct)
    ######################
    # 出牌
    '''
    spc = special(ct, rdt, sdt)
    if not spc == '':
        print(spc)
        #####
        # 特殊牌出牌接口
        #####
    else:
    '''

    head, middle, bottom = getPile(mycard, rdt, sdt, ct)
    hstr = ''
    for c in head:
        if c.suit == 'clubs':
            suit = '$'
        elif c.suit == 'diamonds':
            suit = '#'
        elif c.suit == 'spades':
            suit = '*'
        else:
            suit = '&'
        hstr += ' ' + suit + c.rank
    hstr = hstr[1:]
    mstr = ''
    for c in middle:
        if c.suit == 'clubs':
            suit = '$'
        elif c.suit == 'diamonds':
            suit = '#'
        elif c.suit == 'spades':
            suit = '*'
        else:
            suit = '&'
        mstr += ' ' + suit + c.rank
    mstr = mstr[1:]
    bstr = ''
    for c in bottom:
        if c.suit == 'clubs':
            suit = '$'
        elif c.suit == 'diamonds':
            suit = '#'
        elif c.suit == 'spades':
            suit = '*'
        else:
            suit = '&'
        bstr += ' ' + suit + c.rank
    bstr = bstr[1:]
    print(hstr)
    print(mstr)
    print(bstr)
    submit(header, gid, hstr, mstr, bstr)
    page = 1
    hislist = getHglist(header, pid, page, limit=100)
    print(pid)
    print(type(pid))
    print(gid)
    print(hislist)
    #getHgmore(header, gid)
t2 = time.time()
print(t2 - t1)
#[Card(rank='K', suit='hearts'), Card(rank='K', suit='clubs'), Card(rank='J', suit='diamonds'), Card(rank='10', suit='hearts'), Card(rank='9', suit='spades'), Card(rank='7', suit='hearts'), Card(rank='4', suit='hearts'), Card(rank='4', suit='clubs'), Card(rank='3', suit='diamonds'), Card(rank='3', suit='spades'), Card(rank='2', suit='spades'), Card(rank='2', suit='hearts'), Card(rank='2', suit='clubs')]
