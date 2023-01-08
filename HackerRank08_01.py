"""
Find the Runner-Up Score!

Code:
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = sorted(set(arr))[-2]
    print(result)
