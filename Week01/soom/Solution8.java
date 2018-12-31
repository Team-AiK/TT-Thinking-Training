class Solution {
    boolean solution(String s) {
		boolean answer = false;
		int countP = 0, countY = 0;

		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 'P' || s.charAt(i) == 'p') {
				countP++;
			} else if (s.charAt(i) == 'Y' || s.charAt(i) == 'y') {
				countY++;
			}
		}

		if (countP == countY) {
			answer = true;
		}

		return answer;
	}
}