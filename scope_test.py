x = 16
# As we can see, Python does not check one level above for variables
# the way JS does.

def scopetest2():
    print(x)


def scopetest():
    x = 12
    scopetest2()





print(x)
scopetest()