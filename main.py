from blockchain.block import Block

if __name__ == "__main__":
    b1 = Block("", "Alice gave 5€ to Bob")
    
    b2 = Block(b1.get_hash(), "Bob paid a pizza 18 € to Michel")

    print(b1.get_hash())
    print(b2.get_hash())
    pass