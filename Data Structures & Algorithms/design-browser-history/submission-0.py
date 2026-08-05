class BrowserNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = BrowserNode(homepage)
        
    def visit(self, url: str) -> None:
        node = BrowserNode(url) # init node object
        node.prev = self.current # set its trailing node to the current node
        self.current.next = node # set the current nodes pointer to our new nodes object
        self.current = node # set the current pointer to our new node object

    def back(self, steps: int) -> str:
        while steps and self.current.prev: # iterate to back of list or steps are complete
            self.current = self.current.prev # walk back along the list
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next: # same logic as back but pointing up the list instead of down
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)