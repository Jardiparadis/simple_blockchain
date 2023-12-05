

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


def shift_right(n : int, x : int) -> int:
    return x >> n

def rotation_right(n : int, x : int):
    # print((bin(x)[2:]))
    x_1 : int = x >> n
    # print((bin(x_1)[2:]))

    x_2 : int = (x << (32-n))
    # print((bin(x_2)[2:]))
    return x_1 | x_2 & 0xFFFFFFFF


def ch(x: int, y: int, z:int) -> int:
    return (x & y) ^ ((~x) & z)
    
def maj(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)
    
def sigma(param: int, x:int) -> int:
    if(param == 0):
        return rotation_right(2, x) ^ rotation_right(13, x) ^ rotation_right(22, x)
    elif(param == 1):
        return rotation_right(6, x) ^ rotation_right(11, x) ^ rotation_right(25, x)
    else:
        print("error")

def rho(param: int, x: int) -> int:
    if(param == 0):
        return rotation_right(7, x) ^ rotation_right(18, x) ^ shift_right(3, x)
    elif(param == 1):
        return rotation_right(17, x) ^ rotation_right(19, x) ^ shift_right(10, x)
    else:
        print("error")

if __name__ == "__main__":
    message = "Hello, world!"
    # print(bin_representation(message=message))
    toto = int(bin_representation(message=message),base=2)
    # print(bin(toto))
    print( "0b" + (bin(rotation_right(1, toto))[2:]).zfill(8*(len(message)))  )
    pass