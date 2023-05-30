# make queue using 2 stacks (ver.1)
import sys
input = sys.stdin.readline

def enqueue(data):
    queue.append(data)

def dequeue():
    # create stack for assistence
    stack = list()
    # put queue data into stack but remain first element
    for i in range(1, len(queue)):
        stack.append(queue.pop())
    # remove first element of queue
    queue.pop()
    # put saved data of stack to queue
    for i in range(len(stack)):
        queue.append(stack.pop())  

def check():
    print(queue[0])

query_cnt = int(input())
queue = list()
    
for _ in range(query_cnt):
    query = input()
    if query[0] == '1':
        data = int(query.split()[1])
        enqueue(data)
    elif query[0] == '2':
        dequeue()
    else:
        check()