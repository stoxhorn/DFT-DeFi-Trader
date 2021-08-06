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

def test(address):

    quicknodeHTTP = 'https://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
    quicknodeURL = 'wss://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
    w3 = Web3(Web3.HTTPProvider(quicknodeHTTP))# Web3(Web3.WebsocketProvider(quicknodeURL, websocket_kwargs = {'ping_interval':None})) # 
    # the other router address = 0x6e7a5FAFcec6BB1e78bAE2A1F0B612012BF14827
    # not many transactions mostly approving spending for some. Wonder what this is?

    address = w3.toChecksumAddress(address)


    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    block = w3.eth.get_block('latest', full_transactions = True)
    block_num = block['number']

    token = w3.toChecksumAddress('0xcd18d59e1c85258b5f86ecb5b8e7efea1682785c')
    cake = w3.toChecksumAddress('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')
    cat = w3.toChecksumAddress('0xcd18d59e1c85258b5f86ecb5b8e7efea1682785c')
    twbnb = Web3.toChecksumAddress("0xae13d989dac2f0debff460ac112a837c89baa7cd")
    # token_list = [cake, twbnb, vlha]
    
    filt1 = {'fromBlock': 0, 'toBlock': 'latest', 'address': address}
    filter = w3.eth.filter(filt1)

    print(filter.get_new_entries())
    print(w3.eth.getTransactionCount(address))
    return filter.get_all_entries()



    '''
    filt1 = {'fromBlock': 7501462, 'toBlock': 7501462, 'address': cat}
    filter = w3.eth.filter(filt1)#, 'address': token})#, 'address': w3.toChecksumAddress('0xcd18d59e1c85258b5f86ecb5b8e7efea1682785c')})


    def avg(list):
        sum = 0
        d = 0
        for i in list:
            sum += i
            d += 1
        return sum/d

    times = []
    while(True):
        blocks = filter.get_all_entries()
        for i in blocks:
            #print(blocks[0])
            t1 = time.time()
            txn_hash = w3.toHex(i['transactionHash'])
            txn = w3.eth.get_transaction(txn_hash)
            t2 = time.time() - t1
            times.append(t2)
            #print(avg(times))
            #print(txn['input'])
            print(txn_hash)
            print(txn['input'])
            print(ctime())


    # luckycat launch transaction https://bscscan.com/tx/0x5435f66194a08053fd0ecb56cead2429ea788f989d5cd4c17faf8b27d843b26f
    # luckycat token address 0xcD18d59E1C85258B5f86Ecb5B8E7EFEa1682785C
    

    txns = filter.get_all_entries()

    owner = w3.toChecksumAddress('0x6c716df5d038f0e81aa4c7ef33f87945aa110de7')
    for i in block['transactions']:
        if i['from'] == owner:
            print(i['hash'])
    '''

if __name__ == '__main__':
    print(test('0x9c8619590014D54AD9B6121dec82fF0EC949F47c'))