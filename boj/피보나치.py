# 백준 1003, 피보나치 함수 https://www.acmicpc.net/problem/1003zxd

def fibonacci(n):
    count_of_zeros = [1, 0]
    count_of_ones = [0, 1]

    if n > 1:
        for i in range(1, n):
            count_of_zeros.append(count_of_zeros[-1] + count_of_zeros[-2])
            count_of_ones.append(count_of_ones[-1] + count_of_ones[-2])

    print(f'{count_of_zeros[n]} {count_of_ones[n]}')


if __name__ == '__main__':

    countOfNumber = int(input())

    for i in range(countOfNumber):
        number = int(input())
        fibonacci(number)
