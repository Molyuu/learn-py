import random

choices=["石头","剪刀","布"]
cpu_score=0
player_score=0


while True:
    ins=input("Please type:(0 代表石头;1 代表剪刀;2 代表布)")
    ins=int(ins)
    cpu=random.randint(0,3)
    if ins==cpu:
        print("平手！\n")
        print(player_score,"VS",cpu_score)
    elif ins==0:
        if cpu==1:
            print("你赢啦！\n")
            player_score=player_score+1
            print(player_score,"VS",cpu_score)
        elif cpu==2:
            print("你输啦！\n")
            cpu_score=cpu_score+1
            print(player_score,"VS",cpu_score)
    elif ins==1:
        if cpu==0:
            print("你输啦！\n")
            cpu_score=cpu_score+1
            print(player_score,"VS",cpu_score)
        elif cpu==2:
            print("你赢啦！\n")
            player_score=player_score+1
            print(player_score,"VS",cpu_score)

    elif ins==2:
        if cpu==1:
            print("你输啦！\n")
            cpu_score=cpu_score+1
            print(player_score,"VS",cpu_score)
        elif cpu==0:
            print("你赢啦！\n")
            player_score=player_score+1
            print(player_score,"VS",cpu_score)

    elif cpu_score==5 or player_score==5:
        print("游戏结束！")
        print("电脑得分：",cpu_score)
        print("玩家得分：",player_score)
        if cpu_score > player_score:
            print("电脑胜利！")
        else:
            print("玩家胜利！")
            break;
