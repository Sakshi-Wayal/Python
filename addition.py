def searchNode(self, value):
        curr = self.head
        while curr:
              if curr.getData() == value:
                  return True
              curr = curr.getNextNode()
        return False