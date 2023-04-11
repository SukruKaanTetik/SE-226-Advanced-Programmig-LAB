#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

// METHOD DECLERATIONS 
string passGen(int=5);
string repWithUpper(string="enter a string");
string swapLetters(string = "enter a string");
bool searchLetter(char ='c' ,string= "enter a string");



int main(){
    int number = 0;

    while (number < 3 || number > 7){
        cout<<"Enter a number between 3 and 7.........."<<endl;
        cin>>number;
    }

    string password = passGen(number);
    cout<<"Password: "<<password<<endl;

    string finalPassword= swapLetters(repWithUpper(password));
    cout<<"Final Password: "<<finalPassword<<endl;

    // 1 = true     0 = false
    cout<<searchLetter('k', "kaan")<<endl;

}


// QUESTION 1
string passGen(int user_no){
    srand(time(0)); // without this, random will always give same value

    string password;
    int listSize = size(words);

    // Concatenate user_no random string and create a password
    for (int i=0; i<user_no; i++){
        int randomNum = rand() % listSize;
        password += words[randomNum];
    }

    // Make the password reverse by using swap function
    int lengthPassword = size(password);
    for (int i=0; i<lengthPassword/2; i++){
        swap(password[i], password[lengthPassword-1-i]);
    }

    return password;
}



// QUESTION 2
string repWithUpper(string word){
    srand(time(0));
    char letter = word[rand()%size(word)];

    for (int i=0; i<size(word); i++){
        if (word[i] == letter){
            word[i] = toupper(letter);
        }
    }

    return word;
}

string swapLetters(string word){
    int length = size(word);
    swap(word[0], word[length - 2]);
    swap(word[1], word[length - 1]);

    return word;
}

// QUESTION 3
bool searchLetter(char key, string word){
    if (0 >= word.find(key) && word.find(key) <= size(word)){return true;}
    return false;
}
