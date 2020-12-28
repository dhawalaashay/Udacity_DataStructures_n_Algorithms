import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    try:
        result = list()
        for file in os.listdir(path):
            if file.endswith(suffix):
                result.extend([os.path.join(path, file)])
            else:
                temp_path = os.path.join(path, file)
                if os.path.isdir(temp_path):
                    result.extend(find_files(suffix, temp_path))
        return result
    except Exception as e:
        print(f"couldn't find the files with extension/suffix - {suffix} in the path - {path} due to - {str(e)}")
        return None


if __name__ == "__main__":
    file_path = "/Users/adhawal/my_experiments/Udacity/DataStructureNAlgorithem/Data Structure & Algorithm/testdir"
    results = find_files('.c', file_path)
    print(results)

    """
    output retrieved:
    
    ['/Users/adhawal/my_experiments/Udacity/DataStructureNAlgorithem/Data Structure & Algorithm/testdir/subdir3/subsubdir1/b.c',
     '/Users/adhawal/my_experiments/Udacity/DataStructureNAlgorithem/Data Structure & Algorithm/testdir/t1.c',
      '/Users/adhawal/my_experiments/Udacity/DataStructureNAlgorithem/Data Structure & Algorithm/testdir/subdir5/a.c',
     '/Users/adhawal/my_experiments/Udacity/DataStructureNAlgorithem/Data Structure & Algorithm/testdir/subdir1/a.c']
    """