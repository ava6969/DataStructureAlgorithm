import heapq
import sys
from collections import Counter
from customDS import *


def heapify(freq_table):
    h = []
    for el, wt in freq_table.items():
        heapq.heappush(h, HuffTree(HuffLeafNode(el, wt)))
    return h


def build_tree(data):
    tmp3 = None
    huffman = Counter(data)
    h = heapify(huffman)

    while len(h) > 1:
        tmp1 = heapq.heappop(h)
        tmp2 = heapq.heappop(h)
        tmp3 = HuffTree(HuffInternalNode(tmp1 + tmp2, tmp1._root(), tmp2._root()))
        heapq.heappush(h, tmp3)
    return tmp3


def encode_tree(tree):
    hash_table = {}

    def traverse(node, code=''):
        if node.is_leaf():
            hash_table[node.element] = code
            return

        traverse(node.left, code + '0')
        traverse(node.right, code+ '1')

    traverse(tree.root)
    return hash_table

def huffman_decoding(data, tree):
    def traverse(node, data, root, decoded_text=''):

        if data == '':
            decoded_text += node.element
            return decoded_text

        elif node.is_leaf():
            decoded_text += node.element
            return traverse(root, data, root, decoded_text)

        elif data[0] == '0':
            return traverse(node.left, data[1:], root, decoded_text)
        elif data[0] == '1':
            return traverse(node.right, data[1:], root, decoded_text)

    decoded_text = traverse(tree.root, data, tree.root)
    return decoded_text


def huffman_encoding(data):
    raw_data = data
    tree = build_tree(data)
    table = encode_tree(tree)
    encoded_data = ''.join([table[c] for c in raw_data])
    return tree, encoded_data


def test1():
    data = 'dbdbbeeeaaacceeeaaaacccccakl'
    tree, enc_data = huffman_encoding(data)
    decoded_data = huffman_decoding(enc_data, tree)
    print(f"Original Data {data}")
    print(f"Encoded Data {enc_data}")
    print(f"Decoded Data {decoded_data}")


def test2():
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    tree, encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

test2()
test1()
