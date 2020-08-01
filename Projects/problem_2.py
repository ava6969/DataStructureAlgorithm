import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    def recursive_search(suffix, path):
        paths = ""

        if os.path.isfile(path):
            if path.endswith(suffix):
                return path
            else:
                return
        else:
            for dir_name in os.listdir(path):
                if os.path.isfile(dir_name):
                    if dir_name.endswith(suffix):
                        paths += dir_name + ' '
                else:
                    res = recursive_search(suffix, os.path.join(path, dir_name))
                    if res:
                        paths += res + ' '
            return paths

    return recursive_search(suffix, path).split()


def test():
    res = find_files(".c", "testdir")
    print(len(res) == 4)  # True
    print(all([d.endswith(".c") for d in res]))  # True


test()