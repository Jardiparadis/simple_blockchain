import datetime

class Block:
    def __init__(self, prev_hash, transaction) -> None:
        self._prev_hash = prev_hash
        self._transaction = transaction
        self._date = datetime.datetime.now()
        self._hash_value = 0 # sha256 of prev_hash + transaction + date 


if __name__ == "__main__":
    b1 = Block(None, "Alice gave 5€ to Bob")
    b2 = Block(b1, "Bob paid a pizza 18 € to Michel")


    pass