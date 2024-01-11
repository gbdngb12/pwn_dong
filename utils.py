from pwn import *

def get_diff(base: int, target: int) -> int :
    return target - base

def bytes_to_int(value: bytes, endian: str = 'little') -> int :
    return int.from_bytes(value, endian)

def print_bytes(bstr:str):
    print((b''.join(b'\\x%02x' % i for i in bstr)).decode())
