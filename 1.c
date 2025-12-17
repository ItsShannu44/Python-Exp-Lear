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









// #include <stdio.h>
// #include <stdlib.h>

// struct node {
//     int data;
//     struct node *link;
// };
// typedef struct node* NODE;

// NODE insert_frnt(NODE head, int data)
// {
//     NODE nn=malloc(sizeof(struct node));
//     nn->data=data;
//     nn->link=NULL;
//     if(head==NULL)
//     {
//         nn->link=head;
//         printf("Data %d inserted at front.\n",nn->data);
//         return nn;
//     }
//     nn->link=head;
//     printf("Data %d inserted at front.\n",nn->data);
//     return nn;
// }
// NODE insert_end(NODE head,int data)
// {
//     NODE nn=malloc(sizeof(struct node));
//     nn->data=data;
//     nn->link=NULL;
//     if(head==NULL)
//     {
//         printf("\nInserted %d at rear.",nn->data);
//         return nn;
//     }else{
//         NODE T=head;
//         while(T->link!=NULL)
//             T=T->link;
//             T->link=nn;
//         }
//         printf("\nInserted %d at end\n",nn->data);
//         return head;
// }
// NODE delete_frnt(NODE head)
// {
//     if(head==NULL)
//     {
//         printf("\nEmpty List..");
//     }else{
//         NODE T=head;
//         head=head->link;
//         printf("\nDeleted %d from front\n",T->data);
//         free(T);
//     }
//     return head;
// }
// NODE delete_rear(NODE head)
// {
//     NODE curr=head,prev=NULL;
//     if(head==NULL)
//     {
//         printf("\nEmpty List...\n");
//         return head;
//     }else{
//         while(curr->link!=NULL)
//         {
//             prev=curr;
//             curr=curr->link;
//         }
//         prev->link=NULL;
//         printf("\nDeleted %d from rear\n",curr->data);
//         free(curr);
//         return head;
//     }
// }

// void display(NODE head) {
//     NODE T = head;
//     while (T != NULL) {
//         printf("%d ", T->data);
//         T = T->link;
//     }
// }

// int main()
// {
//     NODE head=NULL;
//     head=insert_frnt(head,10);
//     head=insert_frnt(head,20);
//     head=insert_frnt(head,30);
//     display(head);
//     head=insert_end(head,50);
//     display(head);
//     head=delete_frnt(head);
//     display(head);
//     head=delete_rear(head);
//     display(head);
//     return 0;
// }











// NODE insertFront(NODE head, int val) {
//     NODE newnode = malloc(sizeof(struct node));
//     newnode->data = val;
//     newnode->link=NULL;
//     if(head==NULL)
//     {
//         newnode->link=head;
//         return newnode;
//     }
//     newnode->link=head;
//     head=newnode;
//     return head;
// }
// NODE insertEnd(NODE head, int val)
// {
//     NODE newnode=malloc(sizeof(struct node));
//     newnode->data=val;
//     newnode->link=NULL;
//     if(head==NULL)
//     {
//         printf("Inserted  %d at rear",newnode->data);
//         return newnode;
//     }
//     NODE T=head;
//     while(T->link!=NULL)
//     {
//         T=T->link;
//     }
//     T->link=newnode;
//     printf("\nInserted %d at rear.\n",newnode->data);
//     return head;
// }
// NODE delete_frnt(NODE head)
// {
//     NODE T=head;
//     if(head==NULL)
//     {
//         printf("Empty list");
//     }else{
//         NODE T=head;
//         head=head->link;
//         printf("\nDeleted %d at front.\n",T->data);
//         free(T);
//     }
//     return head;
// }
// NODE delete_rear(NODE head)
// {
//     if(head==NULL)
//     {
//         printf("Empty List...");
//         return head;
//     }else{
//         NODE curr=head,prev=NULL;
//         while(curr->link!=NULL)
//         {
//             prev=curr;
//             curr=curr->link;
//         }
//         prev->link=NULL;
//         printf("\nDeleted %d from rear\n",curr->data);
//         free(curr);
//         return head;
//     }
// }
// void display(NODE head) {
//     NODE temp = head;
//     while (temp != NULL) {
//         printf("%d ", temp->data);
//         temp = temp->link;
//     }
// }

// int main() {
//     NODE head = NULL;
//     head = insertFront(head, 30);
//     head = insertFront(head, 20);
//     head = insertFront(head, 10);
//     display(head);
//     head=delete_frnt(head);
//     display(head);
//     head=insertEnd(head, 60);
//     display(head);
//     head=delete_rear(head);
//     display(head);
//     return 0;
// }



// #include<stdio.h>
// #include<stdlib.h>

// typedef struct mynode{
//     int data;
//     struct mynode*link;
// }*NODE;

// NODE ins_frnt(NODE h, int data)
// {
//     NODE nn=malloc(sizeof(struct mynode));
//     nn->data=data;
//     if(h==NULL)
//     {
//         nn->link=h;
//         return nn;
//     }
//     nn->link=h;
//     h=nn;
//     return h;
// }
// NODE ins_rear(NODE h, int data)
// {
//     NODE nn=malloc(sizeof(struct mynode));
//     nn->data=data;
//     nn->link=NULL;
//     if(h==NULL)
//     {
//         printf("\nInserted %d at end.\n",nn->data);
//         return nn;
//     }
//     NODE T=h;
//     while(T->link!=NULL)
//     {
//         T=T->link;
//     }
//     T->link=nn;
//     printf("\nInserted %d at rear.\n",nn->data);
//     return h;
// }
// NODE del_frnt(NODE h)
// {
//     if(h==NULL)
//     {
//         printf("\nEmpty List...\n");
//         return h;
//     }
//     NODE T=h;
//     h=h->link;
//     printf("NODE %d deleted at frnt.\n",T->data);
//     free(T);
//     return h;
// }
// NODE del_end(NODE h)
// {
//     if(h==NULL)
//     {
//         printf("\nEmpty List..\n");
//         return h;
//     }
//     NODE curr=h, prev=NULL;
//     while(curr->link!=NULL)
//     {
//         prev=curr;
//         curr=curr->link;
//     }
//     prev->link=NULL;
//     printf("Deleted %d at end.\n",curr->data);
//     free(curr);
//     return h;
// }
// void display(NODE h)
// {
//     NODE T=h;
//     while(T!=NULL)
//     {
//         printf("%d->",T->data);
//         T=T->link;
//     }
//     printf("NULL\n");
// }
// int main(){
//     NODE h=NULL;
//     h=ins_frnt(h,10);
//     h=ins_frnt(h,12);
//     h=ins_frnt(h,14);
//     display(h);
//     h=ins_rear(h,20);
//     h=ins_rear(h,30);
//     display(h);
//     h=del_frnt(h);
//     display(h);
//     h=del_end(h);
//     display(h);
// }

// #include<stdio.h>
// int main(){
//     int i,j,n=5;
//     for(j=0;j<n;j++){
//     for(i=1;i<=n;i++)
//     {
//         printf("%d\t",i);
//     }
//     printf("\n");
// }
//     return 0;

// }