import java.util.*;

class Solution {
  public boolean solution(String s) {
		boolean answer = false;

		if (s.length() == 4) {
			try {
				int num = Integer.parseInt(s);
				answer = true;
			} catch (NumberFormatException e) {

			}
		}

		return answer;
	}
}