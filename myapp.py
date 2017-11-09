msg = "Hello World"
print(msg)
msg="Hello Again"
print(msg)

ADMIN_EMAIL = "j148016s"

html = """<html>
<body></body>
</html>"""

print(html)

i= 10
x=10
print(x/3)
print(x//3)
print(x%3)
print(x**3)

y=4
y=y+12
print(y)

print(True or False)
print(True and False)
print(not True)
name = "taguchi"
score = 52.8
print("name: %s,socer: %f" %(name,score))
print("name: %-10s,socer: %10.2f" %(name,score))
score = int(input("socer?"))

if score > 80:
    print("Great")
elif score > 60:
    print("Good")
else:
    print("soso")
print("Great" if score >80 else "soso")

i = 0
while i < 10:
    print(i)
    i+=1
    if i == 5:
        break
else:
    print("end")

