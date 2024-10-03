#include <stdio.h>
#define MAXSIZE 5

int stack[MAXSIZE];
int top = -1;

int isFull(){
    return top == MAXSIZE - 1;
}

int isEmpty(){
    return top == -1;
}

void printStack() {
    if (isEmpty()) {
        printf("Stack is empty!\n");
    } else {
        printf("Stack: ");
        for (int i = 0; i <= top; i++) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

int push(int data){
    if(!isFull()) {
        top = top + 1;
        stack[top] = data;
    } else {
        printf("Stack is full!!");
    }
}

int pop() {
    int data;
    if(!isEmpty()) {
        data = stack[top];
        top = top - 1;
        return data;
    } else {
        printf("Stack is Empty!!");
    }
}

int main() {
    push(44);
    push(10);
    push(50);
    push(1);
    push(44);
    push(10);
    push(50);
    push(1);
    
    printStack();

    int data = pop();
    
    printStack();
    return 0;
}
