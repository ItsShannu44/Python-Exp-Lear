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



// #include<stdio.h>
// #include<ctype.h>
// #include<math.h>

// int stack[100];
// int top=-1;

// void push(char c)
// {
//     stack[++top]=c;
// }
// int pop()
// {
//     return stack[top--];
// }

// int main()
// {
//     char exp[50];
//     printf("Enter Postfix:");
//     scanf("%s",exp);
//     for(int i=0;exp[i];i++)
//     {
//         if(isdigit(exp[i]))push(exp[i]-'0');
//         else{
//             int b=pop(), a=pop();
//             switch(exp[i])
//             {
//                 case '+':push(a+b); break;
//                 case '-':push(a-b);break;
//                 case '*':push(a*b);break;
//                 case '/':push(a/b);break;
//                 case '^':push(pow(a,b));break;
//             }
//         }
//     }
//     printf("Result: %d\n",pop());
// }



// @VPL mainfile       // ← marks this as the file students see
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};
typedef struct node* NODE;

NODE insertFront(NODE head, int val) {
    NODE newnode = malloc(sizeof(struct node));
    newnode->data = val;
    newnode->link=NULL;
    if(head==NULL)
    {
        newnode->link=head;
        return newnode;
    }
    newnode->link=head;
    head=newnode;
    return head;
}
NODE insertEnd(NODE head, int val)
{
    NODE newnode=malloc(sizeof(struct node));
    newnode->data=val;
    newnode->link=NULL;
    if(head==NULL)
    {
        printf("Inserted  %d at rear",newnode->data);
        return newnode;
    }
    NODE T=head;
    while(T->link!=NULL)
    {
        T=T->link;
    }
    T->link=newnode;
    printf("\nInserted %d at rear.\n",newnode->data);
    return head;
}
NODE delete_frnt(NODE head)
{
    NODE T=head;
    if(head==NULL)
    {
        printf("Empty list");
    }else{
        NODE T=head;
        head=head->link;
        printf("\nDeleted %d at front.\n",T->data);
        free(T);
    }
    return head;
}
NODE delete_rear(NODE head)
{
    if(head==NULL)
    {
        printf("Empty List...");
        return head;
    }else{
        NODE curr=head,prev=NULL;
        while(curr->link!=NULL)
        {
            prev=curr;
            curr=curr->link;
        }
        prev->link=NULL;
        printf("\nDeleted %d from rear\n",curr->data);
        free(curr);
        return head;
    }
}
void display(NODE head) {
    NODE temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->link;
    }
}

int main() {
    NODE head = NULL;
    head = insertFront(head, 30);
    head = insertFront(head, 20);
    head = insertFront(head, 10);
    display(head);
    head=delete_frnt(head);
    display(head);
    head=insertEnd(head, 60);
    display(head);
    head=delete_rear(head);
    display(head);
    return 0;
}