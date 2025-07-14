import hashlib
import time

blockchain = []

def make_block(index, data, prevhash):
    tm = time.time()
    stuff = str(index) + str(tm) + data + prevhash
    h = hashlib.sha256(stuff.encode()).hexdigest()
    return {
        'i': index,
        't': tm,
        'd': data,
        'ph': prevhash,
        'h': h
    }

def start():
    b0 = make_block(0, "first", "0")
    blockchain.append(b0)

start()
