
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    Node visited[];
    public Solution() {
        this.visited = new Node[100];
    }
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }
        Node copy = new Node(node.val);
        visited[copy.val - 1] = copy;
        
        for (Node neighbor: node.neighbors) {
            if (visited[neighbor.val - 1] == null) {
                neighbor = cloneGraph(neighbor);
                visited[neighbor.val - 1] = neighbor;
            } 
            copy.neighbors.add(visited[neighbor.val - 1]);
        }
        visited[copy.val - 1] = copy;
        return copy;
    }
}