
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