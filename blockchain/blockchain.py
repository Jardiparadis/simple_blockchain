from blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = []

    def add_transaction(self, transaction) -> str:
        previous_hash = ""
        if len(self.chain) != 0:
            previous_hash = self.chain[-1].get_hash()
        new_block = Block(previous_hash, transaction)
        self.chain.append(new_block)
        return new_block.get_hash()

    def get_transaction(self, hash_value):
        for block in self.chain:
            if block.get_hash() == hash_value:
                return block.get_transaction()

    def create_fake_initial_block(self, sender, receiver, nb_tokens):
        self.add_transaction([f"{sender}:{receiver}:{nb_tokens}"])

    def get_statistics(self):
        nb_tokens_per_user = {}

        for block in self.chain:
            for transaction in block.get_transaction():
                sender, receiver, nb_tokens = transaction.split(':')
                if receiver not in nb_tokens_per_user:
                    nb_tokens_per_user[receiver] = 0
                nb_tokens_per_user[receiver] += int(nb_tokens)

        return nb_tokens_per_user
