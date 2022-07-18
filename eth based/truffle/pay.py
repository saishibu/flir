import json
from web3 import Web3, HTTPProvider
from hexbytes import HexBytes

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
print(web3.eth.defaultAccount)

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/FLIRContract.json'

# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x645e911F16D22f8423fD79a4d565c32F139A8F28'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

def checkBalance(fromAddress):
	balance = web3.eth.getBalance(fromAddress)
	return balance

accounts = web3.eth._get_accounts()
ngAddress = accounts[0]
c1Address = accounts[1]
p1Address = accounts[2] 

print("Old Balances")

_balance = round(web3.fromWei(checkBalance(ngAddress),'ether'),2)
print("Nano Grid Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(c1Address),'ether'),2)
print("C1 Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(p1Address),'ether'),2)
print("P1 Wallet Balance: " + str(_balance)+ " Eth")

payment=contract.functions.sendViaTransfer(p1Address)
txh=payment.transact({"from":ngAddress,"value":1})
print(payment)


print("New Balances")

_balance = round(web3.fromWei(checkBalance(ngAddress),'ether'),2)
print("Nano Grid Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(c1Address),'ether'),2)
print("C1 Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(p1Address),'ether'),2)
print("P1 Wallet Balance: " + str(_balance)+ " Eth")

