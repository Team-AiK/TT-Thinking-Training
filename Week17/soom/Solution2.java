class Solution {
    public long solution(int N) {
		long answer = 0;
		long[] piv = new long[81];
		piv[1] = 1;
		piv[2] = 1;
		for (int i = 3; i <= N; i++) {
			piv[i] = piv[i - 1] + piv[i - 2];
		}
		answer = piv[N] * 2 + (piv[N] + piv[N - 1]) * 2;
		return answer;
	}
}