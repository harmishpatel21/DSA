#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *head = NULL;
struct node *current = NULL;

void printList(){
    struct node *p = head;
    while(p!=NULL){
        printf("%d ",p->data);
        p = p->next;
    }
}

void insertAtBegin(int data){
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

void insertAtEnd(int data) {
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
        return;
    }

    struct node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = newNode;
}

int main() {
    
    insertAtEnd(100);
    printList();
    printf("\n");
    insertAtBegin(1);
    printList();
    printf("\n");
    insertAtBegin(2);
    insertAtEnd(3);
    insertAtEnd(1);
    insertAtEnd(10);
    printList();
    return 0;

}
