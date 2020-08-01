import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.previous = None
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # TODO: Implement this method to append to the tail of the list
        if not self.head:
            self.head = Block(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
                              data, 0)
            self.tail = self.head
            return

        new_node = Block(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
                         data, self.tail.hash)
        new_node.previous = self.tail
        self.tail = new_node

    def to_list(self):

        # TODO: Write function to turn Linked List into Python List
        lst = []
        ptr = self.head
        while ptr:
            lst.append(ptr.data)
            ptr = ptr.next

        return lst


def test():
    bc = Blockchain()
    bc.append("INFO 1")
    bc.append("INFO 2")
    bc.append("INFO 3")

    print(bc.to_list())

test()