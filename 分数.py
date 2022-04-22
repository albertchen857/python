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
easygui.msgbox("分数计算器",title="人性化计算器")
n1=input("分数计算器·ENTER进入教程")
n1=input('''====================
输入1:分数1分子
输入2:分数1分母
输入3:运算符号[+加 -减 *乘 /除]
输入4:分数2分子
输入5:分数2分母
ENTER开始使用·好用记得三连''')
while True:
    a1=int(input("分数1分子:"))
    a2=int(input("分数1分母:"))
    a=input("运算符号[+-*/]:")
    b1=int(input("分数2分子:"))
    b2=int(input("分数2分母:"))
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
        print(a1,"/",a2,"+",b1,"/",b2,"=",sum1,"/",sum2)
    n2=input("是否退出(Y-N/ENTER)")
    if a=="-":
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
        print(a1,"/",a2,"-",b1,"/",b2,"=",sum1,"/",sum2)
    n2=input("是否退出(Y-N/ENTER)")
    if a=="*":
        c1=a1*b1
        c2=a2*b2
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"x",b1,"/",b2,"=",sum1,"/",sum2)
    if a=="/":
        c1=a1*b2
        c2=a2*b1
        c3=gcd(c1,c2)
        sum1=c1/c3
        sum2=c2/c3
        print(a1,"/",a2,"÷",b1,"/",b2,"=",sum1,"/",sum2)
    n2=input("是否退出(Y-N/ENTER)")
    if n2=="Y":
        break