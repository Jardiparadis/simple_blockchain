import hashlib
from blockchain.blockchain import Blockchain
import rsa
import copy


class Node:
    def __init__(self, blockchain, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        # Each node has its own blockchain copy
        self.blockchain = copy.deepcopy(blockchain)


class Network:
    def __init__(self):
        self.nodes = []

    def register_nodes(self, node):
        self.nodes.append(node)

    def transfer_token(self):
        pass


if __name__ == "__main__":
    network = Network()

    public_key_a, private_key_a = rsa.newkeys(512)
    # PKSC = Public Key Cryptographic Standards https://fr.wikipedia.org/wiki/Public_Key_Cryptographic_Standards
    pksc_a = public_key_a.save_pkcs1()
    network.register_nodes(Node(Blockchain(), public_key_a, private_key_a))

    public_key_b, private_key_b = rsa.newkeys(512)
    pksc_b = public_key_b.save_pkcs1()
    network.register_nodes(Node(Blockchain(), public_key_b, private_key_b))
