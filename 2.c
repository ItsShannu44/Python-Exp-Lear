// #include <stdio.h>
// #include <stdlib.h>
// #define MAX 5

// typedef struct MyQ {
//     int q[MAX];
//     int front, rear;
// } *QUEUE;

// QUEUE create_Queue(void)
// {
//     QUEUE Q = malloc(sizeof(struct MyQ));
//     Q->front = Q->rear = -1;
//     return Q;
// }

// int isFull(QUEUE Q)
// {
//     return (Q->rear == MAX - 1);
// }

// int isEmpty(QUEUE Q)
// {
//     return (Q->front == -1);
// }

// QUEUE enqueue(QUEUE Q, int E)
// {
//     if (!isFull(Q))
//     {
//         Q->q[++Q->rear] = E;
//         if (Q->front == -1)
//             Q->front = 0;
//     }
//     else
//     {
//         printf("\nQueue is full.");
//     }
//     return Q;
// }

// QUEUE dequeue(QUEUE Q)
// {
//     if (!isEmpty(Q))
//     {
//         printf("\nDeleted: %d", Q->q[Q->front]);

//         if (Q->front == Q->rear)
//             Q->front = Q->rear = -1;
//         else
//             Q->front++;
//     }
//     else
//     {
//         printf("\nQueue is empty.");
//     }
//     return Q;
// }

// QUEUE display(QUEUE Q)
// {
//     if (!isEmpty(Q))
//     {
//         printf("\nQueue: ");
//         for (int i = Q->front; i <= Q->rear; i++)
//         {
//             printf("%d ", Q->q[i]);
//         }
//     }
//     else
//     {
//         printf("\nEmpty Queue.");
//     }
//     return Q;
// }

// int main()
// {
//     QUEUE q = create_Queue();

//     enqueue(q, 10);
//     enqueue(q, 20);
//     enqueue(q, 30);
//     display(q);

//     dequeue(q);
//     display(q);

//     enqueue(q, 40);
//     enqueue(q, 50);
//     enqueue(q, 60); 
//     display(q);

//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #define MAX 5

// typedef struct MyQ {
//     int q[MAX];
//     int front, rear;
// } *QUEUE;

// QUEUE create_Queue(void)
// {
//     QUEUE Q = malloc(sizeof(struct MyQ));
//     Q->front = Q->rear = -1;
//     return Q;
// }
// int isFull(QUEUE Q)
// {
//     return ((Q->rear + 1) % MAX == Q->front);
// }
// int isEmpty(QUEUE Q)
// {
//     return (Q->front == -1);
// }

// QUEUE enqueue(QUEUE Q, int E)
// {
//     if (!isFull(Q))
//     {
//         if (Q->front == -1) 
//             Q->front = 0;

//         Q->rear = (Q->rear + 1) % MAX;
//         Q->q[Q->rear] = E;
//     }
//     else
//     {
//         printf("\nQueue is full.");
//     }
//     return Q;
// }

// QUEUE dequeue(QUEUE Q)
// {
//     if (!isEmpty(Q))
//     {
//         printf("\nDeleted: %d", Q->q[Q->front]);

//         if (Q->front == Q->rear)
//             Q->front = Q->rear = -1;
//         else
//             Q->front = (Q->front + 1) % MAX;
//     }
//     else
//     {
//         printf("\nQueue is empty.");
//     }
//     return Q;
// }

// QUEUE display(QUEUE Q)
// {
//     if (!isEmpty(Q))
//     {
//         printf("\nQueue: ");

//         int i = Q->front;
//         while (1)
//         {
//             printf("%d ", Q->q[i]);
//             if (i == Q->rear)
//                 break;
//             i = (i + 1) % MAX;
//         }
//     }
//     else
//     {
//         printf("\nEmpty Queue.");
//     }
//     return Q;
// }

// int main()
// {
//     QUEUE q = create_Queue();

//     enqueue(q, 10);
//     enqueue(q, 20);
//     enqueue(q, 30);
//     enqueue(q, 40);
//     display(q);

//     dequeue(q);
//     dequeue(q);
//     display(q);

//     enqueue(q, 50);
//     enqueue(q, 60); 
//     enqueue(q, 70); 
//     display(q);

//     return 0;
// }


// #include<stdio.h>
// #include<stdlib.h>

// typedef struct MyNode{
//     int data;
//     struct MyNode*llink, *rlink;
// }*NODE;

// NODE create_node(int data)
// {
//     NODE nn=malloc(sizeof(struct MyNode));
//     if(nn==NULL)
//     {
//         printf("NO MEM!!");
//         exit(0);
//     }
//     nn->data=data;
//     nn->llink=nn->rlink=NULL;
//     return nn;
// }

// NODE ins_frnt(NODE H, int data)
// {
//     NODE nn=create_node(data);
//     if(H==NULL)
//     {
//         return nn;
//     }else{
//         H->llink=nn;
//         nn->rlink=H;
//         H=H->llink;
//         return H;
//     }
// }
// NODE ins_rear(NODE H, int data)
// {
//     if(H==NULL)
//         return(create_node(data));
//     NODE curr=H;
//     while(curr->rlink!=NULL)
//         curr=curr->rlink;
//     curr->rlink=create_node(data);
//     curr->rlink->llink=curr;
//     return H;
// }

// NODE del_frnt(NODE H)
// {
//     if(H==NULL)
//     {
//         printf("Empty list");
//         return H;
//     }
//     if(H->rlink==NULL)
//     {
//         free(H);
//         return NULL;
//     }else{
//         H=H->rlink;
//         free(H->llink);
//         H->llink=NULL;
//     }
// }

// NODE del_rear(NODE H)
// {
//     NODE curr=H;
//     while(curr->rlink->rlink!=NULL)
//     {
//         curr=curr->rlink;
//     }
//     free(curr->rlink);
//     curr->rlink=NULL;
//     return H;
// }

// void display(NODE H)
// {
//     NODE curr=H;
//     while(curr!=NULL)
//     {
//         printf("%d->",curr->data);
//         curr=curr->rlink;
//     }
//     printf("NULL");
//     printf("\n");
// }
// int main()
// {
//     NODE H=NULL;
//     H=ins_frnt(H,10);
//     H=ins_frnt(H,8);
//     H=ins_frnt(H,6);
//     display(H);
//     H=ins_rear(H,12);
//     H=ins_rear(H,14);
//     display(H);
//     H=del_frnt(H);
//     display(H);
//     H=del_rear(H);
//     display(H);
//     return 0;
// }




// #include <stdio.h>
// #define MAX 5

// typedef struct {
//     int arr[MAX];
//     int top;
// } STACK;

// void push(STACK *s, int element) {
//     if (s->top == MAX - 1) {
//         printf("\nStack Overflow! Cannot push %d", element);
//         return;
//     }
//     s->arr[++(s->top)] = element;
//     printf("\nPushed: %d", element);
// }

// void pop(STACK *s) {
//     if (s->top == -1) {
//         printf("\nStack Underflow!");
//         return;
//     }
//     printf("\nPopped: %d", s->arr[s->top]);
//     s->top--;
// }

// void peek(STACK *s) {
//     if (s->top == -1) {
//         printf("\nStack is Empty!");
//         return;
//     }
//     printf("\nTop Element: %d", s->arr[s->top]);
// }

// void display(STACK *s) {
//     if (s->top == -1) {
//         printf("\nStack is Empty!");
//         return;
//     }

//     printf("\nStack Elements: ");
//     for (int i = s->top; i >= 0; i--)
//         printf("%d ", s->arr[i]);
// }

// int main() {
//     STACK s;
//     s.top = -1; 

//     push(&s, 10);
//     push(&s, 20);
//     push(&s, 30);
//     display(&s);

//     pop(&s);
//     display(&s);

//     peek(&s);

//     push(&s, 40);
//     push(&s, 50);
//     push(&s, 60); 
//     display(&s);

//     return 0;
// }


#include<stdio.h>
#include<stdlib.h>

typedef struct mynode{
    int data;
    struct mynode *llink,*rlink;
}*NODE;

NODE create_node(int data)
{
    NODE nn=malloc(sizeof(struct mynode));
    if(nn==NULL)
    {
        printf("No Mem!!");
        exit(1);
    }
    nn->data=data;
    nn->llink=nn->rlink=NULL;
    return nn;
}
NODE ins_frnt(NODE H,int data)
{
    NODE nn=create_node(data);
    if(H==NULL)
    {
        return nn;
    }else{
        H->llink=nn;
        nn->rlink=H;
        H=H->llink;
        return H;
    }
}
NODE ins_rear(NODE H, int data)
{
    if(H==NULL)
        return (create_node(data));
    NODE curr=H;
    while(curr->rlink!=NULL)
        curr=curr->rlink;
    curr->rlink=create_node(data);
    curr->rlink->llink=curr;
    return H;
}
NODE del_frnt(NODE H)
{
    if(H==NULL)
    {
        printf("Empty List");
        return H;
    }
    if(H->rlink==NULL)
    {
        free(H);
        return NULL;
    }
    else{
        H=H->rlink;
        free(H->llink);
        H->llink=NULL;
    }
}
NODE del_rear(NODE H)
{
    NODE curr=H;
    while(curr->rlink->rlink!=NULL)
    {
        curr=curr->rlink;
    }
    free(curr->rlink);
    curr->rlink=NULL;
    return H;
}
void display(NODE H)
{
    NODE curr=H;
    while(curr!=NULL)
    {
        printf("%d->",curr->data);
        curr=curr->rlink;
    }
    printf("NULL\n");
}
int main()
{
    NODE H=NULL;
    H=ins_frnt(H,10);
    H=ins_frnt(H,5);
    display(H);
    H=ins_rear(H,15);
    display(H);
    H=del_frnt(H);
    display(H);
    H=del_rear(H);
    display(H);
    return 0;
}