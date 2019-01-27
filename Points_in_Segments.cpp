#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    int check[m+1]={0};
    int a[n][2];
    for (int i=0;i<n;i++){
        cin>>a[i][0]>>a[i][1];
        for(int j=a[i][0];j<=a[i][1];j++){
            check[j]++;
        }
    }
    int count = 0;
    for(int i=1;i<m+1;i++){
        if (check[i]==0){
            count++;
        }
    }
    cout<<count<<endl;
    for(int i=1;i<m+1;i++){
        if(check[i]==0){
            cout<<i<<" ";
        }
    }

    return 0;
}