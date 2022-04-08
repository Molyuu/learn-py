import random
cpu=random.randint(0,11);
count=0
while True:    
    ins=input("请输入你的猜测:")
    ins=int(ins)
    count+=1
    if ins == cpu:
        print("你牛逼！")
        print("你猜了{}次就猜中啦！".format(count))
        break;
    elif ins<cpu:
        print("小了")
    elif ins>cpu:
        print("大了")