#include<bits/stdc++.h>
#define pb push_back
#define boost ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
int main(){
    int n,i;
    float temp;
    long long int s = 0;
    vector<float>nos;
    vector<int>res;
    cin>>n;
    for(i=0;i<n;i++){
        cin>>temp;
        nos.pb(temp);
        res.pb(floor(temp));
        s += floor(temp);
    }
    if(s==0){
        for(i=0;i<n;i++){
            cout<<res[i]<<endl;
        }
        return 0;
    }
    for(i=0;i<n;i++){
        if(s==0){break;}
        if(res[i]!=nos[i]){
            res[i]++;
            s++;
        }
    }
    for(i=0;i<n;i++){
        cout<<res[i]<<endl;
    }
    return 0;
}