import os
import re
script_dir = os.path.dirname(__file__)
path = input("Enter filename: ")
fname = path
path = "scripts/" + path
path = os.path.join(script_dir, path)
with open(path,"r") as f:
    info = f.read()
info = "".join(info.split("\n"))
fname = re.sub(r"\.\w+", ".py", fname)
path = os.path.join(script_dir, "scripts/" + fname)
f = open(path, "w+")
txt = "asd = ''\nstring = ''\nloop_end = 0\nloop_start = 0\nstr_ind = 0\ncurr = 0\nind = [0]\n"
point = 0
while point < len(info):
    x = info[point]
    if x == "+":
        txt += "ind[curr] += 1\n"
    elif x == "-":
        txt += "ind[curr] -= 1\nif ind[curr] < 0:\n    ind[curr] = 0\n"
    elif x == ">":
        txt += "curr += 1\ntry:\n    ind[curr]\nexcept IndexError:\n    ind.append(0)\n"
    elif x == "<":
        txt += "curr -= 1\nif curr < 0:\n    ind.insert(0,0)\n    curr = 0\n"
    elif x == ".":
        txt += "asd += chr(ind[curr])\n"
    elif x == ",":
        txt += "if string == '':\n    string = input()\ntry:\n    ind[curr] = ord(string[str_ind])\nexcept:\n    ind[curr] = 0\nstr_ind += 1\n"
    elif x == "[":
        txt += "loop_start = point\nloop_end = point+info[point:].index(']')\nif ind[curr] == 0:\n    point = loop_end\n"
    elif x == "]":
        txt += "if ind[curr] != 0:\n    point = loop_start\n"
    elif x == "/":
        txt += "asd += str(ind[curr])\n"
    elif x == "?":
        txt += "ind[curr] = int(input())\n"
    point += 1
txt += "print(asd)\nprint('Program ran successfully.')\ninput('Press any key to continue...')"
f.write(txt)
f.close()
print("Compilation successfull.")
print("File '{}' created.".format(fname))
