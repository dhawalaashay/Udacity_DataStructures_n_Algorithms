import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    # calculating hash value with - data of the block and timestamp at which it was created
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"We are going to encode this string of data - {self.data} and {self.timestamp}!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    # to check the starting block of the blockchain
    def __init__(self):
        self.start = None

    # print the blocks of the blockchain as a list, the list contains the block object
    def to_list(self):
        out_block = list()
        block = self.start
        while block:
            out_block.append(block)
            block = block.next
        return out_block


# it expects list of tuple: [(timestamp, data, previous_hash), (timestamp, data, previous_hash)]
def create_BlockChain(block_list):
    end = None
    start = None
    for item in block_list:
        if start is None:
            start = Block(*item)
            end = start
        else:
            end.next = Block(*item)
            end = end.next
    return start


if __name__ == "__main__":
    # test case 1
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    block1 = Block(timestamp, "my block1")

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    block2 = Block(timestamp, "my block2", block1.hash)

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    block3 = Block(timestamp, "my block3", block2.hash)
    chain = list()
    chain.append((block1.timestamp, block1.data, None))
    chain.append((block2.timestamp, block2.data, block2.previous_hash))
    chain.append((block3.timestamp, block3.data, block3.previous_hash))

    block = create_BlockChain(chain)
    while block is not None:
        print(f"data of the block :'{block.data}' has a hash value of {block.hash} \
        and a previous hash - {block.previous_hash}")
        block = block.next
    print("\n***********************************************\n")
    # testcase 2, blockchain with empty block data
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # creating block with no data
    block4 = Block(timestamp, "")

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    block5 = Block(timestamp, "my block5", block4.hash)

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    block6 = Block(timestamp, "my block6", block5.hash)
    chain = list()
    chain.append((block4.timestamp, block4.data, None))
    chain.append((block5.timestamp, block5.data, block5.previous_hash))
    chain.append((block6.timestamp, block6.data, block6.previous_hash))

    block = create_BlockChain(chain)
    while block is not None:
        print(f"data of the block :'{block.data}' has a hash value of {block.hash} \
            and a previous hash - {block.previous_hash}")
        block = block.next

    print("\n***********************************************\n")
    # testcase 3, blockchain with same timestamp
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # creating block with no data
    block7 = Block(timestamp, "my block7")
    block8 = Block(timestamp, "my block8", block7.hash)
    block9 = Block(timestamp, "my block9", block8.hash)
    chain = list()
    chain.append((block7.timestamp, block7.data, None))
    chain.append((block8.timestamp, block8.data, block8.previous_hash))
    chain.append((block9.timestamp, block9.data, block9.previous_hash))

    block = create_BlockChain(chain)
    while block is not None:
        print(f"data of the block :'{block.data}' has a hash value of {block.hash} \
                and a previous hash - {block.previous_hash}")
        block = block.next