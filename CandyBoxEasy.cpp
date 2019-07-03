#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
using namespace std;
int main(){
    int q;
    cin>>q;
    vector<int>freq;
    set<int>keys;
    int prev;
    long long int ans;
    int n,temp;
    map<int,int>a;
    while(q--){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>temp;
            a[temp] ++;
            keys.insert(temp);
        }
        for(auto i:keys){
            if(a[i]!=0){
                freq.pb(a[i]);
            }
        }
        sort(freq.rbegin(),freq.rend());
        prev = 200005;
        ans = 0;
        for(int i=0;i<freq.size();i++){
            if(prev==0){
                break;
            }
            if(prev>freq[i]){
                ans += freq[i];
                prev = freq[i];
            }
            else{
                ans += prev-1;
                prev --;
            }
        }
        a.clear();
        keys.clear();
        freq.clear();
        cout<<ans<<endl;
    }
    return 0;
}