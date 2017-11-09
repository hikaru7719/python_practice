msg = "hello"

def say_hi():
    msg = "hello global"
    print(msg)

def say_hi2():
    print(msg)

def say_hi3():
    global msg
    msg="hello global"
    print(msg)



say_hi()
say_hi2()
say_hi3()
print(msg)
