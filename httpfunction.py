import requests
import json
from urllib import parse
import re

token = ''
gid = 0
header = {
            'content-type': 'application/json',
            "X-Auth-Token": token
        }
def login(username, password):
    global pid
    url = "https://api.shisanshui.rtxux.xyz/auth/login"
    headers = {
        'content-type': 'application/json'
    }
    data = {
        "username": username,
        "password": password
    }
    respond = requests.post(url, json=data).text
    print(respond)
    res = json.loads(respond)
    status = -1
    status = res['status']
    pid = 0
    if status == 0:
        token = res['data']['token']
        print(type(token))

        pid = int(res['data']['user_id'])
        print(token)
        header['X-Auth-Token'] = token
    return status, pid




def register(username, password):
    url = 'https://api.shisanshui.rtxux.xyz/auth/register'
    data = {
        "username": username,
        "password": password
    }
    print(data)
    respond = requests.post(url, json=data).text
    print(respond)
    res = json.loads(respond)
    status = res['status']
    id = 0
    if status == 0:
        st, id = login(username, password)
        if st == 0:
            return True, id
    else:
        return False, id


def validate(header):
    u = 'https://api.shisanshui.rtxux.xyz/auth/validate'

    response = requests.get(url=u, headers=header).text
    print(response)
    return json.loads(response)


def logout(header):
    url = 'https://api.shisanshui.rtxux.xyz/auth/logout'
    data ={}
    respond = requests.post(url, json=data).text
    print(respond)


def open(header):
    url = 'https://api.shisanshui.rtxux.xyz/game/open'

    respond = requests.post(url, headers=header).text
    print(respond)
    res = json.loads(respond)
    return res['data']['id'], res['data']['card']


def getHglist(header, playerid, page, limit=4):
    url = "https://api.shisanshui.rtxux.xyz/history"
    print(limit)
    querystring = {
        "page": page,
        "limit": limit,
        "player_id": playerid
    }
    respones = requests.request('GET', url, headers=header, params=querystring).text
    print(respones)
    return json.loads(respones)

def getHgmore(header, gameid):
    url = "https://api.shisanshui.rtxux.xyz/history/" + str(gameid)
    print(url)
    response = requests.request("GET", url, headers=header).text
    print(response)

def httprank(header):
    url = "https://api.shisanshui.rtxux.xyz/rank"
    response = requests.get(url, headers=header).text
    print(response)
    res = json.loads(response)
    return res
def submit(header, gid, hstr, mstr, bstr):
    url = 'https://api.shisanshui.rtxux.xyz/game/submit'
    data = {
        "id": gid,
        "card": [
            hstr,
            mstr,
            bstr
        ]
    }
    response = requests.request('POST', url, data=json.dumps(data), headers = header).text
    print(response)
if __name__ == '__main__':

    username = 'x'
    password = '123456'


    #register(username, password)
    status, pid = login(username, password)
    print(pid)
    httprank(header)
    validate(header)
    #gid, card = open(header)
    page = 1
    print(pid)
    hislist = getHglist(header, pid, page=3, limit=4)
    print(hislist)
    #print(hislist['data'])
    #getHgmore(header, 5347)
    logout(header)
