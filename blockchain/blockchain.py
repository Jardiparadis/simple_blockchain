from blockchain.block import Block
import rsa


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

    def get_token_for_user(self, public_key):
        user_tokens = 0

        for block in self.chain:
            for transaction in block.get_transaction():
                sender, receiver, nb_tokens = transaction.split(':')
                if receiver == public_key:
                    user_tokens += int(nb_tokens)
                if sender == public_key:
                    user_tokens -= int(nb_tokens)
        return user_tokens

    def create_token(self, public_key, nb_tokens):
        # sender "#" does not exist, these tokens appeared magically
        self.add_transaction([f"#:{public_key.decode()}:{nb_tokens}"])

    def transfer_token(self, sender_key, receiver_key, nb_tokens, message, signature):
        # Check if signature is verified
        try:
            sender_public_key = rsa.PublicKey.load_pkcs1(sender_key)
            rsa.verify(message, signature, sender_public_key)
        except rsa.pkcs1.VerificationError:
            return print('Verification failed, abort token transfer.')
        # Check is sender has enough tokens
        sender_tokens = self.get_token_for_user(sender_key.decode())
        if sender_tokens < nb_tokens:
            return print('Sender has not enough token, abort token transfer.')
        # Transfer tokens
        self.add_transaction([f"{sender_key.decode()}:{receiver_key.decode()}:{nb_tokens}"])

    def get_tokens_per_user(self):
        nb_tokens_per_user = {}

        for block in self.chain:
            for transaction in block.get_transaction():
                sender, receiver, nb_tokens = transaction.split(':')
                if receiver not in nb_tokens_per_user:
                    nb_tokens_per_user[receiver] = 0
                if sender not in nb_tokens_per_user:
                    nb_tokens_per_user[sender] = 0
                nb_tokens_per_user[receiver] += int(nb_tokens)
                nb_tokens_per_user[sender] -= int(nb_tokens)

        return nb_tokens_per_user
