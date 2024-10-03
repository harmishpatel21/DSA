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

void insertAfterNode(struct node *list, int data) {
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = list->next;
    list->next = newNode;
}

void deleteAtBegin() {
    if(head == NULL) {
        return;
    }
    struct node* temp = head;
    head = head->next;
    free(temp);
}

void deleteAtEnd() {
    if(head == NULL) {
        return;
    }

    if(head->next == NULL) {
        free(head);
        head = NULL;
        return;
    }
    struct node* temp = head;
    while(temp->next->next != NULL) {
        temp = temp->next;
    }
    free(temp->next);
    temp->next = NULL;

}

int main() {
    
    insertAtEnd(100);
    printList();
    printf("\n");
    insertAtBegin(1);
    printList();
    printf("\n");
    deleteAtBegin();
    printList();
    printf("\n");
    insertAtBegin(2);
    insertAfterNode(head->next, 50);
    insertAtEnd(3);
    deleteAtEnd();
    printList();
    printf("\n");
   
    insertAtEnd(1);
    insertAtEnd(10);
    printList();
    return 0;

}
