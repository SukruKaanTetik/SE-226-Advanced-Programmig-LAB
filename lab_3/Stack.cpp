
#include <iostream>
#include <new>
using namespace std;

class Node{
public:
    int data;
    Node *prev; // instead of next, pointing prev is better because avoids some for loops
    Node(int d, Node* n){
        data = d;
        prev = n;
    }
};


class Stack {

private:
    Node *topNode;
    int numElement;

public:
    Stack(){
        topNode = NULL;
        numElement = 0;
    }

    bool isEmpty(){
        if (numElement == 0)
            return true;
        return false;
    }

    // adds the new element to top
    void push(int data){
        if (isEmpty()){
            topNode = new Node(data, nullptr);
        }
        else {
            Node *newTop;
            newTop = new Node(data, topNode);
            topNode = newTop;
        }
        numElement ++;
    }

  
    // Deletes the top element 
    int pop(){
        int deletedData;
        Node * pastTop;

        if (isEmpty())
            cout<<"Stack is empty"<<endl;
        else {
            deletedData = topNode->data;
            pastTop = topNode;
            topNode = topNode->prev;

            delete pastTop;
            numElement --;
            return deletedData;
        }
    }

    int peek(){
        return topNode->data;
    }

    // prints out the stak starting from top node
    void display(){
        Node *d = topNode;
        for(int i= 0; i<numElement; i++){
            cout<<d->data<<endl;
            d = d->prev;
        }
    }

};
