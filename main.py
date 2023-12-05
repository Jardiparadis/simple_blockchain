import hashlib
from blockchain.blockchain import Blockchain
import rsa


if __name__ == "__main__":
    blockchain = Blockchain()

    public_key_a, private_key_a = rsa.newkeys(512)
    # PKSC = Public Key Cryptographic Standards https://fr.wikipedia.org/wiki/Public_Key_Cryptographic_Standards
    pksc_a = public_key_a.save_pkcs1()

    public_key_b, private_key_b = rsa.newkeys(512)
    pksc_b = public_key_b.save_pkcs1()

    signature_a = rsa.sign(b"user1", private_key_a, "SHA-1")
    signature_b = rsa.sign(b"user2", private_key_b, "SHA-1")

    # Create magic tokens to test transfer
    blockchain.create_token(pksc_a, 20)
    blockchain.create_token(pksc_b, 20)

    blockchain.transfer_token(pksc_a, pksc_b, 12, b"user1", signature_a)
    blockchain.transfer_token(pksc_b, pksc_a, 4, b"user2", signature_b)
