#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

void printlist(struct node* head);
void append(struct node** head, int data);
void pop(struct node* last);
void removeNode(struct node* head, int index);
void start(int data);
void getLast(struct node* head, struct node* last);
void getHalf(struct node* head, struct node* half, int len);
int getLen(struct node* head);
void getMax(struct node* head, struct node* max);
void getMin(struct node* head, struct node* min);
