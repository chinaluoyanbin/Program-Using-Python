class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hash[key] = {}
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.hash:
            self.hash.pop(key)
        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hash:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
# obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
