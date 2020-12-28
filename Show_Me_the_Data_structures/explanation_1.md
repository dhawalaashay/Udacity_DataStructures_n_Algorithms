The following is an explanation of "LRU cache" implemented as part of the project - "Show me the Data Structures"

The implemented cache is a hash table where key is the element to be found and value being an doubly Linked list node.

for example: if 2 elements are in cache such as :
"a" = 1
"b" = 2

they are implemented as:
"a" = (a -> 1) head of the doubly linked list
"b" = (b -> 2) tails of the doubly linked list

Insertion of key in the function insertKeyValuePair(key, value) : O(1) time | O(1) space - similar to normal hash map.

Retrieving value from the cache in the function getValueFromKey(key) : O(1) time | O(1) space - similar to normal hash map.

Updating(deleting/adding a node) the doubly Linked List happens to be in constant time, i.e. O(1) as we have 2 pointers respectively
for head and tail, so traversing is not required