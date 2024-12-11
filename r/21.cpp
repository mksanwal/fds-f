#include<iostream>
using namespace std;

class circular_queue{
    public:

    int *arr;
    int size;
    int front;
    int rear;

    public:
    circular_queue(int n){
        size=n;
        arr=new int[size];
        front=rear=-1;
    }

    void enqueue(int data){
        if(front == 0 && rear == size -1 || rear == (front-1)%(size-1)){
            cout<<"Queue is full"<<endl;
            return;
        }else if(front == -1){
            rear=front=0;
        }else if(rear == size -1 && front != 0){
            rear=0;
        }else{
            rear++;
        }

        arr[rear]=data;
    }

    int dequeue(){
        if(front == -1){
            cout<<"Queue is empty"<<endl;
            return -1;
        }else{
            int ans=arr[front];
            arr[front] =-1;

            if(front == rear){
                front=-1;
                rear=-1;
            }else if(front == size-1){
                front=0;
            }else{
                front++;
            }

            return ans;
        }
    }

    void display(){
        if(front == -1){
            cout<<"Queue is empty"<<endl;
            return;
        }else{
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
    }
};

int main(){
    
    circular_queue q(5);
 
    // Inserting elements in Circular Queue
    q.enqueue(14);
    q.enqueue(22);
    q.enqueue(13);
    q.enqueue(-6);
 
    // Display elements present in Circular Queue
    q.display();
 
    // Deleting elements from Circular Queue
    printf("\nDeleted value = %d", q.dequeue());
    printf("\nDeleted value = %d", q.dequeue());

    cout<<endl;
 
    q.display();
 
    q.enqueue(9);
    q.enqueue(20);
    q.enqueue(5);
 
    q.display();
 
    q.enqueue(20);
}