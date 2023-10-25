import sys
arr = list(map(str, sys.stdin.readline().rstrip().split()))
ans = []
for i in range(1, len(arr)):
    val = arr[i][:-1]
    remainder = ""
    name = ""
    for j in range(len(val)):
        if val[j] == "[" or val[j] == "&" or val[j] == "*":
            name = val[:j]
            remainder = val[j:]
            break
    else:
        name = val
    
    #print("name and val: ", name, remainder)
    if remainder == "":
        ans.append(str(arr[0]+ " "+ name+";"))
    else:
        
        remainder_list = []
        for v in remainder:
            if v == "]":
                continue
            if v == "[":
                remainder_list.append("[]")
            else:
                remainder_list.append(v)
        reverse_remainder =""
        for k in range(len(remainder_list)-1, -1, -1):
            reverse_remainder += remainder_list[k]   
        #print("reverse", reverse_remainder)
        ans.append(str(arr[0]+reverse_remainder+" "+name+";")) 
for a in ans:
    print(a)