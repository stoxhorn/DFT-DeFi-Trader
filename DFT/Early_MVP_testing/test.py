import json
import web3
import time
from time import ctime
from copy import copy
from solc import compile_standard
from web3 import Web3
import threading
from web3.middleware import geth_poa_middleware
from hexbytes import HexBytes as hb
from datetime import datetime

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from funcs import load_abi

def load_abi(filename):
    abi = None
    
    with open(filename) as jsonF:
        abi = json.load(jsonF)
    return abi

quicknodeHTTP = 'https://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
quicknodeURL = 'wss://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
getblock_http = 'https://bsc.getblock.io/mainnet/?api_key=fe1f550e-6047-4810-9891-24364cb9c060'
getblock_Wss = 'wss://bsc.getblock.io/mainnet/?api_key=fe1f550e-6047-4810-9891-24364cb9c060'
# w3 = Web3(Web3.WebsocketProvider(getblock_Wss, websocket_kwargs = {'ping_interval':None})) 
w3 = Web3(Web3.HTTPProvider(getblock_http))# 
# the other router address = 0x6e7a5FAFcec6BB1e78bAE2A1F0B612012BF14827
# not many transactions mostly approving spending for some. Wonder what this is?

if(w3.isConnected()):
    print("connected")
else:
    print("not connected")

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

block = w3.eth.get_block('latest', full_transactions = True)
block_num = block['number']

token = w3.toChecksumAddress('0xcd18d59e1c85258b5f86ecb5b8e7efea1682785c')
cake = w3.toChecksumAddress('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')
wbnb = Web3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")
# token_list = [cake, twbnb, vlha]

address1 = '0x9c8619590014D54AD9B6121dec82fF0EC949F47c'
address2 = '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82'

# create token contract for cake token



print()
print(str(cake_contract.functions.balanceOf(address2).call()/decimals))

def get_token_balance(address, token):
    # create contract based on ABI used as standard. 
    abi = load_abi("token_abi.json")
    cake_contract = w3.eth.contract(abi = abi, address = cake)
    
    # get amount of decimals
    decimals = 10**(cake_contract.functions.decimals().call())
    
    return cake_contract.functions.balanceOf(address1).call()/decimals

# luckycat launch transaction https://bscscan.com/tx/0x5435f66194a08053fd0ecb56cead2429ea788f989d5cd4c17faf8b27d843b26f
# luckycat token address 0xcD18d59E1C85258B5f86Ecb5B8E7EFEa1682785C
'''

txns = filter.get_all_entries()

owner = w3.toChecksumAddress('0x6c716df5d038f0e81aa4c7ef33f87945aa110de7')
for i in block['transactions']:
    if i['from'] == owner:
        print(i['hash'])
'''