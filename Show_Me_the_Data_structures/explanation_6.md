The following is an explanation of "Union and Intersection of two Linked lists" implemented as part of the project - "Show me the Data Structures"

The union of 2 sets has time complexity O(len(s)+len(t)), where s and l being their respective lengths
The intersection of 2 sets has time complexity O(min(len(s),lent(t)), where s and l being their respective lengths

Space complexities for the above two operations happens to be O(1) because we are creating a new linked list for storing 
the union/intersection of 2 linked list

The set data structure was used because we wanted to take care of duplicate elements, updating a set happens to be in O(1)