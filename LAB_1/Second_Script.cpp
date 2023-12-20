#include <iostream>
using namespace std;

int main(){
    int var1;
    int var2;

    cout<<"Enter var1:";
    cin>>var1;
    cout<<"Enter var2:";
    cin>>var2;

    int sum = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;

    cout<<"Var1: "<<var1<<"  Var2: "<<var2<<endl;
    cout<<"Sum: "<<sum<<"  Diff: "<<diff<<"  Prod: "<<prod;

    return 0;
}
