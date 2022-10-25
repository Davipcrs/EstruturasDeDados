#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

void printlist(struct node* head); //ok
void append(struct node** head, int data); //ok
void pop(struct node** head_ref); //ok
void removeNode(struct node* head, int index);
struct node getNode(struct node* head, int index);
void start(struct node* head, int data);
void getLast(struct node** head, struct node** last); //ok
void getHalf(struct node** head, struct node** half, int len); //ok
int getLen(struct node* head); //ok
void getMax(struct node* head, struct node** max); //ok
void getMin(struct node* head, struct node** min); //ok
void testFunc(struct node* Head, struct node* Half, struct node* Last, int data, int len, struct node* max, struct node* min); //ok


