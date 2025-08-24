import math
lengths = [1,6,46,6,3,2]
def choose(n, r):
    ncr = math.factorial(n) / (math.factorial(r) * math.factorial((n - r)))
    return int(ncr)

# def numberof_tables(length):
#     if length % 2 == 0:
#         max_ones = length //2
#         sum = 0
#         for i in range(max_ones):
#             sum += choose(max_ones, i)#max_ones choose i
#         sum = sum *2
#         sum +=1 # to count the config all 0s once
#
#     else: # if length is odd
#         max_ones = length // 2
#         sum = 0
#         for i in range(max_ones): # goes up to max number of 1s - 1 as there is only 1 way to remove all 1s
#             sum += choose(max_ones, i)  # max_ones choose i
#         sum = sum * 3
#         sum +=1# to count the config all 0s once
#     return sum
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
