import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
# print(web3.eth.defaultAccount)
# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/FLIRContract.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x645e911F16D22f8423fD79a4d565c32F139A8F28'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)

# setnPnCnEV = contract.functions.getnPnCnEV(5,3,2).call()
# print(setnPnCnEV)

# Pexp1 = 200


# # contract.functions.getProsumerTariff(Pexp1).buildTransaction()
# getPT = contract.functions.getProsumerTariff(Pexp1).call()
# print(getPT)


# getCT = contract.functions.getConsumerTariff(420).call()
# print(getCT)

accounts = web3.eth._get_accounts()
print(accounts)
# print(type(accounts))


_address = "0x5eb1f05Bb1713A68bd0E3b23540Ccd8b7971c29d"
getBal = contract.functions.getBalance(accounts[0]).call()
print(getBal)

_balance = web3.eth.getBalance(accounts[1])
print(_balance)

# sendTXN = web3.eth.send_transaction({'to': accounts[1],'from': accounts[0],'value': '10000000000000000'})
# print(sendTXN)



# getSellerID = contract.functions.sellerID(1).call()
# print(getSellerID)

# getSeller = contract.functions.getSellers().call()
# print(getSeller)
