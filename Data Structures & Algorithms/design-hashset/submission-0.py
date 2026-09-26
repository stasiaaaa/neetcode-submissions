class MyHashSet:

    def __init__(self):
        self.tmp = []
        

    def add(self, key: int) -> None:
        if key not in self.tmp:
            self.tmp.append(key)

    def remove(self, key: int) -> None:
        if key in self.tmp:
            self.tmp.remove(key)        

    def contains(self, key: int) -> bool:
        if key in self.tmp:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)