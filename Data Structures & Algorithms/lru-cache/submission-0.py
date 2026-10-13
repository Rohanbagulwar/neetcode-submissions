class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.time = 0   # global counter to track recency

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # update recency
        self.time += 1
        self.cache[key]['used'] = self.time
        return self.cache[key]['val']

    def put(self, key: int, value: int) -> None:
        self.time += 1

        # if key already exists → update value & recency
        if key in self.cache:
            self.cache[key]['val'] = value
            self.cache[key]['used'] = self.time
            return

        # if cache is full → evict LRU
        if len(self.cache) == self.capacity:
            # remove least recently used
            lru_key = min(self.cache, key=lambda k: self.cache[k]['used'])
            self.cache.pop(lru_key)

        # insert new key
        self.cache[key] = {'used': self.time, 'val': value}
        
