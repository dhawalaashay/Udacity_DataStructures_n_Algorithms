The following is an explanation of "Huffman Coding" implemented(priority queue) as part of the project - "Show me the Data Structures"

1)  To determine the frequency of each character in the given string, would take O(n), n being the length of the string

2)  Traversal from root to a node with a specific value would take - O(log(n)) time  
    The while loop  used in building the huffman tree. This by itself has a complexity of O(N) then inside the loop, the priorityq.delete() method is used. 


  # for popping an element based on Priority
    def delete(self):
        try:
            self.queue.sort()
            item = self.queue[0]
            del self.queue[0]
            return item
        except IndexError:
            print()
            exit()
  In this method, an in-built pyhton method (sort()) is used. This method has a time complexity of O(N(Log(n))). Hence, the overall time complexity is O(N(Log(n))) * O(N)
  