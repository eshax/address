
import pymongo
import btc

# mdb = pymongo.MongoClient(host='127.0.0.1', port=27017, connect=False)

private_key = btc.get_private_key("18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725")
public_key = btc.get_public_key(private_key)
public_address = btc.get_public_address(public_key)
bitcoin_address = btc.base58_encode("00", public_address)
print("Final address %s" % bitcoin_address)
