# problem link: https://dmoj.ca/problem/ccc22s1
num = int(input())
ans = 0
while num >= 0:
    if (num % 5) == 0:
        ans += 1
    num -= 4
print(sol)