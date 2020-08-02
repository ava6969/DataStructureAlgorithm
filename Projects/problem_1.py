import heapq

class ANCHOR:

    """Used as an identifier of the end and beginning of linked lists."""

    pass


class _LRUCacheLink(object):

    """Linked list object for the LRU cache."""

    __slots__ = ('left', 'right', 'key', 'obj')


class LRUCache(object):

    """LRU(Least Recently Used) Cache. O(1) Implementation.
    """

    __slots__ = ('_size', '_anchor', '_ldict')

    def __init__(self, size):
        """Constructor.
        :param size: Static size of LRU cache.
        """
        if size < 2:
            raise ValueError('Cache size can not be less than 2 elements')

        self._size = size

        # Anchor is the beginning of the cache list.
        self._anchor = _LRUCacheLink()
        self._anchor.key = ANCHOR
        self._anchor.left = self._anchor
        self._anchor.right = self._anchor

        # Map of all cache elements for fast access.
        self._ldict = {}

    def __len__(self):
        return len(self._ldict)

    def set(self, key, obj):
        """Add new item into cache."""

        if key in self._ldict:
            # Unlink item and put it as fresh element.
            item = self._move_to_top(key)
            item.obj = obj
        else:
            if len(self._ldict) >= self._size:
                # Reuse item that is going to be removed.
                new_item = self._remove_item(self._anchor.left.key)
            else:
                new_item = _LRUCacheLink()
            new_item.obj = obj
            new_item.key = key
            self._link_item_as_top(new_item)
            self._ldict[key] = new_item

    def _move_to_top(self, key):
        """Moves element to the top of the list and returns associated item."""
        item = self._ldict[key]
        l_item = item.left
        r_item = item.right
        l_item.right = r_item
        r_item.left = l_item
        self._link_item_as_top(item)
        return item

    def _link_item_as_top(self, item):
        """Set linked list item to the top of the list."""
        anchor = self._anchor
        anchor_r = anchor.right
        item.left = anchor
        item.right = anchor_r
        anchor_r.left = item
        anchor.right = item

    def _remove_item(self, key):
        """Removes item from the linked list and returns associated item."""
        item = self._ldict.pop(key)
        l_item = item.left
        r_item = item.right
        l_item.right = r_item
        r_item.left = l_item
        return item

    __delitem__ = _remove_item

    def get(self, key, default=-1):
        """Get data from cache.
        :param key: Object key.
        :param default: Default value if object not found.
        :return: Object associated with key.
        """

        if key in self._ldict:
            return self._move_to_top(key).obj
        else:
            return default


def test():
    our_cache = LRUCache(3)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.get(4)  # Expected Value = 4
    our_cache.get(1)  # Expected Value = -1
    our_cache.set(2, 4)
    our_cache.get(2)  # Expected Value = 4
    our_cache.set(5, 5)
    our_cache.get(3)  # Expected Value = -1
    our_cache.get(5)  # Expected Value = 5
    our_cache.set(2, 6)
    our_cache.get(2)  # Expected Value = 6
    our_cache.set(6, 6)
    our_cache.get(4)  # Expected Value = -1
    our_cache.get(6)  # Expected Value = 6
    our_cache.set(5, 10)
    our_cache.set(7, 7)
    our_cache.get(2)  # Expected Value = -1
    our_cache.get(7)  # Expected Value = 7
    our_cache.get(6)  # Expected Value = 6
    print(our_cache.get(5))  # Expected Value = 10 Your Output = -1

test()