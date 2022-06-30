from ethtoken.abi import EIP20_ABI
from web3.auto import w3
from web3 import Web3,HTTPProvider
import web3
import os

w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/2428631d7b6044cd8ccfa6cbdbbbc50f'))
unicorns = w3.eth.contract(address="0xdAC17F958D2ee523a2206206994597C13D831ec7", abi=EIP20_ABI)
#bal = unicorns.functions.balanceOf('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3').call()
"""
bal = w3.eth.getBalance('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3')
balc = int(bal) / (10**18)
print("BALANCE: ", bal)
print("CONVERTED BALANCE: ", balc)
exit()
"""
print("CHECKING...")
while 1:
    try:
        #bal = w3.eth.getBalance('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3')
        #balc = int(bal) / (10**18)

        #if (balc > 0.0001):
        nonce = w3.eth.getTransactionCount('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3')  
        #print("BALANCE: ", bal)
        #print("CONVERTED BALANCE: ", balc)
        # Build a transaction that invokes this contract's function, called transfer
        unicorn_txn = unicorns.functions.transfer('0x47B75EF0dD69dF42591Ba17AA5bb2A7C19175F2D', 169400000000,).buildTransaction({'chainId': 1, 'gas': 4000,'gasPrice': w3.toWei('1', 'gwei'), 'nonce': nonce,})

        private_key = "ee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"
        signed_txn = w3.eth.account.signTransaction(unicorn_txn, private_key=private_key)

        whexx = w3.toHex(w3.sha3(signed_txn.rawTransaction))
        whex = signed_txn.rawTransaction
        print("TX ID: ", whex)
        w3.eth.sendRawTransaction(whex)
        print("RAW TX ID: ", whexx)
        #exit()
    except ValueError:
        pass
        
 
