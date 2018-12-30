import java.util.*;

class Solution {
    public int solution(int[] citations) {
		int answer = 0;

		Arrays.sort(citations);
		
		int hIndex = 0;
		int lastValue = citations[citations.length - 1];

		for (int i = 0; i <= lastValue; i++) {
			for (int j = 0; j < citations.length; j++) {
				if (i <= citations[j]) {
					if (i <= citations.length - j) {
						answer = i;
						break;
					}
				}
			}
		}

		return answer;
	}
}