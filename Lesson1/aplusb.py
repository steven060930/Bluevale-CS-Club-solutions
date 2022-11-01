#https://dmoj.ca/problem/aplusb

# input the number of test cases
T = int(input())

for i in range (T):
    # take variables a and b from user input
    a, b = map(int, input().split())

    # print their sum
    print(a + b)