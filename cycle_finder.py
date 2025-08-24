fg_map = {}
k = 6

def mapper(og_num):
    mapped_num = og_num[1:]
    a = og_num[0]
    b = og_num[1]
    c = og_num[2]
    if b == "1" and c == "1":
        if a == "0":
            mapped_num += "1"
        else:
            mapped_num += "0"
    else:
        mapped_num += a
    return mapped_num

for i in range(2**k):
    bin_num = bin(i)[2:] # removing leading 0b
    to_add = k - len(bin_num)
    bin_num = ("0" * to_add) + bin_num
    fg_map[bin_num] = mapper(bin_num)

#print(fg_map)
def cycle_finder(start):
    cycle = []
    current = start
    map_out = None
    flag = False
    while not flag:
        map_out = fg_map[current]
        cycle.append(current)
        #print(current, map_out)

        if map_out == start:
            flag = True
        current = map_out

    return cycle

cycles_list = []
for starter in fg_map:
    if any(starter in sublist for sublist in cycles_list) == False:
        cycle = cycle_finder(starter)
        cycles_list.append(cycle)

for sublist in cycles_list:
    print(f"LENGTH: {len(sublist)} \t {sublist}")




