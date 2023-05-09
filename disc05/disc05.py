def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    # if not is_leaf(t):
    #     branch = branches(t)
    #     for i in branch:
    #         if not is_leaf(i):
    #             return height(i) + 1
    # else:
    #     return 1
    if is_leaf(t):
        return 0
    else:
        max_height = 0
        for i in branches(t):
            max_height = max(max_height, height(i))
        return 1 + max_height
    
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        max_sum = 0
        for i in branches(t):
            max_sum = max(max_sum, max_path_sum(i))
        return label(t) + max_sum
    
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
        
    # if label(t) == x:
    #     return [label(t)]
    # elif is_leaf(t):
    #     return None
    # else:
    #     for i in branches(t):
    #         path = find_path(i, x)
    #         if path != None:
    #             return [label(t)] + path

def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    if is_leaf(t):
        return label(t)
    else:
        sum = 0
        for i in branches(t):
            sum += sum_tree(i)
        return label(t) + sum
    
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    # if is_leaf(t):
    #     return True
    # else:
    #     lis = []
    #     for i in branches(t):
    #         lis += [sum_tree(i)]
    #     for j in range(len(lis)-1):
    #         if lis[j] != lis[j + 1]:
    #             return False
    #         else:
    #             return balanced()
    if is_leaf(t):
        return True
    else:
        first_branches = sum_tree(branches(t)[0])
        for i in branches(t):
            if sum_tree(i) != first_branches:
                return False
        for j in branches(t):
            if not balanced(j):
                return False
    return True

def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        lis = []
        for i in leaves:
            lis +=[tree(i)]
        t = tree(label(t), lis)
        return t
    else:
        new_branches = []
        for b in branches(t):
            new_branches += [sprout_leaves(b, leaves)]
        t = tree(label(t), new_branches)
        return t
    
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(n * 2, h - 1)]
    if ((n - 1) // 3) % 2 != 0 and (n - 1) % 3 == 0 and (n - 1) // 3 > 1:
        branches += [hailstone_tree((n - 1) // 3, h - 1)]
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)
