# problem link: https://dmoj.ca/problem/ccc18j2
N = int(input())
s = input()
t = input()

ans = 0
for i in range(N):
    if s[i] == 'C' and t[i] == 'C':
        ans += 1

print(ans)