# Basic implementation of a hash map
# Separate chaining with power-of-two capacity  

from typing import Any, Hashable


class HashMap:
    def __init__(self, capacity: int = 8):
        """
        Initialise an empty HashMap object
        
        Args:
            capacity: initial table capacity, power-of-two for bitwise indexing
        """
        self._table = [[] for _ in range(capacity)]
        self._capacity = capacity
        self._size = 0
        
    def insert(self, key: Hashable, value: Any):
        """
        Insert or update a value at a given key
        
        Args:
            key:    key for storing the value
            value:  value to store with the key
            
        """
        if self._size >= 0.75 * self._capacity:
            self._increaseCapacity()
        table_index = hash(key) & (self._capacity - 1)
        slot = self._table[table_index]
        for i, key_value in enumerate(slot):
            if key_value[0] == key:
                slot[i] = (key, value)
                return
        self._table[table_index].append((key, value))
        self._size += 1
        
    def retrieve(self, key: Hashable) -> Any:
        """
        Return the value associated with a key in the HashMap
        
        Args:
            key: the key to search in the HashMap
        """
        table_index = hash(key) & (self._capacity - 1)
        slot = self._table[table_index]
        for key_value in slot:
            if key_value[0] == key:
                return key_value[1]
        raise KeyError("Key does not exist in hashmap")
            
    def remove(self, key: Hashable) -> Any:
        """
        Remove the key value pair associated with a key in the HashMap
        
        Args:
            key: the key to delete in the HashMap
            
        Returns:
            The value of the deleted entry
        """
        if self._capacity >= 8 and self._size <= 0.25 * self._capacity:
            self._decreaseCapacity()
        table_index = hash(key) & (self._capacity - 1)
        slot = self._table[table_index]
        for i, key_value in enumerate(slot):
            if key_value[0] == key:
                val = key_value[1]
                del slot[i]
                self._size -= 1
                return val
        raise KeyError("Key does not exist in hashmap")
        
    def contains(self, key: Hashable) -> bool:
        """Return whether or not the specified key exists in the table"""
        table_index = hash(key) & (self._capacity - 1)
        slot = self._table[table_index]
        for key_value in slot:
            if key_value[0] == key:
                return True
        return False
    
    def clear(self):
        """Reset the table and size"""
        self._capacity = 8
        self._size = 0
        self._table = [[] for _ in range(self._capacity)]
    
    def _increaseCapacity(self):
        """Double the table capacity and rebuild the HashMap"""
        self._capacity *= 2
        self._rebuildTable()
                
    def _decreaseCapacity(self):
        """Half the table capacity and rebuild the HashMap"""
        self._capacity //= 2
        self._rebuildTable()

    def _rebuildTable(self):
        """Rebuild the HashMap"""
        if self._capacity <= 8:
            return
        new_table = [[] for _ in range(self._capacity)]
        
        for slot in self._table:
            for item in slot:
                key, value = item[0], item[1]
                table_index = hash(key) & (self._capacity - 1)
                new_table[table_index].append((key, value))

        self._table = new_table

    ##################################
    # Below is Pythonic API, for fun #
    ##################################

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return self.contains(key)

    def __getitem__(self, key):
        return self.retrieve(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)

if __name__ == "__main__":
    # Create a new hashmap
    hm = HashMap()

    # Test insert and retrieve
    hm.insert("apple", 10)
    hm.insert("banana", 20)
    assert hm.retrieve("apple") == 10
    assert hm.retrieve("banana") == 20

    # Test update existing key
    hm.insert("apple", 30)
    assert hm.retrieve("apple") == 30

    # Test contains
    assert hm.contains("apple") is True
    assert hm.contains("cherry") is False

    # Test remove
    val = hm.remove("banana")
    assert val == 20
    try:
        hm.retrieve("banana")
    except KeyError:
        pass
    else:
        assert False, "Expected KeyError after removing 'banana'"

    # Test length
    assert len(hm) == 1

    # Test Pythonic API
    hm["cherry"] = 40
    assert hm["cherry"] == 40
    assert "cherry" in hm
    del hm["cherry"]
    assert "cherry" not in hm

    # Test resizing triggers
    for i in range(100):
        hm.insert(i, i*2)
    assert len(hm) == 101  # 1 leftover + 100 new
    for i in range(100):
        assert hm.retrieve(i) == i*2
        
    # Test clearing
    hm.clear()
    assert len(hm) == 0

    print("All tests passed")
