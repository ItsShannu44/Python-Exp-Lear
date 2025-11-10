// #include <stdio.h>
// #include <math.h>
// #include <ctype.h>

// char stack[50];
// int top=-1;

// void push(char c)
// {
//     stack[++top]=c;
// }
// char pop()
// {
//     return stack[top--];
// }
// char peek(){
//     return stack[top];
// }
// int isEmpty(){
//     return top==-1;
// }
// int prec(char op)
// {
//     switch(op)
//     {
//         case '^':return 3;
//         case '*':
//         case '/':return 2;
//         case '+':
//         case '-':return 1;
//         default: return 0;
//     }
// }
// void infixtopostfix(char *exp) {
//     char output[100];
//     int k = 0;

//     for (int i = 0; exp[i]; i++) {
//         char c = exp[i];

//         if (isalnum(c)) {  
//             output[k++] = c;
//         } 
//         else if (c == '(') {
//             push(c);
//         } 
//         else if (c == ')') {
//             while (!isEmpty() && peek() != '(')
//                 output[k++] = pop();
//             if (!isEmpty()) pop(); 
//         } 
//         else { 
//             while (!isEmpty() && prec(peek()) >= prec(c)) {
//                 if (c == '^' && prec(peek()) == prec(c))
//                     break; 
//                 output[k++] = pop();
//             }
//             push(c);
//         }
//     }

//     while (!isEmpty())
//         output[k++] = pop();

//     output[k] = '\0';
//     printf("Postfix: %s\n", output);
// }

// int main() {
//     char exp[100];
//     printf("Enter the infix expression: ");
//     scanf("%s", exp);
//     infixtopostfix(exp);
//     return 0;
// }
















// #include<stdio.h>
// #include<math.h>
// #include<ctype.h>

// char stack[100];
// int top=-1;

// void push(char c){
//     stack[++top]=c;
// }
// char pop(){
//     return stack[top--];
// }
// char peek(){
//     return stack[top];
// }
// int isEmpty(){
//     return top==-1;
// }

// int prec(char op)
// {
//     switch(op)
//     {
//         case '^':return 3;
//         case '*':
//         case '/':return 2;
//         case '+':
//         case '-':return 1;
//         default: return 0;
//     }
// }

// void infixtopostfix(char*exp)
// {
//     char output[100];
//     int k=0;

//     for(int i=0;exp[i];i++)
//     {
//         char c=exp[i];

//         if(isalnum(c))
//         {
//             output[k++]=c;
//         }else if(c=='('){
//             push(c);
//         }else if(c==')'){
//             while(!isEmpty() && peek()!='(')
//             output[k++]=pop();
//         if(!isEmpty())pop();
//         }else{
//             while(!isEmpty() && prec(peek())>=prec(c)){
//             if(c=='^' && prec(peek())>=prec(c))
//             break;
//                 output[k++]=pop();
//             }
//             push(c);
//         }
//     }
//     while(!isEmpty())
//     {
//         output[k++]=pop();
//         output[k]='\0';
//         printf("Postfix: %s\n",output);
//     }
// }
// int main()
// {
//     char exp[100];
//     printf("Enter the infix exp:");
//     scanf("%s",exp);
//     infixtopostfix(exp);
//     return 0;
// }



#include<stdio.h>
#include<ctype.h>
#include<math.h>

int stack[100];
int top=-1;

void push(char c)
{
    stack[++top]=c;
}
int pop()
{
    return stack[top--];
}

int main()
{
    char exp[50];
    printf("Enter Postfix:");
    scanf("%s",exp);
    for(int i=0;exp[i];i++)
    {
        if(isdigit(exp[i]))push(exp[i]-'0');
        else{
            int b=pop(), a=pop();
            switch(exp[i])
            {
                case '+':push(a+b); break;
                case '-':push(a-b);break;
                case '*':push(a*b);break;
                case '/':push(a/b);break;
                case '^':push(pow(a,b));break;
            }
        }
    }
    printf("Result: %d\n",pop());
}