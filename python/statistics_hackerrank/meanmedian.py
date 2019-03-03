from statistics import median, mean, mode
from scipy import stats
a = int(input())
b = [int(b_temp) for b_temp in input().split()]
print(mean(b))
print(median(b))
print(stats.mode(b))