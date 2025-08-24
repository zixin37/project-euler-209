import math
lengths = [1,6,46,6,3,2]
def choose(n, r):
    ncr = math.factorial(n) / (math.factorial(r) * math.factorial((n - r)))
    return int(ncr)

numof_tables = [0,1,3]
max_length = max(lengths) + 1
for i in range(3,max_length):
    combs = numof_tables[i-1] + numof_tables[i-2]
    numof_tables.append(combs)
print(numof_tables)
total_number = 1
for l in lengths:
    total_number *= numof_tables[l]
print(total_number)

