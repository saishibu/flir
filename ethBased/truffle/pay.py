#Web3 and Smart Contract Interaction to transfer funds

from web3 import Web3, HTTPProvider
import json

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

accounts=web3.eth._get_accounts()
fromAddress = accounts[0]
toAddress = accounts[1]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/FLIRContract.json'

# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x645e911F16D22f8423fD79a4d565c32F139A8F28'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)


print("Old Balances")

print("Balance of 'From' Address: " +str(web3.fromWei(web3.eth.getBalance(fromAddress),'ether')))
print("Balance of 'To' Address: " +str(web3.fromWei(web3.eth.getBalance(toAddress),'ether')))

payment=contract.functions.sendViaTransfer(toAddress).transact({"from":fromAddress,"value":web3.toWei(2,'ether')})
print(payment)

print("New Balances")

print("Balance of 'From' Address: " +str(web3.fromWei(web3.eth.getBalance(fromAddress),'ether')))
print("Balance of 'To' Address: " +str(web3.fromWei(web3.eth.getBalance(toAddress),'ether')))
