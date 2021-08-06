# python file for storing important files for later organization


# load an ABI from json file
def load_abi(filename):
    abi = None
    
    with open(filename) as jsonF:
        abi = json.load(jsonF)
    return abi


# given a token address and a wallet adress, will return the balance of said token, accounting for decimals. 
def get_token_balance(address, token):
    # create contract based on ABI used as standard. 
    abi = load_abi("token_abi.json")
    cake_contract = w3.eth.contract(abi = abi, address = cake)
    
    # get amount of decimals
    decimals = 10**(cake_contract.functions.decimals().call())
    
    return cake_contract.functions.balanceOf(address1).call()/decimals