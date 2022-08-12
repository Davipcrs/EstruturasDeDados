#include<C:\Users\davip\Documents\Projetos\ED\C\linkedlist.h>




void printlist(struct node* head){
    struct node* n = head;
    
    while(n != NULL){
        printf("%d ", n->data);                                                        //faz o print de toda a linked list.
        n = n->next;
    }

}

void append(struct node** head_ref, int data){                                          //é preciso passar uma posição na memória usando &.
    struct node* new_node = NULL;
    new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;
    
    struct node* last = *head_ref;



    if(*head_ref == NULL){                                                              //caso não exista o 'head' é criado outro.
        *head_ref = new_node;
        return;
    }
    
    while(last->next!=NULL){
        last = last->next;                                                              //Busca o ultimo elemento da lista
    }

    last->next = new_node;                                                              //adiciona o novo valor como sendo o ultimo valor da lista
    return;

    
}


void getLast(struct node* head, struct node* last){
    struct node* aux = head;
    while(aux->next!=NULL){
        aux = aux->next;
    }
    last = aux;
}

int getLen(struct node*head){
    int i = 1;
    struct node* aux = head;

    while(aux->next != NULL){
        aux = aux->next;
        i++;
    }

    return i;
}






int main(){
    int auxData = 10;
    struct node* Head = NULL;
    struct node* Last = NULL;
    struct node* Half = NULL;
    int len = 0;


    //scanf("%d", &auxData);

    Head = (struct node*)malloc(sizeof(struct node));
    Last = Head;
    Head->data = auxData;
    Head->next = NULL;




    append(&Head, 15);
    printlist(Head);
    printf("\n");
    len = getLen(Head);
    printf("%d", len);
    printf("\n");
    getLast(Head, Last);
    append(&Last, 20);
    printlist(Head);
    printf("\n");
    len = getLen(Head);
    
    printf("%d", len);
    printf("\n");
    free(Head);

    return 0;
}
