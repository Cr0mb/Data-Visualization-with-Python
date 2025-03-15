import os
import time
from mnemonic import Mnemonic
from bip32utils import BIP32Key
import hashlib

def generate_wallet():
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)
    seed = mnemo.to_seed(mnemonic_phrase, passphrase="")
    root_key = BIP32Key.fromEntropy(seed)
    child_key = root_key.ChildKey(84).ChildKey(0).ChildKey(0).ChildKey(0).ChildKey(0)
    private_key_wif = child_key.WalletImportFormat()

    pub_key = child_key.PublicKey()
    pub_key_hash = hashlib.new('ripemd160', hashlib.sha256(pub_key).digest()).digest()
    segwit_address = "bc1" + hashlib.new('ripemd160', hashlib.sha256(pub_key).digest()).hexdigest()

    return mnemonic_phrase, private_key_wif, segwit_address

while True:
    mnemonic_phrase, private_key_wif, bitcoin_address = generate_wallet()
    print("=" * 10)
    print("Mnemonic:", mnemonic_phrase)
    print("Private Key (WIF):", private_key_wif)
    print("Bitcoin Address (SegWit):", bitcoin_address)
    print("Balance: 0.000000000 BTC")
    print("=" * 10)
    print("\n")
    time.sleep(1)