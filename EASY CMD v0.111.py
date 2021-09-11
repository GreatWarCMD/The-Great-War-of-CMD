#英国


#国家情况
politics = 50                  #默认政治点数50
stability = 65                 #默认稳定度
wars = 20                      #默认战争支持度
parties = 95                   #政党支持率
speak = 70                     #国际影响力

amry_power = 5                 #陆军战斗力
navy_power = 50                #海军战斗力
air_force_power = 3            #空军战斗力



#国家精神
fake_final_war = "结束所有战争的战争"
# 领导人与国民们都还对世界大战记忆犹新，他们不愿意派出令一代人奔向战壕送死。
#    效果：

Washington_Naval_Treaty = "伦敦海军条约签署国"
navy_power = navy_power - navy_power*0.2
# 我们已经签署了《伦敦海军条约》，因此我们的主力舰规格受到了限制。
#    效果：

George_Ⅴ = "乔治五世"
stability += 15
# 英国人民团结在英国国王的周围，为他们帝国的成就所骄傲，虽然这个帝国正在衰弱。
# 受欢迎的名誉领袖：
#    效果：稳定度+15%

# Edward_Ⅷ = "爱德华八世"  1936.1.20-1936.12.11
# George_Ⅵ = "乔治六世"



#历史系统
print("英国介绍")
print("英国帝国在19世纪末期国力日渐衰弱，而22年前那场前所未有的大战让所有英国人至今心有余悸，而1929年美国股市崩盘的危机至今仍笼罩着大不列颠，罢工，抗议，不满充斥着帝国各个角落，远东的帝国主义势力崛起，近东红色的威胁日趋强大，而法西斯的威胁更是近在眼前...")       #英国介绍

print("是否继续")
print("按0继续")
choice = input("")


if choice == "0":
    print("1931年9月，日军以”满铁事件“为借口，大举入侵中国东北，东北的张学良采取极为消极的态度，在不久后也许日军会攻占整个东北地区")
    print("我们应该采取什么态度")
    print("请按对应数字代表您的态度")
    print("1  这当然是不对的，但我们似乎无能为力    效果：国际影响力-1 政党支持率-3")
    print("2  向日本提出强烈外交抗议    效果：国际影响力-3 政党支持率+2")
    print("3  警告日本政府，并对日禁运  效果：国际影响力-5 政党支持率-5 稳定度-3 战争支持度+5 ")
    choice = int(input(""))
    if choice == 1:
        speak = speak - 1
        parties = parties - 3
    elif choice == 2:
        speak = speak - 3
        parties = politics + 2
    elif choice == 3:
        speak = speak - 5
        parties = politics - 5
        stability = stability - 3
        wars = wars + 5
else:
    print("输入错误")
    print("退出游戏")
    pass


#查看国家精神
print("如果您想查看您的国家精神，请按0")
print("不想查看请按其他任意键")
choice = input("")
if choice == "0":
    print(fake_final_war)
    print("# 领导人与国民们都还对世界大战记忆犹新，他们不愿意派出另一代人奔向战壕送死。")
    print("#    效果：陆军战斗力-30%  海军战斗力-5%  空军知道了-10%")
    print("")
    print(Washington_Naval_Treaty)
    print("# 我们已经签署了《伦敦海军条约》，因此我们的主力舰规格受到了限制。")
    print("#    效果：海军战斗力-20%")
    print("")
    print(George_Ⅴ)
    print("# 英国人民团结在英国国王的周围，为他们帝国的成就所骄傲，虽然这个帝国正在衰弱。")
    print("# 受欢迎的名誉领袖：")
    print("#    效果：稳定度+15%")
    print("")
    # print(Edward_Ⅷ)  1936.1.20-1936.12.11
    # print(George_Ⅵ)
else:
    print("跳过查看国家精神")




#查看基本概况
print("如果您想查看国家的基本概况，请按0")
choice = input("")
if choice == "0":
    print(f"政治点数：{politics}")  # 默认政治点数50
    print(f"稳定度：{stability}")  # 默认稳定度
    print(f"战争支持度：{wars}")  # 默认战争支持度
    print(f"政党支持率：{parties}")  # 政党支持率
    print(f"国际影响力：{speak}")  # 国际影响力

    print(f"陆军战斗力：{amry_power}")  # 陆军战斗力
    print(f"海军战斗力：{navy_power}")  # 海军战斗力
    print(f"空军战斗力：{air_force_power}")  # 空军战斗力
else:
    print("跳过查看国家基本概况")


print("是否继续")
print("按0继续")
choice = input("")


if choice == "0":
    print("1932年2月，满洲国在东北正是建立，是日本人为扶持爱新觉罗~溥仪重登大宝的建立的政权，但是许多人怀疑这是日本为继续侵略塞利斯所建立的傀儡政权，溥仪只是个笼中鸟罢了...")
    print("我们应该采取什么态度")
    print("请按对应数字代表您的态度")
    print("1  忠诚的日本人正在为他们的主子复辟    效果：获得“对日关友好”  稳定度+3")
    print("2  这是日本人与中国人的事，我们无权过问，但我们最好告诉日本人不要太嚣张    效果：国际影响力-1 ")
    print("3  这毫无疑问是变相的侵略，国际联盟应立即前往满洲国进行调查其合法性  效果：国际影响力+2  稳定度-2 战争支持度+2 ")



# 总价成效果
fake_final_war = "结束所有战争的战争"
# 领导人与国民们都还对世界大战记忆犹新，他们不愿意派出令一代人奔向战壕送死。
#    效果：陆军战斗力-30%  海军战斗力-5%  空军知道了-10%

Washington_Naval_Treaty = "伦敦海军条约签署国"
# 我们已经签署了《伦敦海军条约》，因此我们的主力舰规格受到了限制。
#    效果：海军战斗力-20%

George_Ⅴ = "乔治五世"
stability += 15
# 英国人民团结在英国国王的周围，为他们帝国的成就所骄傲，虽然这个帝国正在衰弱。
# 受欢迎的名誉领袖：
#    效果：稳定度+15%

amry_power = amry_power - amry_power*0.3
navy_power = navy_power - navy_power*0.25
air_force_power = air_force_power - air_force_power* 0.1



#查看国家精神
print("如果您想查看您的国家精神，请按0")
print("不想查看请按其他任意键")
choice = input("")
if choice == "0":
    print(fake_final_war)
    print("# 领导人与国民们都还对世界大战记忆犹新，他们不愿意派出另一代人奔向战壕送死。")
    print("#    效果：陆军战斗力-30%  海军战斗力-5%  空军知道了-10%")
    print("")
    print(Washington_Naval_Treaty)
    print("# 我们已经签署了《伦敦海军条约》，因此我们的主力舰规格受到了限制。")
    print("#    效果：海军战斗力-20%")
    print("")
    print(George_Ⅴ)
    print("# 英国人民团结在英国国王的周围，为他们帝国的成就所骄傲，虽然这个帝国正在衰弱。")
    print("# 受欢迎的名誉领袖：")
    print("#    效果：稳定度+15%")
    print("")
    # print(Edward_Ⅷ)  1936.1.20-1936.12.11
    # print(George_Ⅵ)
else:
    print("跳过查看国家精神")




#查看基本概况
print("如果您想查看国家的基本概况，请按0")
choice = input("")
if choice == "0":
    print(f"政治点数：{politics}")  # 默认政治点数50
    print(f"稳定度：{stability}")  # 默认稳定度
    print(f"战争支持度：{wars}")  # 默认战争支持度
    print(f"政党支持率：{parties}")  # 政党支持率
    print(f"国际影响力：{speak}")  # 国际影响力

    print(f"陆军战斗力：{amry_power}")  # 陆军战斗力
    print(f"海军战斗力：{navy_power}")  # 海军战斗力
    print(f"空军战斗力：{air_force_power}")  # 空军战斗力
else:
    print("跳过查看国家基本概况")