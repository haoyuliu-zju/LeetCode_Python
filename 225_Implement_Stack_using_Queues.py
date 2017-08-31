class Queue(object):
    def __init__(self):
        self.queue = []
        
    def push(self, x):
        self.queue.append(x)
    
    def peek(self):
        return self.queue[0]
    
    def pop(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return len(self.queue) == 0

class MyStack(object):
    def __init__(self):
        self.a = Queue()
        self.b = Queue()
    
    def push(self, x):
        if self.a.empty():
            self.a.push(x)
            for _ in range(self.b.size()):
                self.a.push(self.b.pop())

        else:
            self.b.push(x)
            for _ in range(self.a.size()):
                self.b.push(self.a.pop())
            
    def pop(self):
        if self.a.empty() and self.b.empty():
            return []
        elif self.a.empty():
            return(self.b.pop())
        else:
            return(self.a.pop())
        
    def top(self):
        if self.a.empty() and self.b.empty():
            return []
        elif self.a.empty():
            return(self.b.peek())
        else:
            return(self.a.peek())
        
    def empty(self):
        return self.a.empty() and self.b.empty() == True

class MyStack2(object):
    def __init__(self):
        self.a = Queue()
        self.b = Queue()
    
    def push(self, x):
        if self.a.empty():
            self.a.push(x)
            for _ in range(self.b.size()):
                self.a.push(self.b.pop())

        else:
            self.b.push(x)
            for _ in range(self.a.size()):
                self.b.push(self.a.pop())
            
    def pop(self):
        if not self.a.empty():   ##速度会慢一点
            return(self.a.pop())
        if not self.b.empty():
            return(self.b.pop())
        
    def top(self):
        
        if not self.a.empty():    ##速度会慢一点
            return(self.a.peek())
        if not self.b.empty():
            return(self.b.peek())
        
    def empty(self):
        return self.a.empty() and self.b.empty() == True
