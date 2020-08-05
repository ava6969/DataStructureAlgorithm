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

    def __repr__(self):
        return f"timestamp: {self.timestamp}\n" \
               f"data:      {self.data}\n" \
               f"prev_hash: {self.previous_hash}\n" \
               f"hash:      {self.hash}\n"



class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # TODO: Implement this method to append to the tail of the list
        if data == "" or data is None:
            return

        if not self.head:
            self.head = Block(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
                              data, 0)
            self.tail = self.head
            return

        new_node = Block(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
                         data, self.tail.hash)
        self.tail.next = new_node
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def to_list(self):

        # TODO: Write function to turn Linked List into Python List
        lst = []
        ptr = self.head
        while ptr:
            lst.append(ptr)
            ptr = ptr.next

        return lst


def test2():
    bc = Blockchain()
    print(len(bc.to_list()) == 0)  # True


def test():
    bc = Blockchain()
    bc.append("INFO 1")
    print(bc.head.data == "INFO 1" ) # True
    print(len(bc.to_list()) == 1)  # True
    bc.append("INFO 2")

    bc.append("INFO 3")
    list_v = bc.to_list()
    print(list_v)

    print(list_v[1].previous_hash == list_v[0].hash) # True
    print(len(list_v) == 3)  # True

    bc.append("")
    print(len(list_v) == 3)  # True
    bc.append(None)
    print(len(list_v) == 3)  # True



test2()