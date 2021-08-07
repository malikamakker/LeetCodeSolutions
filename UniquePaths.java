import java.util.*;

class Solution {
    public int uniquePaths(int m, int n) {
        List<List<Integer>> path = new ArrayList<>();
        for(int i=0;i<m;i++) {
            List<Integer> a = new ArrayList<>();
            for (int j=0;j<n;j++) {
                a.add(-1);
            }
            path.add(a);
        }
        return findPaths(path, 0, 0, m, n);
    }
    
    public int findPaths(List<List<Integer>> path, int i, int j, int m, int n)
    {
        if (i==m-1 && j == n-1) 
            return 1;
        int count = 0;
        if (i<m && j<n) {
            if (path.get(i).get(j) > -1) 
                return path.get(i).get(j);
            count += findPaths(path, i+1, j, m, n);
            count += findPaths(path, i, j+1, m, n);
            List<Integer> row = path.get(i);
            row.set(j, count);
            path.set(i, row);
        }
        return count;
    }
}