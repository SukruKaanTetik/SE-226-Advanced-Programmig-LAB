#include <iostream>
#include <new>
using namespace std;

// Elements of the queue. Eaach node has data and pointer to next node
class Node{
public:
    int data;
    Node *next;

    Node (int d, Node *n){
        data = d;
        next = n;
    }
};

class Queue{
private:
    Node *head;  // first element 
    Node *end;  // last element 
    int numberElement;

public:
    Queue (){
        head = nullptr;
        end = nullptr;
        numberElement = 0;
    }

    // Adds new element to the end of the queue
    void enqueue(int data){
        if (head == nullptr){
            head = new Node(data, nullptr);
            end = head;
        }
        else {
            end->next = new Node(data, nullptr);
            end = end->next;
        }
        numberElement ++;
    }


    // removes the head element from the queue
   int dequeue(){
        Node *removeNode;
        int removeData;
        if (numberElement == 0){
            cout<<"Queue is empty"<<endl;
        }
        else{
            removeNode = head;
            removeData = head->data;
            head = removeNode->next;
            delete removeNode;
            numberElement --;
        }
        return removeData;
    }

    // returns the head element
    int top(){return head->data;}

    // returns true if queue is empty
    bool isEmpty(){
        if (numberElement == 0){ return true;}
        return false;
    }

    // returns the number of elements in queue
    int size(){
        return numberElement;
    }

    // print all elements in the queue in order
    void display(){
        Node *display = head;
        for (int i=0; i<size(); i++){
            cout<<display->data<<endl;
            display = display->next;
        }
    }


};
