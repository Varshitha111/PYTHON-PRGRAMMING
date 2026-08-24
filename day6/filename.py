# file=open("info.txt","r")
# content=file.readlines()
# print(content)
# file.close()
# import sys
# file=open("info1.txt","r").read()
# print(file)
# file=open("info1.txt","w")
# file.write("Hello World\n")
# file.write("Hello World1234")
# file.close()
# content=open("info1.txt","r").read()
# print(content)


import datetime
file=open("hello.py","w")
file.write(f"import datetime\nprint(datetime.datetime.now())")
file=open('hello.py','r')
content=file.read()

print(content)
exec(content)