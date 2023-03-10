from bisect import bisect_left, bisect_right
n, x = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

def bisect_count(arr, a):
 left = bisect_left(arr, a)
 right = bisect_right(arr, a)
 return right - left

print(bisect_count(arr, x))