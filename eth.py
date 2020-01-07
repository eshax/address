import secp256k1
import random
from Crypto.Hash import keccak

def get_eth_addr(private_key_str=None):
    if private_key_str is None:
        private_key = secp256k1.PrivateKey()
        private_key_str = private_key.serialize()
    else:
        private_key_bytes = bytes.fromhex(private_key_str)
        private_key = secp256k1.PrivateKey(private_key_bytes)
    public_key_bytes = private_key.pubkey.serialize(compressed=False)
    public_key_str = public_key_bytes.hex()
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key_bytes[1:])
    h = keccak_hash.hexdigest()
    address = '0x' + h[-40:]
    return {
        "private_key": private_key_str,
        # "public_key": public_key_str,
        "address": address
    }


if __name__ == '__main__':
    r = random.randint(0, 2**256)
    # hr = str(hex(r))[2:]
    r = r.to_bytes(32, byteorder='big').hex()
    print(r)
    # get_eth_addr(hr)
