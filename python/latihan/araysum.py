from statistics import mean
a = int(input())
b = [int(b_temp) for b_temp in input().split()]
c = mean(b)
print(c.__format__(".2f"))