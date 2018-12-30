import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
		HashMap<String, Integer> spy = new HashMap<String, Integer>();
		int count = 0;
		int answer = 1;

		for (int i = 0; i < clothes.length; i++) {
			if (spy.containsKey(clothes[i][1])) {
				spy.put(clothes[i][1], spy.get(clothes[i][1]) + 1);
				count++;
			} else {
				spy.put(clothes[i][1], 1);
				count++;
			}
		}

		for (int v : spy.values()) {
			answer *= v+1;
		}

		return answer - 1;
	}
}