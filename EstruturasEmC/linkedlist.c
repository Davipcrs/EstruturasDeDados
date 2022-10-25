#include"linkedlist.h"
//comments for commit.
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

void getLast(struct node** head, struct node** last){
    struct node* aux = *head;
    while(aux->next!=NULL){
        aux = aux->next;
    }
    *last = aux;
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

void pop(struct node** head_ref){
    struct node* aux = *head_ref;
    aux = aux->next;   
    
    if (*head_ref==NULL){
        return;
    }
    
    *head_ref = NULL;
    *head_ref = aux;
 
}


void getHalf(struct node** head, struct node** half, int len){
    struct node* aux = *head;
    if(aux == NULL){
        return;
    }

    int auxLen = len/2;
    int i = 0;

    for(i; i<auxLen; i++){
        aux = aux->next;
    }

    *half = aux;

}

void getMax(struct node* head, struct node** Nmax){
    if(head == NULL){
        printf("List not Initialized!");
        return;
    }
    struct node* auxH = head;
    struct node* auxMax = auxH;
    int i;
    while(auxH!=NULL){
        if(auxMax->data < auxH->data){
            auxMax = auxH;
            auxH = auxH->next;
        }
        else{
            auxH = auxH->next;
        }
    }
    
    *Nmax = auxMax;
    
}

void getMin(struct node* head, struct node** Nmin){
    if(head == NULL){
        printf("List not Initialized!");
        return;
    }
    struct node* auxH = head;
    struct node* auxMin = auxH;
    int i;
    while(auxH!=NULL){
        if(auxMin->data > auxH->data){
            auxMin = auxH;
            auxH = auxH->next;
        }
        else{
            auxH = auxH->next;
        }
    }
   
    *Nmin = auxMin;
}

void removeNode(struct node* head, int index){
	if(head == NULL){
		return;	
	}
	int i = 0;
	struct node* aux1 = head;
	while(i<index){
		aux1 = aux1->next;
	}
	struct node auxPrev = *aux1;
	struct node deleted = *aux1->next;
	struct node auxNext = *aux1->next->next;
	
	auxPrev->next = auxNext;
	deleted = NULL;
}

struct node getNode(struct node* head, int index){
    struct node* aux = head;
    struct node aux2;
    for(int i = 0; i<index; i++){
        aux = aux->next;

    }
	aux2 = *aux;


    return aux2;
}

void start(struct node** head, int data){
    struct node *aux = *head;
    aux->data = data;
    aux->next = NULL;
    *head = aux;
}



void testFunc(struct node* Head, struct node* Half, struct node* Last, int data, int len, struct node*max, struct node* min){
    append(&Head, 15);
    printlist(Head);
    printf("\n");
    len = getLen(Head);
    printf("%d", len);
    printf("\n");
    getLast(&Head, &Last);
    append(&Last, 20);
    printlist(Head);
    printf("\n");
    len = getLen(Head);
    
    printf("%d", len);
    printf("\n");
    pop(&Head);
    printlist(Head);
    len = getLen(Head);
    printf("\n");
    printf("%d", len);

    printf("\n");
    append(&Head, 10);
    printlist(Head);
    getLast(&Head, &Last);
    len = getLen(Head);
    getHalf(&Head, &Half, len);
    printf("  %d", Half->data);
    printf("  %d", Last->data);
    append(&Last, 60);
    getHalf(&Head, &Half, getLen(Head));
    getLast(&Head, &Last);

//    removeNode(Head, 1);

    getMax(Head, &max);
    getMin(Head, &min);
    printf("\n");
    printlist(Head);
    printf("  %d", Half->data);
    printf("  %d", Last->data);
    printf("  %d Maior", max->data);
    printf("  %d Menor", min->data);

}


int main(){
    int auxData = 10;
    struct node* Head   =   NULL;
    struct node* Last   =   NULL;
    struct node* Half   =   NULL;
    struct node* NMax   =   NULL;
    struct node* NMin   =   NULL;
    int len = 0;


    //scanf("%d", &auxData);

    Head    =   (struct node*)malloc(sizeof(struct node));
    Last    =   (struct node*)malloc(sizeof(struct node));
    Half    =   (struct node*)malloc(sizeof(struct node));
    NMax    =   (struct node*)malloc(sizeof(struct node));
    NMin    =   (struct node*)malloc(sizeof(struct node));

    Head->data = auxData;
    Head->next = NULL;

    testFunc(Head, Half, Last, auxData, len, NMax, NMin);


    free(Head);
    free(Half);
    free(Last);
    free(NMax);
    free(NMin);

    return 0;
}
