# 백준 1463, 1로 만들기 https://www.acmicpc.net/problem/146


if __name__ == '__main__':

    numbers = [0, 0]

    number = int(input())
    for i in range(2, number+1):
        numbers.append(numbers[i - 1] + 1)

        if i % 2 == 0:
            numbers[i] = min(numbers[i], numbers[i // 2] + 1)

        if i % 3 == 0:
            numbers[i] = min(numbers[i], numbers[i // 3] + 1)
    print(numbers[number])
