The following is an explanation of "File Recursion" implemented as part of the project - "Show me the Data Structures"

1)  os.listdir(path) will list all the files and folders in a given path. Since it has to iterate over each item to provide a list, it takes linear time complexity.
Let l be the length of the path_elements => O(len(path_elements)) => O(l)

2)  If s is a length of the filename (name of the file/folder) with a specific extension(.c in our case),
then it takes O(s) time to find out a file with the given extension.
Therefore, for f number of files, it takes O(f*s) time. 
If file names are not too long , this would lead to - O(f)

3)  traversing through g number of directories  will take linear time i.e. O(g)

The above 3 steps will take => O(l + f + g) => O(l)
Since, l (len(path_elements)) is a dominant term (combination of path_files and path_folders)