#### 구현 리스트
# 1. 이중연결리스트 Doubly Linked List

class DLLNode:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.node_count = 0
        self.head = DLLNode(None)
        self.tail = DLLNode(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
    

    def __repr__(self):
        return 'Linked List: ' + str(self.traverse())
    

    def __len__(self):
        return self.getLength()
                

    def getLength(self):
        return self.node_count
    

    def getAt(self, pos):
        if pos < 0 or pos > self.node_count:
            raise IndexError
        
        if pos <= self.node_count // 2:
            i = 0
            curr = self.head
            
            while i < pos:
                curr = curr.next
                i += 1
        
        else:
            i = self.node_count
            curr = self.tail

            while i >= pos:
                curr = curr.prev
                i -= 1

        return curr
    

    def insertAt(self, pos, x):
        if pos < 1 or pos > self.node_count + 1:
            raise IndexError
        
        if not isinstance(x, DLLNode):
            x = DLLNode(x)
        prev = self.getAt(pos - 1)
        self.insertAfter(prev, x)

        return True
    

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

        self.node_count += 1

        return True
    

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

        self.node_count += 1

        return
    

    def popAt(self, pos=1):

        if pos < 1 or pos > self.node_count:
            raise IndexError
        
        elif pos == 1:
            return self.popAfter(self.head)
        
        else:
            prev = self.getAt(pos-1)
            return self.popAfter(prev)
    

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next

        prev.next = next
        next.prev = prev

        curr.prev = None
        curr.next = None
        
        self.node_count -=1

        return curr
    

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev

        prev.next = next
        next.prev = prev

        curr.prev = None
        curr.next = None

        self.node_count -=1
        
        return curr
    

    def concat(self, L):
        prev = self.getAt(self.node_count)
        next = L.getAt(1)
        
        prev.next = next
        next.prev = prev

        self.node_count += L.node_count

        return True


    def traverse(self):
        
        if self.node_count == 0:
            return []
        
        else:
            result = []
            curr = self.head.next

            while curr.data is not None:
                result.append(curr.data)
                curr = curr.next

            return result
    

    def reverse(self):

        if self.node_count == 0:
            return []
        
        else:
            result = []
            curr = self.tail.prev

            while curr.data is not None:
                result.append(curr.data)
                curr = curr.prev

            return result

        return
    


# 2. 스택 (이중연결리스트 활용) Stack

class Stack(DoublyLinkedList):
    
    def __init__(self):
        super().__init__()


    def __repr__(self):
        return 'Stack: ' + str(self.traverse())
    

    @property
    def size(self):
        return self.getLength()
    

    def isEmpty(self):
        return self.size() == 0
    

    def push(self, x):
        node = DLLNode(x)
        self.insertBefore(self.tail, node)
        print(self)
    

    def pop(self):
        return self.popBefore(self.tail)
    

    def peek(self):
        return self.getAt(self.node_count)



# 3. 큐 Queue 

class Queue(DoublyLinkedList):

    def __init__(self):
        super().__init__()


    def __repr__(self):
        return 'Queue: ' + str(self.traverse())


    @property
    def size(self):
        return self.getLength()


    def isEmpty(self):
        return self.size == 0


    def enqueue(self, x):
        node = DLLNode(x)
        self.insertBefore(self.tail, node)


    def dequeue(self):
        return self.popAt()


    def peek(self):
        return self.getAt(1)



# 4. 환형큐 Circular Queue

class CircularQueue:

    def __init__(self, n):
        self.max_count = n
        self.data = [None] * self.max_count
        self.count = 0
        self.front = -1
        self.rear = -1


    def __len__(self):
        return self.count
    

    @property
    def size(self):
        return self.count, self.max_count


    def isEmpty(self):
        return self.size[0] == 0


    def isFull(self):
        return self.size[0] == self.size[1]
    

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue Full')

        self.rear = (self.rear + 1) % self.max_count
        self.data[self.rear] = x
        self.count += 1


    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        
        self.front = (self.front + 1) % self.max_count
        self.count -= 1

        return self.data[self.front]


    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        
        return self.data[self.front + 1]


# 5. 이진트리 Binary Tree

class TreeNode:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1


    def inorder(self):
        traversal = []

        if self.left:
            traversal += self.left.inorder()

        traversal.append(self.data)

        if self.right:
            traversal += self.right.inorder()

        return traversal


    def preorder(self):
        traversal = []

        traversal.append(self.data)

        if self.left:
            traversal += self.left.preorder()

        if self.right:
            traversal += self.right.preorder()

        return traversal


    def postorder(self):
        traversal = []

        if self.left:
            traversal += self.left.postorder()

        if self.right:
            traversal += self.right.postorder()

        traversal.append(self.data)

        return traversal


class BinaryTree:

    def __init__(self, root):
        if not isinstance(root, TreeNode):
            root = TreeNode(root)
        self.root = root


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        if self.root:
            return self.root.depth()
        
        else: return 0


    def inorder(self):
        if self.root:
            return self.root.inorder()
        
        else: return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        
        else: return []


    def postorder(self):
        if self.root:
            return self.root.postorder()
        
        else: return []


    def bft(self):
        traversal = []

        q = Queue()
        q.enqueue(self.root)

        while not q.isEmpty():
            visit = q.dequeue()
            traversal.append(visit.data.data)
            if visit.data.left:
                q.enqueue(visit.data.left)
            if visit.data.right:
                q.enqueue(visit.data.right)

        return traversal



# 6. 이진검색트리 Binary Search Tree

class BSTNode(TreeNode):

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    
    def inorder(self):
        return super().inorder()


    def min(self):

        if self.left:
            return self.left.min()
        
        else:
            return self

    
    def max(self):
        
        if self.right:
            return self.right.max()
        
        else:
            return self


    def lookup(self, key, parent=None): # 키값을 받으면 해당 노드 및 부모 노드 반환
        
        if key < self.key:

            if self.left:
                self.left.lookup(key, self)
            
            else:
                print('no data')
                return None, None
        
        elif key > self.key:

            if self.right:
                self.right.lookup(key, self)

            else:
                print('no data')
                return None, None
        
        else:
            print('Found Data')
            return self, parent


    def insert(self, key, data):
        
        if key > self.key:
            if self.right:
                self.right.insert(key, data)
            
            else:
                self.right = BSTNode(key, data)

        elif key < self.key:
            if self.left:
                self.left.insert(key, data)

            else:
                self.left = BSTNode(key, data)

        else:
            raise KeyError

    
    def count_children(self):
        count = 0
        
        if self.left:
            count += 1
        
        if self.right:
            count += 1

        return count



class BinarySearchTree:

    def __init__(self):
        self.root = None


    def inorder(self):
        
        if self.root:
            return self.root.inorder()
        
        else:
            return []


    def min(self):
        
        if self.root:
            return self.root.min()
        
        else:
            return None


    def max(self):
        
        if self.root:
            return self.root.max()
        
        else:
            return None


    def lookup(self, key): # 키값을 받으면 해당 노드 및 부모 노드 반환
        
        if self.root:
            return self.root.lookup(key)
        
        else:
            return None, None


    def insert(self, key, data):
        
        if self.root:
            self.root.insert(key, data)
        
        else:
            self.root = BSTNode(key, data)


    def remove(self):
        pass



# 7. 힙(최대/최소) MaxHeap/ MinHeap

class MaxHeap:

    def __init__(self):
        pass


    def insert(self, item):
        pass


    def remove(self):
        pass


class MinHeap:

    pass



# 8. 최대힙을 활용한 우선순위큐 Priority Queue using Heap

class PriorityQueue:

    pass



# 9. 힙 정렬 Heap Sort

def HeapSort():
    
    pass