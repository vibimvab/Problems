class Node:
    def __init__(self, value, left, right):
        self.value: int = value
        self.parent = None
        self.left = left if left != -1 else None
        self.right = right if right != -1 else None
        self.left_value: int = 0  # value of left subtree
        self.right_value: int = 0  # value of right subtree


def solution(k, num, links):
    # constructing the tree
    nodes: [Node] = []
    for i, value in enumerate(num):
        nodes.append(Node(value, links[0], links[1]))

    for node in nodes:
        if node.left:
            node.left = nodes[node.left]
            node.left.parent = node
        if node.right:
            node.right = nodes[node.right]
            node.right.parent = node

    root = nodes[0]
    while root.parent:
        root = root.parent

    # DFS
    st = [root]
    while st:
        if st[-1].left:
            st.append(st[-1].left)



    answer = 0
    return answer