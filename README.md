# Image-Verification-Using-Blockchain

A secure image-based verification system that leverages blockchain technology and QR codes 

## 🚀 Features

- 📤 Upload image to generate and store a **SHA-256 hash** on the **Ethereum blockchain**
- 🔐 Verify uploaded QR/image against the blockchain for authenticity
- 🔗 Uses **Ganache** as local Ethereum blockchain, **Web3.py** for interaction
- ⚡ Generates **QR code** that links to the uploaded image
- 🔎 Quick and tamper-proof validation process via blockchain smart contract
- 🧪 Simple web interface using **Flask**

---

## 🛠️ Tech Stack

| Component         | Description                                  |
|------------------|----------------------------------------------|
| Python (Flask)    | Backend web framework                        |
| Solidity          | Smart contract for hash storage & validation |
| Ganache           | Local Ethereum test blockchain               |
| Web3.py           | Python library for blockchain interaction    |
| QRCode, hashlib   | Python libraries for QR and hashing          |
| HTML/CSS/JS       | Frontend templates and forms                 |

NOTE:-Create folders for HTML file and store them in that folder by the name template

NOTE(2):- Put the deploy.js file in the folder named Scripts

NOTE(3):- Put the Solidity file in a folder named Contracts

NOTE(4):- Use ganache as the local Ethereum test blockchain

NOTE(5):- Create two empty folders Named "qrcodes" and "uploads" put those folder in a parent folder named "static"

NOTE(6):- create a virtual environment in python before running the flask script
