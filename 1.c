#include<stdio.h>
#include<stdlib.h>

typedef struct mynode{
    int data;
    struct mynode*link;
}*NODE;

NODE Create_Node(int data)
{
    NODE nn=malloc(sizeof(struct mynode));
    if(nn==NULL)
    {
        printf("\n\t NO MEMORY");
        exit(1);
    }  
nn->data=data;
nn->link=NULL;
return nn;
}

NODE Insert_at_front(NODE H,int data)
{
    NODE nn=Create_Node(data); 
    if(H==NULL)
    {
        return nn;
    }else{
        nn->link=H;
        return nn;
    }
}

void Display(NODE H)
{
    if(H ==NULL)
    {
        printf("\n List is Empty");
        return;
    }
    printf("Linked list ele:");
    while(H!=NULL)
    {
        printf("%d->",H->data);
        H=H->link;
    }
    printf("NULL \n");
}

int main()
{
    NODE H=NULL;
    NODE n1 = Create_Node(10);
    printf("Node created with data: %d\n", n1->data);
    H=Insert_at_front(H,80);
    H=Insert_at_front(H,60);
    Display(H);
    return 0;
}
