class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] map = new int[101][101];
        int[][] p = new int[101][101];

        for (int i = 0; i < puddles.length; i++) {
            p[puddles[i][1]][puddles[i][0]] = -1;
        }

        map[1][0] = 1;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (p[i][j] != -1) {
                    map[i][j] = (map[i - 1][j] + map[i][j - 1]) % 1000000007;
                } else {
                    map[i][j] = 0;
                }
            }
        }

        answer = map[n][m];

        return answer;
    }
}