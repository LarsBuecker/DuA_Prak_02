import os

t_ok = 0
for i in range(1, 15):
    if i < 10:
        os.system("python main.py -avl pubInst/00" + str(i) + ".txt > output.txt.sol")
        output = open("output.txt.sol", "r")
        sol = open("pubInst/00" + str(i) + ".txt.sol", "r")
    else:
        os.system("python main.py -avl pubInst/0" + str(i) + ".txt > output.txt")
        output = open("output.txt", "r")
        sol = open("pubInst/0" + str(i) + ".txt.sol", "r")
    out_line = []
    sol_line = []
    for line in output:
        out_line.append(line)
    for line in sol:
        sol_line.append(line)
    output.close()
    sol.close()
    
    c_ok = 0
    for j in range(0, len(sol_line) - 1):
        if sol_line[j] == out_line[j]:
            c_ok += 1
    if c_ok == len(sol_line) - 1:
        t_ok += 1

print(str(t_ok) + " of 15 Test where OK")
        #assert sol_line[j] == out_line[j], "Output is not identical with the solution at file: " + str(i) + " line: " + str(j)
    