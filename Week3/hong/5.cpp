
#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> >productMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
  int sizeA=A.size(),sizeA0=A[0].size(),sizeB0=B[0].size();
        vector<vector<int> >answer;
  answer.resize(sizeA,vector<int>(sizeB0));
        for(int i=0;i<sizeA;i++){
    for(int j=0;j<sizeB0;j++){
     for(int k=0;k<sizeA0;k++){
     answer[i][j]+=A[i][k]*B[k][j];
     }
    }
  }
        return answer;
}

int main()
{
        vector<vector<int> >A{
          {1,2}, {2,3}
        };
        vector<vector<int> >B{
          {2,3}, {3,4}
        };
        vector<vector<int> > testAnswer = productMatrix(A,B);

        for(int i=0;i<testAnswer.size(); i++)
        {
                for(int j=0;j<testAnswer[i].size(); j++)
                        cout<<testAnswer[i][j]<<" ";
                cout<<"\n";
        }
}

