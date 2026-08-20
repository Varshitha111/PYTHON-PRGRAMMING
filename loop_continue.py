def loop_cotinue(n):
    for i in range(1,n+1):
        if i%3==0:
            continue
        else:
            print(i)
loop_cotinue(10)