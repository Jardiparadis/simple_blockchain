import datetime
import hashlib

class Block:
    def __init__(self, prev_hash, transaction) -> None:
        self._prev_hash = prev_hash
        self._transaction = transaction
        self._date = datetime.datetime.now()
        self._hash_value = hashlib.new('sha256') # sha256 of prev_hash + transaction + date
     
        if(type(self._prev_hash) == str):
            value_to_hash: str = self._prev_hash + self._transaction + self._date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            value_to_hash: str = self._prev_hash.hexdigest() + self._transaction + self._date.strftime('%Y-%m-%d %H:%M:%S')
            
        self._hash_value.update( value_to_hash.encode('utf-8')) # string.encode('utf-8')


        self._hash_value.hexdigest()






if __name__ == "__main__":
    b1 = Block("", "Alice gave 5€ to Bob")
    
    b2 = Block(b1._hash_value, "Bob paid a pizza 18 € to Michel")

    print(b1._hash_value.hexdigest())
    print(b2._hash_value.hexdigest())
    pass