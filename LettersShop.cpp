#include<bits/stdc++.h>
#define boost ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
int main(){
    boost;
    int n;cin>>n;
    string master;cin>>master;
    vector<vector<int>>indx(26);
    map<char,int>mp;
    int i,j,m=0,tmp,t;
    int f;cin>>f;
    int ans[f] = {0};
    string temp;
    for(i=0;i<n;i++){
        (indx[master[i]-'a']).push_back(i+1);
    }
    for(i=0;i<f;i++){
        cin>>temp;
        m = 0;
        mp.clear();
        for(j=0;j<temp.length();j++){
            t = mp[temp[j]];
            tmp = indx[temp[j]-'a'][t];
            if(m<tmp){
                m = tmp;
            }
            mp[temp[j]]++;
        }
        ans[i] = m;
    }
    for(i=0;i<f;i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}