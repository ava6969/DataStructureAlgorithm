class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):

        lst = []
        ptr = self.head
        while ptr:
            lst.append(ptr.value)
            ptr = ptr.next

        return lst

    def flatten(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each

    def __repr__(self):
        return ' '.join([w for w in self.flatten().to_list()])


# util functions
def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


class HuffBaseNode:

    def __init__(self, weight):
        self._weight = weight
        self.code = None

    def is_leaf(self):
        return NotImplemented

    def weight(self):
        return self._weight

    def __add__(self, other):
        return self.weight() + other.weight()

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __eq__(self, other):
        return self.weight() == other.weight()


class HuffLeafNode(HuffBaseNode):
    def __init__(self, element, weight):
        super().__init__(weight)
        self.element = element
        self.visited = False

    def value(self):
        return self.element

    def is_leaf(self):
        return True

    def __repr__(self):
        return f"el: {self.element}, wt: {self._weight}"


class HuffInternalNode(HuffBaseNode):

    def __init__(self, weight, left, right):
        super().__init__(weight)
        self.left = left
        self.right = right

    def is_leaf(self):
        return False

    def __repr__(self):
        tabs = '\t'
        return f'\n{tabs}weight: {self._weight}\n{tabs}left: {self.left.__repr__()}\n{tabs}right: {self.right.__repr__()}'


class HuffTree:
    def __init__(self, node):
        self.root = node

    def _root(self):
        return self.root

    def weight(self):
        return self.root.weight()

    def __repr__(self):
        return 'root:' + self.root.__repr__()

    def __add__(self, other):
        return  self.root.weight() + other.weight()

    def __lt__(self, other):
        return self.root.weight() < other.weight()

    def __gt__(self, other):
        return self.root.weight() > other.weight()

    def __eq__(self, other):
        return self.root.weight() == other.weight()