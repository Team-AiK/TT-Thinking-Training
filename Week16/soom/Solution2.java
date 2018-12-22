import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        String pre = "", post = "";
        
        for(int i=0; i<phone_book.length; i++){
            pre = phone_book[i];
            for(int j=0; j<phone_book.length; j++){
                if(i!=j){
                    post = phone_book[j];
                    if(pre.startsWith(post)){
                        answer = false;
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}