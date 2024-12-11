#include<bits/stdc++.h>
using namespace std;

class Deque{
    public:
    int * arr;
    int size;
    int front;
    int rear;

    public:

    Deque(int s){
        this->size = s;
        arr = new int[size];
        front = -1;
        rear = -1;
    }

    bool isfull(){
        if(front == 0 && rear == size-1 ||(front!=0) && rear == (front-1)%(size-1)){
            return true;
        }
        return false;
    }

    bool isEmpty(){
        if(front == -1){
            return true;
        }

        return false;
    }

    void push_front(int val){
        if(isfull()){
            cout<<"Queue is Full"<<endl;
            return;
        }else if(isEmpty()){
            front = rear = 0;
        }else if(front==0 and rear!= size -1){
            front = size -1;
        }else{
            front --;
        }

        arr[front] = val;
    }

    void push_rear(int val){
        if(isfull()){
            cout<<"Queue is Full"<<endl;
            return;
        }else if(isEmpty()){
            front = rear = 0;
        }else if(front!=0 and rear== size -1){
            rear = 0;
        }else{
            rear++;
        }

        arr[rear] = val;
    }

    int pop_front(){
        if(isEmpty()){
            cout<<"Queue is empty"<<endl;
            return -1;
        }else{

            int val = arr[front];
            arr[front]=-1;

            if(front == rear){
                front = rear = 0;
            }else if(front == size-1){
                front =0;
            }else{
                front++;
            }

            return val;
        }
    }

    int pop_rear(){
        if(isEmpty()){
            cout<<"Queue is empty"<<endl;
            return -1;
        }else{

            int val = arr[rear];
            arr[rear]=-1;

            if(front == rear){
                front = rear = 0;
            }else if(rear == 0){
                rear = size -1;
            }else{
                rear--;
            }

            return val;
        }
    }

    int qfront(){
        if(isEmpty()){
            cout<<"Queue is Empty"<<endl;
            return -1;
        }

        return arr[front];
    }

    int qrear(){
        if(isEmpty()){
            cout<<"Queue is Empty"<<endl;
            return -1;
        }

        return arr[rear]; 
    }

    void display(){
        if(rear>=front){
            for(int i=front;i<=rear;i++){
                cout<<arr[i]<<" ";
            }
            cout<<endl;
        }else{
            for(int i=front;i<size;i++){
                cout<<arr[i]<<" ";
            }

            for(int i=0;i<=rear;i++){
                cout<<arr[i]<<" ";
            }

            cout<<endl;
        }
    }
};



int main(){

    Deque d(5);
    d.push_front(5);
    d.push_front(5);
    d.display();
    d.push_front(5);
    d.push_rear(4);
    d.push_front(1);
    d.push_rear(7);
    d.display();
    cout<<d.pop_front()<<endl;
    d.display();
    cout<<d.pop_rear()<<endl;
    d.display();
    cout<<d.qfront()<<endl;
    cout<<d.qrear()<<endl;
}