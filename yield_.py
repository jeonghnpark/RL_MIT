p1=1
p2=2

def alternator():
    while True:
        yield p1
        yield p2

def call_alt():
    num=alternator()
    print(num)
    cnt=0
    while True:
        n=next(num)
        print(cnt,":",n)
        cnt+=1
        if cnt>10:
            return

call_alt()