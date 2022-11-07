# problem link: https://dmoj.ca/problem/ccc16s2
X = int(input())
N = int(input())
d = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
total = 0
p.sort()
if X == 1:
    d.sort()
else:
    d.sort(reverse=True)
for i in range(N):
    total += max(d[i],p[i])
print(total)