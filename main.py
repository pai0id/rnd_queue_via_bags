from person_arr import read_arr, write_arr, reset_arr
from random import shuffle

save_file = "save.txt"
output_file = "list.txt"

try:
    f_in = open(save_file, "r")
except Exception:
    exit(1)

try:
    f_out = open(output_file, "w")
except Exception:
    exit(1)

arr = read_arr(f_in)
if arr[0].bag_is_empt():
    arr = reset_arr(arr)

names_nums = [(p.get_name(), p.get_num()) for p in arr]

names_nums.sort(key=lambda n_n: n_n[1])

line = []
tmp_arr = []

for i in range(len(names_nums) - 1):
    if not tmp_arr and names_nums[i][1] != names_nums[i + 1][1]:
        line.append(names_nums[i][0])
    elif names_nums[i][1] == names_nums[i + 1][1]:
        tmp_arr.append(names_nums[i][0])
    else:
        tmp_arr.append(names_nums[i][0])
        shuffle(tmp_arr)
        line.extend(tmp_arr)
        tmp_arr = []

if names_nums[len(names_nums) - 1][1] == names_nums[len(names_nums) - 2][1]:
    tmp_arr.append(names_nums[len(names_nums) - 1][0])
    shuffle(tmp_arr)
    line.extend(tmp_arr)
    tmp_arr = []
else:
    line.append(names_nums[len(names_nums) - 1][0])

i = 1
for p in line:
    f_out.write(f"{i}. {p}\n")
    i += 1

f_in.close()
f_in = open(save_file, "w")
write_arr(f_in, arr)
f_in.close()

f_out.close()