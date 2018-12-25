import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        int[] newArr = {};
        
        for(int i=0; i<commands.length; i++){
            for(int j=0; j<(commands[i][1]-commands[i][0])+1; j++){
                newArr[j] = array[commands[i][0] - 1 + j];
            }
            Arrays.sort(newArr);
            answer[i] = newArr[commands[i][2] - 1];
            newArr = null;
        }
        
        return answer;
    }
}