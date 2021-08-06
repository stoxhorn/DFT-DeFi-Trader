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

class Tools:

    def __init__(self):
        quicknodeHTTP = 'https://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
        quicknodeURL = 'wss://billowing-muddy-glade.bsc.quiknode.pro/0c1d1395d189ab42e9a03901bed0ff61a6b9e774/'
        getblock_http = 'https://bsc.getblock.io/mainnet/?api_key=fe1f550e-6047-4810-9891-24364cb9c060'
        getblock_Wss = 'wss://bsc.getblock.io/mainnet/?api_key=fe1f550e-6047-4810-9891-24364cb9c060'
        # w3 = Web3(Web3.WebsocketProvider(getblock_Wss, websocket_kwargs = {'ping_interval':None})) 
        self.w3 = Web3(Web3.HTTPProvider(getblock_http))# 
        # the other router address = 0x6e7a5FAFcec6BB1e78bAE2A1F0B612012BF14827
        # not many transactions mostly approving spending for some. Wonder what this is?

        if(self.w3.isConnected()):
            print("connected")
        else:
            print("not connected")

        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        self.tokens = {'cake': self.w3.toChecksumAddress('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'), 'wbnb': self.w3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")}

        self.address = None

        self.balances = None

    def set_address(self, address):
        self.address = self.w3.toChecksumAddress(address)


    def load_abi(self, filename):
        abi = None

        with open(filename) as jsonF:
            abi = json.load(jsonF)
        return abi

    def get_token_balance(self, token):
        # create contract based on ABI used as standard. 
        abi = self.load_abi("token_abi.json")
        cake_contract = self.w3.eth.contract(abi = abi, address = token)
        
        # get amount of decimals
        decimals = 10**(cake_contract.functions.decimals().call())
        
        return cake_contract.functions.balanceOf(self.address).call()/decimals

    def get_total_token_balances(self):
        dic = {}
        for i in self.tokens:
            tmp = self.get_token_balance(self.tokens[i])
            dic[i] = tmp
        self.balances = dic

    def add_token(self, name, address):
        if name in self.tokens:
            return False
        else:
            self.tokens[name] = self.w3.toChecksumAddress(address)
            return True

    def get_balances(self):
        return copy(self.balances)