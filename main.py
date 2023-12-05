from blockchain.blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()
    hash1 = blockchain.add_transaction(["transaction 1", "transaction 2"])
    hash2 = blockchain.add_transaction(["transaction 3"])

    print(blockchain.get_transaction(hash1))
    pass
