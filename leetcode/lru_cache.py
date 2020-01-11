class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.age = {}
        self.time = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            self.time += 1
            self.age[key] = self.time
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data and len(self.data) == self.capacity:
            min_key = None
            min_age = None
            for ikey, iage in self.age.items():
                if min_age is None or iage < min_age:
                    min_key = ikey
                    min_age = iage
            del self.data[min_key]
            del self.age[min_key]

        self.time += 1
        self.data[key] = value
        self.age[key] = self.time


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

input = zip(
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
)

input = zip(
    ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
    [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
)

cache = None
output = []

for op, args in input:
    r = None

    if op == "LRUCache":
        cache = LRUCache(*args)
    elif op == "put":
        r = cache.put(*args)
    elif op == "get":
        r = cache.get(*args)

    output.append(r)

print(output)