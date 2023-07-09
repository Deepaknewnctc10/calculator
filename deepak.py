f = input("inter your frist number:")
c = input ("inter you comand : +,-,/,*,% =")
s = input("inter your second number: ")
f = int(f)
s = int (s)

if c== '+':
    print(f  + s)
elif c=='-':
    print(f - s)
elif c=='/':
    print (f /s)
elif c=='*':
    print (f * s)
elif c=='%':
    print (f % s)
else:
    print ( "inviled number")
