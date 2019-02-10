"""
https://atcoder.jp/contests/practice/tasks/practice_1
"""


def parse():
    a = int(input())
    b, c = list(map(int, input().split()))
    s = input()
    return a, b, c, s


def solve(a, b, c, s):
    print("%d %s" % (a + b + c, s))


if __name__ == '__main__':
    inputs = parse()
    solve(*inputs)
