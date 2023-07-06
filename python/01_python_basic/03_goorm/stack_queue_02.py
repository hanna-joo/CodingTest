# 체크카드
# keyword : 시뮬레이션, 큐
# return : deposit, pay, reservation을 모두 수행한 체크 카드의 잔액 출력

"""
1. 큐 (Queue)
- 선입선출(FIFO)
- enqueue, dequeue
"""

def check_card_1(balance, transactions):
    from collections import deque

    reservation = deque()
    for tx in transactions:
        tx_type, tx_amt = tx.split()
        tx_amt = int(tx_amt)
        
        if tx_type == 'deposit':
            balance += tx_amt
            while reservation and (balance >= reservation[0]):
                balance -= reservation.popleft()
        elif tx_type == 'pay':
            if balance >= tx_amt:
                balance -= tx_amt
        else:
            reservation.append(tx_amt)
            while reservation and (balance >= reservation[0]):
                balance -= reservation.popleft()

    return balance


def check_card_2(balance, transactions):
    from collections import deque

    q = deque()
    for tx in transactions:
        op, amt = tx.split()
        amt = int(amt)
        
        if op == 'deposit':
            balance += amt
            while q and (balance >= q[0]):
                balance -= q.popleft()
        elif op == 'pay':
            if balance >= amt:
                balance -= amt
        else:
            if not q and balance >= amt:
                balance -= amt
            else:
                q.append(amt)

    return balance


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(0, ['deposit 10', 'reservation 20', 'pay 5', 'deposit 10', 'deposit 10', 'reservation 6']),
                  (0, ['deposit 10', 'pay 5', 'reservation 5', 'reservation 5', 'pay 5', 'deposit 10'])] # 5, 5
    test_cases.append((int(input()), list(input().rstrip() for _ in range(5))))

    for case in test_cases:
        print(check_card_1(case[0], case[1]))
        print(check_card_2(case[0], case[1]))