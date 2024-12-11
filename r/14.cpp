#include<bits/stdc++.h>
using namespace std;

int precedence(char c){
    if(c=='+' || c=='-'){
        return 1;
    }else if(c=='*' || c=='/'){
        return 2;
    }else{
        return 0;
    }
}

bool isoperator(char c){
    if(c=='+' || c=='-' || c=='*' || c=='/'){
        return true;
    }

    return false;
}

string infixtopostfix(string expression){
    stack<char> s;
    string postfix="";
    for(char c : expression){
        if(isalnum(c)){
            postfix.push_back(c);
        }else if(c=='('){
            s.push(c);
        }else if(c==')'){
            while(!s.empty() and s.top()!='('){
                postfix.push_back(s.top());
                s.pop();
            }
            s.pop();
        }else if(isoperator(c)){
            while(!s.empty() and precedence(c)<=precedence(s.top())){
                postfix.push_back(s.top());
                s.pop();
            }
            s.push(c);
        }
    }

    while(!s.empty()){
        postfix.push_back(s.top());
        s.pop();
    }
    
    return postfix;
}

void evaluation(string s){
    
    stack<double> st;
    for(char c : s){
        if(isalnum(c)){
            st.push(c-'0');
        }else{
            double a = st.top(); st.pop();
            double b = st.top(); st.pop();

            if(c == '+'){
                double val= a + b;
                st.push(val);
            }else if(c == '-'){
                double val= a - b;
                st.push(val);
            }else if(c == '*'){
                double val= a * b;
                st.push(val);
            }else if(c == '/'){
                double val= a / b;
                st.push(val);
            }
        }
    }

    cout<<st.top()<<endl;
}
bool iswellparanthesized(string expression){
    stack<char> s;
    for(char c : expression){
        if(c=='('){
            s.push(c);
        }else if(c==')'){
            if(s.empty() || s.top()!='('){
                return false;
            }
            s.pop();
        }
    }

    if(!s.empty()) return false;
    return true;
}

int main(){
    string expression;
    cin>>expression;
    //a*b+c/d

    if(iswellparanthesized(expression)){
        cout<<"Well paranthesized"<<endl;
        cout<<infixtopostfix(expression)<<endl;
        evaluation(infixtopostfix(expression));
    }else{
        cout<<"not Well Parenthesized"<<endl;
    }
}