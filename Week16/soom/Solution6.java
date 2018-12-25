import java.util.*;

class Solution {
    public String solution(int[] numbers) {
		String answer = "";
		
		for (int i = 0; i < numbers.length; i++) {
			
		}

		for (int i = numbers.length; i > 0; i--) {
			for (int j = 0; j < i - 1; j++) {
				int temp = 0;
				int pre = Integer.parseInt(String.valueOf(numbers[j]) + String.valueOf(numbers[j + 1]));
				int post = Integer.parseInt(String.valueOf(numbers[j + 1]) + String.valueOf(numbers[j]));

				if (pre < post) {
					temp = numbers[j];
					numbers[j] = numbers[j + 1];
					numbers[j + 1] = temp;
				}
			}
		}
		
		for(int i=0; i< numbers.length; i++){
            answer += String.valueOf(numbers[i]);
        }
        
		return answer;
	}
}

/** 데이터가 많을 때는 너무 오래걸린다.
 *  다른 알고리즘이 필요!
 */