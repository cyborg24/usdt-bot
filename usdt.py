from ethtoken.abi import EIP20_ABI
from web3.auto import w3
from web3 import Web3,HTTPProvider
import web3
import os
from etherscan import Etherscan
import multiprocessing as mp

def mainProg(api_key, pid, n):
    eth = Etherscan(api_key)


    w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/2428631d7b6044cd8ccfa6cbdbbbc50f'))
    unicorns = w3.eth.contract(address="0xdAC17F958D2ee523a2206206994597C13D831ec7", abi=EIP20_ABI)
    #bal = unicorns.functions.balanceOf('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3').call()
    print(pid, "==>CHECKING...")
    while 1:
        #try:
        eth_balance = eth.get_eth_balance(address="0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3")
        eth_balance = int(eth_balance) / (10**18)
        feee = int(eth_balance * 1000000000)
        print(pid, "==>BALANCE: ", eth_balance)
        print(pid, "==>FEE: ", feee)
        if (feee > 20999):
            nonce = n #w3.eth.getTransactionCount('0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3')
            print("NONCE: ", nonce)
            unicorn_txn = unicorns.functions.transfer('0x47B75EF0dD69dF42591Ba17AA5bb2A7C19175F2D', 169400000000,).buildTransaction({'chainId': 1, 'gas': feee,'gasPrice': w3.toWei('1', 'gwei'), 'nonce': nonce,})

            private_key = "ee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"
            signed_txn = w3.eth.account.signTransaction(unicorn_txn, private_key=private_key)

            whexx = w3.toHex(w3.sha3(signed_txn.rawTransaction))
            whex = signed_txn.rawTransaction
            print("TX ID: ", whex)
            w3.eth.sendRawTransaction(whex)
            print("RAW TX ID: ", whexx)
            exit()
        #except ValueError:
            #pass



if __name__ == '__main__':
    api_key1 = "38ZEGS8DSA6ADH48HWHEEPRNBQ5WTMV79A"
    api_key2 = "XYRXQIKKZHYJA6BYYY9BJKPASW2464FUFQ"
    api_key3 = "3KSDKHDR7APAF3I2NF1BSQPD834M8D7TXC"
    p1 = mp.Process(target=mainProg, args=(api_key1, 1,3999,))
    p2 = mp.Process(target=mainProg, args=(api_key2, 2,4000,))
    p3 = mp.Process(target=mainProg, args=(api_key3, 3,4001,))
    """
    p4 = mp.Process(target=mainProg)
    p5 = mp.Process(target=mainProg)
    p6 = mp.Process(target=mainProg)
    p7 = mp.Process(target=mainProg)
    """

    p1.start()
    p2.start()
    p3.start()
    """
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    """
