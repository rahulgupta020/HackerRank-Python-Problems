"""
Find the Runner-Up Score!

Code:
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    lst.sort()
    print(lst[-2])
