def is_armstrong_number(number):
    orginal = number
    sum = 0
    f=0
    while number!=0:
        f=f+1
        number=number//10
    number = orginal
    while number!=0:
        d=number%10
        sum=sum+pow(d,f)
        number=number//10
    if sum==orginal:
        return True
    else:
        return False


