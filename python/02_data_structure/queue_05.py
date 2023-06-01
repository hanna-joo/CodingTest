# make queue using 2 stacks (ver.2)
import sys

input = sys.stdin.readline


def data_move():
    # check if stack_pop is empty
    if not stack_pop:
        # empty : move data from stack_push to stack_pop
        for i in range(len(stack_push)):
            stack_pop.append(stack_push.pop())


def enqueue(data):
    stack_push.append(data)


def dequeue():
    data_move()
    stack_pop.pop()


def check():
    data_move()
    if stack_pop:
        print(stack_pop[-1])


query_cnt = int(input())
stack_push, stack_pop = list(), list()

for _ in range(query_cnt):
    query = input()
    if query[0] == "1":
        data = int(query.split()[1])
        enqueue(data)
    elif query[0] == "2":
        dequeue()
    else:
        check()
