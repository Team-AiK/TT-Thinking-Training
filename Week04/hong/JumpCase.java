class JumpCase {
int answer = 0;
    public int jumpCase(int num) {
         if(num==0)
          answer++;
          if(num>0){
         jumpCase(num-1);
         jumpCase(num-2);
        }
        return answer;
    }


    public static void main(String[] args) {
        JumpCase c = new JumpCase();
        int testCase = 4;
        //아래는 테스트로 출력해 보기 위한 코드입니다.
      	System.out.println(c.jumpCase(testCase));
    }
}
