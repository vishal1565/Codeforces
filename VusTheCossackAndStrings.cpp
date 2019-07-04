#include<bits/stdc++.h>
#define boost ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define pb push_back
using namespace std;

int main(){
    boost;
    string a,b;
    cin>>a>>b;
    int i,j,s=0;
    vector<int>big,prefixSum;
    int l = a.length();
    int l2 = b.length();
    big.pb(a[0]-'0');
    prefixSum.pb(big[0]);
    for(i=1;i<l;i++){
        big.pb(a[i]-'0');
        prefixSum.pb(prefixSum[i-1]+a[i]-'0');
    }
    int ones = (count(b.begin(),b.end(),'1'))%2;
    int count = 0;
    if(prefixSum[l2-1]%2==ones){
        count++;
    }
    j=0;
    for(i=l2;i<l;i++){
        if((prefixSum[i]-prefixSum[j])%2==ones){
            count++;
        }
        j++;
    }
    cout<<count<<endl;
    return 0;
}