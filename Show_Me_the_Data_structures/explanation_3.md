The following is an explanation of "Huffman Coding" implemented(priority queue) as part of the project - "Show me the Data Structures"

1)  To determine the frequency of each character in the given string, would take O(n), n being the length of the string

2)  Popping out an element which has the minimum value, after sorting(O(log(n))) will be O(1), therefore net time complexity - O(log(n)) | O(n) space,rearrange the queue after deleting first element.

3)  Traversal from root to a node with a specific value would take - O(log(n)) time

Total time complexity would be nlog(n), where n is the number of unique characters

Conclusion:

For every encoded symbol we have to traverse the tree in order to decode that symbol. If the tree contains k nodes and, on average, it takes O(log k) node visits to decode a symbol. So the time complexity would be O(n log k).
Space complexity is O(k) for the tree and O(n) for the decoded text.