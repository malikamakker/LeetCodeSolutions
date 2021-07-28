class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.list = []
        self.get_all_values()

    def insert(self, v: int) -> int:
        new_node = TreeNode(v)
        self.list.append(new_node)
        parent_node = self.list[int(len(self.list) / 2) - 1]
        if not parent_node.left:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        return parent_node.val

    def get_root(self) -> TreeNode:
        return self.list[0]

    def get_all_values(self):
        level = 1
        last_node = self.root
        while last_node:
            last_node = self.traverse(1, level, self.root)
            level += 1

    def traverse(self, current, target, node):
        if current == target and node:
            self.list.append(node)
            return node
        elif current < target:
            last_node = self.traverse(current + 1, target, node.left)
            last_node = self.traverse(current + 1, target, node.right)
            return last_node
        return None
