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


def sendPayment(fromAddress, toAddress, payAmount):
	fromBal = checkBalance(fromAddress)
	if fromBal > payAmount:
		sendTXN = web3.eth.send_transaction({'to': toAddress,'from': fromAddress ,'value': payAmount})
		fromBal = checkBalance(fromAddress)
		toBal = checkBalance(toAddress)
		return ('tx_hash: {}'.format(sendTXN.hex()), fromBal,toBal)
	else:
		return "Transaction Failed: Balance too low"

def checkBalance(fromAddress):
	balance = web3.eth.getBalance(fromAddress)
	return balance

# Call contract function (this is not persisted to the blockchain)
setnPnCnEV = contract.functions.getnPnCnEV(5,3,2).call()
contract.functions.getnPnCnEV(5,3,2).transact()
print (setnPnCnEV)

Pexp1 = 200


# contract.functions.getProsumerTariff(Pexp1).buildTransaction()
getPT = contract.functions.getProsumerTariff(Pexp1).call()
contract.functions.getProsumerTariff(Pexp1).transact()
getPT = getPT/1000
print(getPT)

getCT = contract.functions.getConsumerTariff(420).call()
contract.functions.getConsumerTariff(420).transact()
getCT = getCT/1000
print(getCT)

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


#Payments to Prosumers
NGtoP1 = sendPayment(ngAddress,p1Address,web3.toWei(getPT,'ether'))
print(NGtoP1[0])

#Payments from Consumers
C1toNG= sendPayment(c1Address,ngAddress,web3.toWei(getCT,'ether'))

print("New Balances")

_balance = round(web3.fromWei(checkBalance(ngAddress),'ether'),2)
print("Nano Grid Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(c1Address),'ether'),2)
print("C1 Wallet Balance: " + str(_balance)+ " Eth")

_balance = round(web3.fromWei(checkBalance(p1Address),'ether'),2)
print("P1 Wallet Balance: " + str(_balance)+ " Eth")

