import matplotlib.pyplot as plt
import subprocess

def find_number_before_string(filename, target_string):
    with open(filename, 'r') as file:
        for line in file:
            if target_string in line:
                index = line.find(target_string)
                substring = line[:index]
                number_before_string = substring.split('.')[-2].strip()
                return int(number_before_string)
    return None

subjects = "ABCDEFGHIJKLMNOPQRST"
save_file = open("../save.txt", "w")
for s in subjects:
    save_file.write(f"{s}:\n")
save_file.close()

a_positions = [0 for _ in subjects]

subprocess.run("cd .. && /bin/python3.11 main.py", shell = True, executable="/bin/bash")
for n in range(10):
    num = find_number_before_string(f"../out/list_{n}.txt", "A")
    if not num:
        exit(1)
    a_positions[num - 1] += 1
    
x = [f"{i+1}" for i in range(len(a_positions))]
y = a_positions

plt.bar(x, y)
plt.xlabel('Позиция')
plt.ylabel('Количество раз')
plt.legend()
plt.show()
