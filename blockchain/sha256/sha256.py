

Ksequence = (
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
)


def messageToByte(message: str) -> bytes:
    return "0x"+ message.encode('utf-8').hex()

# def bitwise_add_one(a):
#     b = 0b1
#     while b != 0:
#         carry = a&b # Carry value is calculated 
#         a = a^b # Sum value is calculated and stored in a
#         b = carry<<1 # The carry value is shifted towards left by a bit

#     return a # returns the final sum

def bin_representation(message: str) -> str:
    binary_rep = "0b" + (bin(int(messageToByte(message=message), base=16) )[2:]  ).zfill(8*(len(message)))
    return binary_rep

def padding(message:str) -> str:
    binary_rep = bin_representation(message=message)
    m = binary_rep
    # I concat a 1 as explained in the algorithm 
    m = m + "1" 
    

    l : int = len(message) * 8 # bits
    k : int = (448 - (l+1)) % 512
    
    # I fill the message with 0s
    m = m + k*"0"
    
    # I put the lenght of the original message in binary
    bin_of_l = (bin(l)[2:]).zfill(64)
    m = m + bin_of_l
    
    return m



def paddingToBlocks(padding:str) -> list[list[str]]:
    
    binary = padding[2:]
    size_of : int = 0

    lenght_message = len(binary)

    L = []

    for i in range(0, lenght_message, 512):
        block = binary[i:i+512]
        L_M = []
        for j in range(0, 512, 32):
            m_block = block[j:j+32]
            L_M.append(m_block)
            print(m_block)
            size_of += len(m_block)
        L.append(L_M)
        # print("0b" + block)
        # size_of += len(block)
        # print('\n')

    print("Total size : {}".format(size_of))
    return L


def getIV() -> list[int]:
    H_init = [
        0x6a09e667,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19
    ]
    return H_init

def get_digest(message: str):
    
    # pad message 
    # cut the result in blocks
    # initialize the hash values

    pass

if __name__ == "__main__":
    message : str = "Hello, World! My name is computer, I compute ! I am a slave and I do exactly what you want"
    
    bin_message : str = padding(message=message)
    
    L = paddingToBlocks(bin_message)

    # print(L)

    # print(bin_message)