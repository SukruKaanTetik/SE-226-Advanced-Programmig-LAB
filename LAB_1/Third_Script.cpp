#include <iostream>
using namespace std;

int main(){
    string name;
    float labGrade;
    float midtermGrade;
    float finalGrade;
/*
    cout<<"Enter name: "<<endl;
    cin>>name;
    cout<<name;
*/
    cout<<"Enter name: "<<endl;
    getline(cin, name);


    cout<<"Enter lab grade:";
    cin>>labGrade;
    cout<<"Enter midterm grade:";
    cin>>midtermGrade;
    cout<<"Enter final grade:";
    cin>>finalGrade;

    float grade = ((labGrade/4) + (midtermGrade * 35/100) + (finalGrade*4/10));

    cout<<"Name: "<<name<<endl<<"Lab: "<<labGrade<<endl<<"Midterm: "
    <<midtermGrade<<endl<<"Final: "<<finalGrade<<endl
    <<"Last Score: "<< grade;

    return 0;
}
