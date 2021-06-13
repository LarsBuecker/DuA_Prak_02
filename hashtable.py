class HashNode():
    def __init__(self, key):
        self.key = key
        self.next = None

class Hashtable():
    INITIAL_CAPACITY = 50
    def __init__(self):
        self.capacity = self.INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for i, c in enumerate(key):
            hashsum += (i + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        
        return hashsum

    def insert(self, key):
        # 1. Increment size
        self.size += 1

        # 2. Compute index of key
        index = self.hash(key)
        node = self.buckets[index]
        
        # 3. If bucket is empty:
        if node is None:
            self.buckets[index] = HashNode(key)
            print("ins true")
            return

        
        # 4. Collision -> Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            if key == node.key:
                print("ins false")
                return
            prev = node
            node = node.next

            # Add new node at the end of the list with provided key
        print("ins true")
        prev.next = HashNode(key)
        

    def delete(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # 2. Iterate to the requestet node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        
        # Node is requestet node or none
        if node is None:
            # Key not found
            print("del false")
            return None
        else:
            # 3. Key was found
            self.size -= 1
            # Delete the element in the linked list
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            
            print("del true")
            return key

    def search(self, key):
        # 1. Compute hash
        index = self.hash(key)

        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        
        #4. Node is the searched one
        if node is None:
            # Not found
            print("search false")
            return None
        else:
            # Found - return node
            print("search true")
            return node