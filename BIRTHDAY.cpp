#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define speed ios_base::sync_with_stdio(false);cin.tie(NULL);
using namespace std;

int main() {
    speed
    ll n, m, k, l;
    cin>>n>>m>>k>>l;
    if(m>n){
        cout<<"-1"<<endl;
    }
    else{
        ll rem = (l+k)/m;
        if((l+k)%m){
            rem++;
        }
        if(rem*m>n){
            cout<<"-1"<<endl;
        }
        else{
            cout<<rem<<endl;
        }
    }
    return 0;
}