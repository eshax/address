
import pymongo
import btc
import random
import binascii
import os
import requests
import json

db = pymongo.MongoClient(host='192.168.31.19', port=27017)
tb = db["address"]["btc"]

r = random.randint(0, 2**256)

# mdb.btc.insert_one({""})
while 1:
    print()
    r += 1
    # print(r)
    hr = str(hex(r))[2:]
    # print(hr)
    # hr = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321727'
    private_key = btc.get_private_key(hr)
    # print("private key: %s" % binascii.hexlify(private_key).decode().upper())
    public_key = btc.get_public_key(private_key)
    # print("public_key: %s" % binascii.hexlify(public_key).decode().upper())
    public_address = btc.get_public_address(public_key)
    bitcoin_address = btc.base58_encode("00", public_address)
    # print("bitcoin address : %s" % bitcoin_address)
    tb.insert_one({
        "private_key": binascii.hexlify(private_key).decode().upper(),
        "public_key": binascii.hexlify(public_key).decode().upper(),
        "bitcoin_address": "%s" % bitcoin_address
    })
    o = tb.find_one({"bitcoin_address": bitcoin_address}, {"_id": 0})
    print(o["private_key"])
    print(o["bitcoin_address"])
    res = requests.get("https://blockchain.info/multiaddr?active=%s" % o["bitcoin_address"])

    if res.status_code == 200:
        js = "%s" % res.text
        # print(js)
        js = json.loads(js)
        balance = js["wallet"]["final_balance"]
        for addr in js["addresses"]:
            if balance == 0:
                balance = addr["final_balance"]
        if balance > 0.0:
            db["balance"]["btc"].insert_one({"bitcoin_address": bitcoin_address, "balance": balance})
            print(balance)

    # break
