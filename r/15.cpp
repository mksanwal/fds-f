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
    node * temp = NULL;
    node * head = NULL;
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

node * onecomplement(node * f){
    // cout<<"One complement"<<endl;
    node * temp = f;
    node * head = NULL;
    node * tail = NULL;

    while(temp!=NULL){
        int val = (temp->data == 0) ? 1 : 0;
        insert(head,tail,val);
        temp=temp->next;
    }

    return head;

}

node * twocomplement(node * f){
    // cout<<"Two Complement"<<endl;
    node * one = onecomplement(f);

    while(one->next != NULL){
        one = one ->next;
    }

    node * head = NULL;
    node * tail = NULL;

    int carry = 1;
    while(one!=NULL){
        int sum = one->data + carry ;
        int val = sum%2;
        carry = sum/2;
        insert(head,tail,val);
        one = one->prev; 
    }

    if(carry){
        insert(head,tail,carry%2);
    }

    node * ans = NULL;
    node * back = NULL;

    while(head->next !=NULL){
        head = head->next;
    }

    while(head!=NULL){
        insert(ans,back,head->data);
        head = head->prev;
    }

    return ans;
}


int main(){
    cout<<"Enter string to find complement : "<<endl;
    string s;
    cin>>s;
    cout<<"Your Stirng is"<<endl;
    node * f = binarytodll(s);
    display(f);
    cout<<"One Complement"<<endl;
    node * comp = onecomplement(f);
    display(comp);
    cout<<"Two Complement"<<endl;
    node * twocomp = twocomplement(f);
    display(twocomp);
}