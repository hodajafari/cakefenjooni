num1=float(input("enter your number"))
op=(input("enter your operation"))
num2=float(input("enter your function"))
if op=='+':
    result=num1+num2
    print("sum of your numbers is :\n" , result)
elif op=='-':
    result=num1-num2
    print("difference of your numbers is :\n" , result)
elif op=='*':
    result=num1*num2
    print("multiplication of your numbers is :\n" , result)
elif op=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="zero definition isn't possible "
else:
    result="your operation ist failed"

print("result of your operation is :\n" , result)
