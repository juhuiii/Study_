sum=0
while True:
    num=int(input("정수를 입력하시오 : "))
    if num!=0:
        sum=sum+num
    else :
        print("합은", str(sum)+"입니다.")
        break;
