#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,k;
	cin>>n>>k;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	int count = 0;
	for(int i=0;i<n;i++){
		if(a[i]<=k){
			count++;
		}
		else{
			break;
		}
	}
	if(count != n){
		for(int i=n-1;i>=0;i--){
			if(a[i]<=k){
				count++;
			}
			else{
				break;
			}
		}
	}
	cout<<count<<endl;
	return 0;
}