for i in range(1, 24+1):
    if i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    elif i%15==0:
        print("fizzbuzz")
    else:
        print(i)
