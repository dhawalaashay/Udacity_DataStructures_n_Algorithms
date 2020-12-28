The following is an explanation of "File Recursion" implemented as part of the project - "Show me the Data Structures"

The time complexity of the implementation is linear i.e. O(N)

This implementation  is similar to a simple depth-first search tree traversal algorithm where the folders and sub-folders in your input data represent the parent nodes in your tree. 
And the files represent the leaf nodes in the tree. Since it only visit each node once, we can effectively say that the time complexity of the algorithm will scale with regards to the number of nodes (Files + Directories)
contained in  input data. Hence O(N).