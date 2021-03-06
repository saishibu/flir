from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed
import time
url="http://sai-iota.duckdns.org:14265"
rseed="ZIKXTJTKXRVPZIZQZYXTH9YJPCTEHP9HTFTBCPMXSK9HPHTNQBUIRAHAVPXRYPXZXRCVFZTUPQTIILITJ"
sseed="LZZNXWOZYEINHUSZLCMCVM9SMXLQALEZ9FAIUU9NFTRRCIFVPAIXEBYFMCSCGBQTPAEHU9RVUSXWMFXGO"
# def send(rseed,sseed,amount,message):
rapi = Iota(url,rseed)
sapi = Iota(url,sseed)
receiver = rapi.get_new_addresses()
receiver=receiver['addresses'][0]
print(receiver)
tx = ProposedTransaction(address=Address(receiver), message=TryteString.from_unicode("message"),tag=Tag('VALUETX'),value=int(100))
input = sapi.get_inputs(start=0, stop=10)
inputs = input['inputs']
print(input)
tx = sapi.prepare_transfer(transfers=[tx], inputs=inputs)
process = sapi.send_trytes(tx['trytes'], depth=1, min_weight_magnitude=9)
#   return "Transaction Success"

# txn=send("LZZNXWOZYEINHUSZLCMCVM9SMXLQALEZ9FAIUU9NFTRRCIFVPAIXEBYFMCSCGBQTPAEHU9RVUSXWMFXGO","ZIKXTJTKXRVPZIZQZYXTH9YJPCTEHP9HTFTBCPMXSK9HPHTNQBUIRAHAVPXRYPXZXRCVFZTUPQTIILITJ",100,"test")
# print(txn)
  
