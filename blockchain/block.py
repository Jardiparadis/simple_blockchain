import datetime
import hashlib


class Block:
    def __init__(self, prev_hash, transaction) -> None:
        self._prev_hash = prev_hash
        self._transaction = transaction
        self._date = datetime.datetime.now()
        self._hash_value = hashlib.new('sha256') # sha256 of prev_hash + transaction + date
     
        value_to_hash: str = self._prev_hash + "".join(self._transaction) + self._date.strftime('%Y-%m-%d %H:%M:%S')
            
        self._hash_value.update(value_to_hash.encode('utf-8')) # string.encode('utf-8')

        self._hash_value.hexdigest()

    def get_hash(self) -> str:
        return self._hash_value.hexdigest()

    def get_transaction(self) -> list[str]:
        return self._transaction
