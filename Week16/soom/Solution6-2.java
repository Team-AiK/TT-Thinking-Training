import java.util.*;

class Solution {
    public String solution(int[] numbers) {
		String answer ="";
            List<String> list = new ArrayList<>();
            int length = numbers.length;
 
            //int형 데이터를 String형으로 바꿔서 저장
            for(int i=0; i<length; i++){
                list.add(Integer.toString(numbers[i]));
            }
 
            int size = list.size();
            Collections.sort(list, (num1, num2) -> (num2+num1).compareTo(num1+num2));

            if(list.get(0).equals("0")){
                return "0";
            }
 
            for(int i=0; i<size; i++){
                answer = answer + list.get(i);
            }
            return answer;
	}
}

/**
 * Compareto(a,b)
 * a == b -> 0반환
 * a > b -> 1반환 ==> 오름차순(sort)
 * a < b -> -1반환 ==> 내림차순(sort)
 * 
 */