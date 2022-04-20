"""дз 182,  323,  560"""
#182
def task182():
    n = int(input("enter n: "))
    list = [int(input()) for i in range(0, n)]
    amount = 0
    sum = 0

    for i in range(0, n):
        if list[i] % 5 == 0 and not(list[i] % 7 == 0):
            amount += 1
            sum += list[i]

    print(amount, sum, sep=", ")

#323
def task323():
    n = int(input("enter n: "))
    tmp = n-1
    while tmp != 0:
        for i in range(tmp, 0, -1):
            tmp1 = tmp
            tmp2 = i
            while tmp2 != 0 and tmp1 != 0:
                if tmp2>tmp1:
                    tmp2 = tmp2 % tmp1
                else:
                    tmp1 = tmp1 % tmp2

            if tmp2+tmp1==1:
                print(tmp, i, sep=", ")
        tmp -= 1

#560
def task560():
    f = 0
    for ch in range(200, 301):
        if ch != f:
            sum1 = 0
            for i in range(1, ch):
                if ch % i == 0:
                    sum1 += i
            sum2 = 0
            for j in range(1, sum1):
                if sum1 % j == 0:
                    sum2 += j
            if sum2 == ch != sum1:
                print(ch, sum1)
                f = sum1

if __name__ == "main":
    print("Task182: ")
    task182()
    print("Task323: ")
    task323()
    print("Task560: ")
    task560()