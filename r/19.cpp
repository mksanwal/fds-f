#include<bits/stdc++.h>
using namespace std;

class node{
    public:
    int data;
    node * next;
    node * prev;

    public:
    node(int d){
        this->data = d;
        prev = NULL;
        next = NULL;
    }
};

void display(node * head){
    node * temp = head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}

node * binarytodll(string s){
    node * head = NULL;
    node * temp = NULL;
    for(auto i : s){
        node * curr = new node(i-'0');
        if(temp == NULL){
            head = curr;
            temp = curr;
        }else{
            temp->next = curr;
            curr->prev = temp;
            temp=temp->next;
        }
    }
    return head;
}

void insert(node * &head,node * &tail,int i){
    node * temp = new node(i);
    if(head == NULL){
        head = temp;
        tail = temp;
    }else{
        tail->next = temp;
        temp->prev = tail;
        tail = tail->next;
    }
}

node * added(node * f, node * s){
    node * F = f;
    while(F->next != NULL){
        F=F->next;
    }

    node * S = s;
    while(S->next != NULL){
        S=S->next;
    }


    node * head = NULL;
    node * tail = NULL;

    int carry =0;
    while(F!= NULL and S!=NULL){
        int sum = F->data + S->data + carry;
        int val = sum%2;
        carry = sum/2;
        insert(head,tail,val);
        F=F->prev;
        S=S->prev;
    }

    while(F!= NULL){
        int sum = F->data + carry;
        int val = sum%2;
        carry = sum/2;
        insert(head,tail,val);
        F=F->prev;
    }

    while(S!=NULL){
        int sum = S->data + carry;
        int val = sum%2;
        carry = sum/2;
        insert(head,tail,val);
        S=S->prev;
    }

    if(carry){
        insert(head,tail,carry%2);
    }

    node * ans = NULL;
    node * t=NULL;

    while(head->next != NULL){
        head = head->next;
    }

    while(head != NULL){
        insert(ans,t,head->data);
        head = head->prev;
    }

    return ans;


}

int main(){

    cout<<"Enter string : ";
    string s1;
    cin>>s1;
    node * f = binarytodll(s1);
    cout<<"Your String is : ";
    display(f);
    cout<<"Enter string : ";
    string t;
    cin>>t;
    node * s = binarytodll(t);
    cout<<"Your String is : ";
    display(s);
    node * adds=added(f,s);
    cout<<"Addition is : ";
    display(adds);

}