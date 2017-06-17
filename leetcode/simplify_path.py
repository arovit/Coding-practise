#!/usr/bin/python   


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        actual_path = ['root']
        path_list = path.split('/')
        for dir in path_list:
            if dir == "..":
                ele = actual_path.pop()
                if ele == "root":
                    actual_path.append('root')
            elif dir == ".":
                pass
            elif dir:
                actual_path.append(dir)
        actual_path = "/".join(actual_path[1:])
        path = "/" + actual_path
        return path
            
