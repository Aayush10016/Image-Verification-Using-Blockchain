from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# ✅ Correct contract address
contract_address = "0xfDa1F49466c3fca5C8724566471F741dfbB594E6"

# ✅ CORRECT ABI (NO extra brackets)
contract_abi = [
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "hash",
          "type": "bytes32"
        }
      ],
      "name": "storeQRHash",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "name": "storedHashes",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "hash",
          "type": "bytes32"
        }
      ],
      "name": "verifyQRHash",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
]
# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Use the first Ganache account
default_account = "0xd900158e687886a56d85C438fdC8C9f0f2fF5A7E"
private_key = "0xd71dde3439c14d971ccca77911ef03d4951d49579f7d235b9f9a15cb1574b654"
