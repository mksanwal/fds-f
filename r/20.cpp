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

string postfixtoinfix(string s){
    stack<string>stk;

    for(char c : s){
        if(!isoperator(c)){
            string operand(1,c);
            stk.push(operand);
        }else{
            string op1 = stk.top();
            stk.pop();
            string op2 = stk.top();
            stk.pop();

            string ans = "("+op2+c+op1+")";
            stk.push(ans);
        }
    }

    return stk.top();
}

string infixtoprefix(string expression){
    stack<char> s;

    reverse(expression.begin(),expression.end());

    string prefix="";
    for(char c : expression){
        if(isalnum(c)){
            prefix.push_back(c);
        }else if(c==')'){
            s.push(c);
        }else if(c=='('){
            while(!s.empty() and s.top()!=')'){
                prefix.push_back(s.top());
                s.pop();
            }
            s.pop();
        }else if(isoperator(c)){
            while(!s.empty() and precedence(c)<=precedence(s.top())){
                prefix.push_back(s.top());
                s.pop();
            }
            s.push(c);
        }
    }

    while(!s.empty()){
        prefix.push_back(s.top());
        s.pop();
    }
    reverse(prefix.begin(),prefix.end());
    return prefix;
}

int main(){
    string expression;
    cin>>expression;
    //a*b+c/d

    if(iswellparanthesized(expression)){
        cout<<"Well paranthesized"<<endl;
        cout<<infixtopostfix(expression)<<endl;
        evaluation(infixtopostfix(expression));
        string infix = postfixtoinfix(infixtopostfix(expression));
        cout<<"Infix is : "<<infix<<endl;
        string prefix = infixtoprefix(infix);
        cout<<"Prefix is : "<<prefix<<endl;
    }else{
        cout<<"not Well Parenthesized"<<endl;
    }
}