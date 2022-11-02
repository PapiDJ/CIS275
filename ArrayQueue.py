from AbstractCollection import AbstractCollection
from Array import Array

class ArrayQueue(AbstractCollection):
    DEFAULT_CAPACITY = 10
    
    def __init__(self, source_collection=None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        AbstractCollection.__init__(self, source_collection)
    
    def ensure_capacity(self):
        new_array = Array(len(self._items) * 2)
        for i in range(len(self)):
            new_array[i] = self._items[self._front]
            self._front = (self._front + 1) % len(self._items)
        self._items = new_array
        self._front = 0
        self._rear = len(self)
        
    def add(self, item):
        if self._size == len(self._items):
            self.ensure_capacity()
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % len(self._items)
        self._size += 1
        
    def pop(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        
        old_item = self._items[self._front]
        # self._items[self._front] = None
        self._items = self._items[1:]
        self._size -= 1
        return old_item
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        return self._items[self._front]
    
    def clear(self):
        self._size = 0
        self._front = 0
        self._rear = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        
    
    def __str__(self):
        return f'Front: {self._items} :Rear '