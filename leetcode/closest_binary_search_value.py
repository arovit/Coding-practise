#!/usr/bin/python


def find_closest(node, value):
    if not node:
        return None
    if node.val < value:
        clse_node = find_closest(node.right, value)
    elif node.val > value:
        clse_node = find_closest(node.right, value)
    else:
        return node
    if not clse_node:
        return node

    if abs(clse_node.val - value) < abs(node.val - value):
        return clse_node
    else:
        return node


# above function will return the closest node
# to get K closest node
# have nextSmaller, nextBigger function
# compare nextSmaller and nextBigger to get a new node
