a = int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if b+c==d:
        print("+")
    elif b-c==d:
        print("-")
