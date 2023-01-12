def countdown(i):
    if i <= 0:
        return
    else:
        print(i)
        countdown(i-1)


countdown(10)
