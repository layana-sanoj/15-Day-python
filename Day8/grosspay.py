# finding the grosspay
# the rate increases by 1.5% on every hour over 40 hours
hrs=input("Enter Hours: ")
rte=input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rte)
except:
    print("Error, please enter numeric input")
    exit()

if h <=40:
    gp=h*r
else:
    a=40*r
    b=(h-40)*(r*1.5)
    gp=a+b
print('Grosspay=' ,round(gp, 2))
