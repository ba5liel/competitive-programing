import math

m, n, a = map(int, input().split())

for_col = math.ceil(m/a)
for_row = math.ceil(n/a) 

print(for_col * for_row)