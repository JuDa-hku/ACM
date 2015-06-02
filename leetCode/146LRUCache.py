class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.key = []
        self.store = {}
        
    # @return an integer
    def get(self, key):
        if key in self.store:
            self.key.remove(key)
            self.key.append(key)
            return self.store[key]
        else:
            return -1

            
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.store:
            self.store[key] = value
            self.key.remove(key)
            self.key.append(key)
        elif key not in self.store and len(self.key)<self.cap:
            self.key.append(key)
            self.store[key] = value
        elif key not in self.store and len(self.key)==self.cap:
            rm = self.key.pop(0)
            del self.store[rm]
            self.key.append(key)
            self.store[key] = value
            
s = LRUCache(1)
print s.get(1)
s.set(1,2)
print s.get(1)
s.set(2,1)
print s.get(1)

        