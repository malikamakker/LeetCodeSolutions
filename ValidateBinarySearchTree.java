
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int last;
    boolean firstValue;
    Solution () {
        this.last = 0;
        this.firstValue = false;
    }

    public boolean isValidBST(TreeNode root) {
        if (root.left != null) {
            if(!isValidBST(root.left)) {
                return false;
            }
        }

        if (this.firstValue && root.val <= this.last) {
            return false;
        }
        this.last = root.val;
        this.firstValue = true;

        if (root.right != null) {
            if(!isValidBST(root.right)) {
                return false;
            }
        }
        return true;
    }
}