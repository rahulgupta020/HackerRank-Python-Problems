"""
Find the Runner-Up Score!

Code:
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newset = set(arr)
    newlist = list(newset)
    newlist.sort()
    print(newlist[-2])
