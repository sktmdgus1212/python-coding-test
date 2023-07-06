import itertools
n, k = map(int, input().split(" "))
alpha = ["a", "n", "i", "c", "t"]

arr = [set(input())-{'a','n','t','i','c'} for _ in range(n)]
# for i in range(n):
#     word = input()
#     word = word.lstrip("anta").rstrip("tica")
#     new_word = ""
#     for w in word:
#         if w in alpha:
#             continue
#         new_word += w
#     arr.append(new_word)

if k < 5:
    print(0)
else:
    k = k - 5
    ans = 0
    before_ans = 0
    for a in arr:
        if not a:
            before_ans += 1
    # 1. 단어 추가
    new_alpha = set()
    for a in arr:
        for al in a:
            new_alpha.add(al)
    if len(new_alpha) <= k:
        print(n)
    else:
        for com in itertools.combinations(new_alpha, k):
            com = set(com)
            temp = 0
            for a in arr:
                if a and a.issubset(com):
                    temp += 1
            
            ans = max(ans, temp)
        print(ans+before_ans)
