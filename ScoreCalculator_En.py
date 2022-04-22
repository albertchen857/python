import easygui
def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a
c1=0
c2=0
c3=0
#a1/a2 +-*/ b1/b2 = sum1/sum2
easygui.msgbox("Score calculator",title="great caculator")
n1=input("Score calculator·Click ENTER to enter the tutorial ")
n1=input('''====================
input1:Fraction1 molecular
input2:Fraction1 denominator
input3:calculating signs[+plus -minus *Multiplication /division]
input4:Fraction2 molecular
input5:Fraction2 denominator
Click ENTER go ahead''')
while True:
    a1=int(input("Fraction1 molecular:"))
    a2=int(input("Fraction1 denominator:"))
    a=input("calculating signs[+plus -minus *Multiplication /division]:")
    b1=int(input("Fraction2 molecular:"))
    b2=int(input("Fraction2 denominator:"))
    if a=="+":
        c1=a2
        c2=b2
        a2=a2*c2
        b2=b2*c1
        a1=a1*c2
        b1=b1*c1
        c1=a1+b1
        c2=a2
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"+",b1,"/",b2,"=",int(sum1),"/",int(sum2))
    elif a=="-":
        c1=a2
        c2=b2
        a2=a2*c2
        b2=b2*c1
        a1=a1*c2
        b1=b1*c1
        c1=a1-b1
        c2=a2
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"-",b1,"/",b2,"=",int(sum1),"/",int(sum2))
    elif a=="*":
        c1=a1*b1
        c2=a2*b2
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"x",b1,"/",b2,"=",int(sum1),"/",int(sum2))
    elif a=="/":
        c1=a1*b2
        c2=a2*b1
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"÷",b1,"/",b2,"=",int(sum1),"/",int(sum2))
    n2=input("whether to quit(Y-N/ENTER)")
    if n2=="Y":
        break
