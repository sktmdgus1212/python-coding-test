import sys

n = int(sys.stdin.readline())
ans_arr = []

def convert_bin(val, num, rbrc):
    value = int(val)
    a = ""
    while value > 0:
        if value % 2 == 0:
            a += "0"
        else:
            a += "1"
        value //= 2
    size_a = size(a, num, rbrc)
    return size_a[::-1] 

def find_opcode(op):
    rbrc = "0"
    if op[-1] == "C":
        rbrc = "1"
        op = op[:-1]
    opcode = ""
    if op == "ADD":
        opcode = "0000"
    elif op == "SUB":
        opcode = "0001"
    elif op == "MOV":
        opcode = "0010"
    elif op == "AND":
        opcode = "0011"
    elif op == "OR":
        opcode = "0100"
    elif op == "NOT":
        opcode = "0101"
    elif op == "MULT":
        opcode = "0110"
    elif op == "LSFTL":
        opcode = "0111"
    elif op == "LSFTR":
        opcode = "1000"
    elif op == "ASFTR":
        opcode = "1001"
    elif op == "RL":
        opcode = "1010"
    elif op == "RR":
        opcode = "1011"
    return opcode, rbrc

def size(value, num, rbrc):
    if len(value) == 1:
            value = value + "00"
    elif len(value) == 2:
        value = value + "0"
    
    if num == 1:
        if rbrc == "0": # RB
            value = "0" + value
        else: # #C
            if len(value) == 3:
                value = value + "0" 
    return value

for _ in range(n):
    ans = ""
    op, rd, ra, rb = map(str, sys.stdin.readline().rstrip().split())
    opcode, rbrc = find_opcode(op)

    rd_bin = ""
    if rd == "0":
        rd_bin = "000"
    else:
        rd_bin = convert_bin(rd, 0, rbrc)

    ra_bin = ""
    if ra == "0":
        ra_bin = "000"
    else:
        ra_bin = convert_bin(ra, 0, rbrc)
    
    rb_bin = ""
    if rb == "0":
        rb_bin = "0000"
    else:
        rb_bin = convert_bin(rb, 1, rbrc)
    
    # print(opcode)
    # print(rbrc)
    # print(rd_bin)
    # print(ra_bin)
    # print(rb_bin)
    ans += (opcode + rbrc + "0" + rd_bin + ra_bin + rb_bin)

    ans_arr.append(ans)

for a in ans_arr:
    print(a)