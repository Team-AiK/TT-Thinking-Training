import java.util.*;

public class Solution {
	public int[] solution(int[] arr) {
		ArrayList<Integer> nums = new ArrayList<Integer>();

		if (arr.length > 1) {
			nums.add(arr[0]);
			for (int i = 1; i < arr.length; i++) {
				if (arr[i] != arr[i - 1]) {
					nums.add(arr[i]);
				}
			}
		} else {
			nums.add(arr[0]);
		}

		int[] answer = new int[nums.size()];

		for (int j = 0; j < nums.size(); j++) {
			answer[j] = nums.get(j);
		}

		return answer;
	}
}