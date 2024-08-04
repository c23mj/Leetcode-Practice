class Node:
    def __init__(self, prev: 'Node' = None, next: 'Node' = None, key: int = 0, val: int = -1):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()

    def get(self, key: int) -> int:
        if key in self.map:
            self.__prioritize(key)
            return self.map[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.__prioritize(key)
            self.map[key].val = value
        else:
            self.size += 1
            if self.size > self.capacity:
                toDelete = self.tail.prev
                self.tail.prev = toDelete.prev
                self.tail.prev.next = self.tail
                del self.map[toDelete.key]

            self.map[key] = Node(key = key, val = value)
            self.__prioritize(key)

    def __prioritize(self, key: int) -> None:
        # print(f"prioritize called on key {key}")
        curr = self.map[key]
        if curr.prev and curr.next:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next.prev = curr
        self.head.next=curr
        
        # tmp = self.head
        # print_list = []
        # while tmp:
        #     print_list.append(str(tmp.val))
        #     tmp = tmp.next
        # out = '->'.join(print_list)
        # print(f'new priorities: {out}')

