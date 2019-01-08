import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
		int answer = 0;
		int sum1 = 0, sum2 = 0;
		int sumArr[][] = new int[triangle.length][triangle.length];

		sumArr[0][0] = triangle[0][0];

		for (int i = 1; i < triangle.length; i++) {
			for (int j = 0; j < triangle[i].length; j++) {
				if (j == 0) {
					sumArr[i][j] = sumArr[i - 1][j] + triangle[i][j];
				} else if (j == triangle[i].length - 1) {
					sumArr[i][j] = sumArr[i - 1][j - 1] + triangle[i][j];
				} else {
					sum1 = sumArr[i - 1][j - 1] + triangle[i][j];
					sum2 = sumArr[i - 1][j] + triangle[i][j];
					sumArr[i][j] = sum1 > sum2 ? sum1 : sum2;
				}
			}
		}

		Arrays.sort(sumArr[triangle.length - 1]);

		answer = sumArr[triangle.length - 1][triangle[triangle.length - 1].length - 1];

		return answer;
	}
}