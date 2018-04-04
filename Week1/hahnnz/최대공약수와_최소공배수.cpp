#include<vector>
#include<iostream>
using namespace std;
vector<int> gcdlcm(int a,int b)
{
    vector<int> answer;
    answer.reserve(2); 
    
    int i,j;
    int gcd = 0;
    int lcm = 0;

    j = (a<b)?a:b;
    for(i=1;i<=j;i++){
        if (a%i==0 && b%i==0) gcd=i;
    }
    j = (a>b)?a:b;
    for(i=j;;i++){
        if (i%a==0 && i%b==0){
            lcm=i;
            break;
        }
    }

    answer.push_back(gcd);
    answer.push_back(lcm);

    return answer;
}

int main()
{
    int a=3, b=12;
    vector<int> testAnswer = gcdlcm(a,b);

    cout<<testAnswer[0]<<" "<<testAnswer[1];
}
