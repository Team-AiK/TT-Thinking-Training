class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] map = new int[101][101];
        int[][] d = new int[101][101];

        for (int[] puddle: puddles) {
            map[puddle[1]][puddle[0]] = -1;
        }

        d[1][0] = 1;
        for (int i=1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (map[i][j] == -1) {
                    d[i][j] = 0;
                } else {
                    d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000007;
                }
            }
        }
        return d[n][m];
    }
}
