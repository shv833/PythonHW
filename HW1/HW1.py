import random

# 182
def task_182(n, l):
    amount = 0
    sum = 0

    for i in range(0, n):
        if l[i] % 5 == 0 and not(l[i] % 7 == 0):
            amount += 1
            sum += l[i]
    return amount, sum

# 323
def task_323(n):
    tmp = n - 1
    list = []
    while tmp != 0:
        for i in range(tmp, 0, -1):
            tmp1 = tmp
            tmp2 = i
            while tmp2 != 0 and tmp1 != 0:
                if tmp2 > tmp1:
                    tmp2 = tmp2 % tmp1
                else:
                    tmp1 = tmp1 % tmp2

            if tmp2 + tmp1 == 1:
                list.append(str(tmp) + ' & ' + str(i))
        tmp -= 1
    return list

# 560
def task_560():
    f = 0
    list = []
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
                list.append(str(ch) + ' ' + str(sum1))
                f = sum1
    return list

if __name__ == "__main__":
    n = int(input("enter n: "))
    random_list = []
    while len(random_list) != n:
        random_list.append(random.randint(1, 100))

    print("Task182: ")
    print("Given list ", random_list)
    print(task_182(n, random_list))
    print("Task323: ")
    print(task_323(n))
    print("Task560: ")
    print(task_560())