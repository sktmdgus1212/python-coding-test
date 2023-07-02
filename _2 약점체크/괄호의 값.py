arr = input()

tf = True
stack = []

ans = 0
val = 1
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
        val *= 2
    elif arr[i] == "[":
        stack.append(arr[i])
        val *= 3
    else:
        if arr[i] == ")":
            if not stack or stack[-1] == "[":
                tf = False
                break
            if arr[i-1] == "(":
                ans += val
            stack.pop()
            val //= 2
   
        elif arr[i] == "]":
            if not stack or stack[-1] == "(":
                tf = False
                break
            if arr[i-1] == "[":
                ans += val
            stack.pop()
            val //= 3
            

if stack or tf == False:
    print(0)
else:
    print(ans)