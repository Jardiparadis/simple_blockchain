from blockchain.blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.create_fake_initial_block("A", "B", 12)
    blockchain.create_fake_initial_block("C", "B", 12)

    print(blockchain.get_statistics())
