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

def addblock():
    data = input("Type something to store: ")
    last = blockchain[-1]
    nb = make_block(len(blockchain), data, last['h'])
    blockchain.append(nb)
    print("done")

def see_chain():
    for b in blockchain:
        print("idx:", b['i'])
        print("time:", b['t'])
        print("data:", b['d'])
        print("prev_hash:", b['ph'])
        print("hash:", b['h'])
        print("--------------------------")

def check_chain():
    good = True
    for i in range(1, len(blockchain)):
        now = blockchain[i]
        before = blockchain[i - 1]
        comb = str(now['i']) + str(now['t']) + now['d'] + now['ph']
        if now['h'] != hashlib.sha256(comb.encode()).hexdigest():
            print("hash wrong at block", i)
            good = False
        if now['ph'] != before['h']:
            print("link broken at block", i)
            good = False
    if good:
        print("chain fine")
    else:
        print("chain broken")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add block")
        print("2. Display chain")
        print("3. Check chain")
        print("4. Bye")

        ch = input("Enter choice: ")

        if ch == "1":
            addblock()
        elif ch == "2":
            see_chain()
        elif ch == "3":
            check_chain()
        elif ch == "4":
            break
        else:
            print("what? try again")

start()
menu()
