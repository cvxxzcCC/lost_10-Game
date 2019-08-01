# -*- coding: utf-8 -*-
import random

all_times = 0
# 输入尝试试验次数
while all_times <= 0:
    all_times = int(input("您希望重复多少次实验（次数必须至少为1哦）："))
# 当前试验次数 sum
all_sum = 0

# 每次实验时 计数 获胜的方式
# 仅记录 先手 后手 先消 后消 平局 ，共 5 种情况
all_firstlost_win = 0
all_secondlost_win = 0
all_player1_win = 0
all_player2_win = 0
all_draw = 0

# 记录先手 后手 先消 后消 平局 ，各种情况组合而成的情况 ， 共 8 种
all_player1_firstlost_win = 0
all_player2_firstlost_win = 0
all_player1_secondlost_win = 0
all_player2_secondlost_win = 0

all_player1_firstlost_draw = 0
all_player2_firstlost_draw = 0
all_player1_secondlost_draw = 0
all_player2_secondlost_draw = 0


# 一局游戏的战况汇总
def result():
    print("整场战斗 共经历 " + str(all_stage) + "回合")
    print("Stage 1 共经历 " + str(stage1_round) + "回合")
    print("Stage 2 共经历 " + str(stage2_round) + "回合")
    print("Stage 3 共经历 " + str(stage3_round) + "回合")

# 判断 STAGE 1 的战况
def judge_firstlost(player1_firstlost,player2_firstlost,round):
    if player1_firstlost == 1:
        print("在第"+str(round)+"轮时，"+"player1 达成“先消”，player2 达成“后消”")
    if player2_firstlost == 1:
        print("在第"+str(round)+"轮时，"+"player2 达成“先消”，player1 达成“后消”")

# 判断 STAGE 2 的战况     前提是游戏会进入 STAGE 3 ，如果直接获胜 ， 函数不会被调用
def judge_secondlost(player1_secondlost,player2_secondlost,round):
    if player1_secondlost == 1 and player2_secondlost == 0:
        print("在第"+str(round)+"轮时，"+"player1 消除一根手指 双方此时都剩下一只手")
    if player2_secondlost == 1 and player1_secondlost == 0:
        print("在第"+str(round)+"轮时，"+"player2 消除一根手指 双方此时都剩下一只手")

# 输出 当前游戏 进行到 第几轮
def print_gameround(round):
    print("Round "+str(round))

# 输出 游戏中 player1 和 player2 的 手指情况
def print_game(player1,player2):
    print("player1:",player1," player2:",player2)

# 所有游戏试验结束后，计算每一种情况发生的概率
def count_probability(the_thing):
    p = the_thing / all_times
    p = p * 100
    return ('p = %.2f%%' % p),p

# 开始游戏
while True:

    # stage 1初始化

    # player1 任何时候 代表 “先手” ， player2 任何时候代表“后手”
    # player1 和 player2 的左右手 ，游戏开始阶段数值为 1
    player1_left = 1
    player1_right = 1
    player2_left = 1
    player2_right = 1
    player1 = [player1_left,player1_right]
    player2 = [player2_left,player2_right]

    # 判断谁先在 STAGE 1 环节中 消除手指 ，若为 1 则消去，称之为“先消”
    player1_firstlost = 0
    player2_firstlost = 0

    # player1 和 player 2 的手指是随机触碰， 0 代表 左手， 1 代表 右手
    random_player1 = random.randint(0,1)
    random_player2 = random.randint(0,1)

    # round 代表游戏进行轮数
    round = 0
    # normal 判断是否 “正常情况” ， key 是判断 normal 的根据
    normal = 1
    key = 0

    # 开始游戏 stage 1
    print("Stage1 player1 先手")
    print_gameround(round)
    print_game(player1,player2)
    print("--------------------------")

    # stage1 _ round 单纯记录 STAGE 1 的轮数
    stage1_round = 0

    # 只要没有人消手 就继续战斗 STAGE 1
    while len(player1) == 2 and len(player2) == 2:
        # 计算游戏round
        round = round + 1
        print_gameround(round)
        stage1_round += 1

        # 初始化脑力信息
        # hide 判断 是否存在隐藏的 死路
        # key 是判断产生 直接碰10 时 ， 避免两只手同时碰 ， 这种情况下左手右手都一样 ， 默认为右手
        normal = 1
        hide = 0
        key = 0

        # player1 先手
        random_player1 = random.randint(0,1)
        random_player2 = random.randint(0,1)

        # 此时 player1 代表 此时的行动者
        # 在 碰手前，判断是否存在 隐藏的死路
        # 函数会输出 hide 来判断是否有死路 ， safeway 内包含 所有安全的道路
        def hide_lose_safe_way1(player1_left,player1_right,player2_left,player2_right):
            # 初始化信息
            hide = 0
            first_11 = 0
            first_00 = 0
            first_01 = 0
            first_10 = 0
            safe_way = []

            # 判断是否有潜在威胁
            # 主玩家 右手 可能性
            player1_right_future = player1_right + player2_left
            if (player1_right_future + player2_left) % 10 == 0 or (player1_right_future + player2_right) % 10 == 0:
                hide = 1
                hide_10 = 1
                first_10 = 1

            player1_right_future = player1_right + player2_right
            if (player1_right_future + player2_left) % 10 == 0 or  (player1_right_future + player2_right) % 10 == 0:
                hide = 1
                first_11 = 1

            # 主玩家 左手 可能性
            player1_left_future = player1_left + player2_left
            if (player1_left_future + player2_left) % 10 == 0 or (player1_left_future + player2_right) % 10 == 0:
                hide = 1
                first_00 = 1

            player1_left_future = player1_left + player2_right
            if (player1_left_future + player2_left) % 10 == 0 or (player1_left_future + player2_right) % 10 == 0:
                hide = 1
                first_01 = 1

            # hide = 1 代表存在 隐藏的死路 ， 开始寻找安全的出路
            if hide == 1:
                if first_01 == 0:
                    safe_way.append('01')
                if first_00 == 0:
                    safe_way.append('00')
                if first_10 == 0:
                    safe_way.append('10')
                if first_11 == 0:
                    safe_way.append('11')

                return 1,safe_way

            return 0,safe_way

        # 判断是否会产生 二次获胜
        # 如果有 ， 就去寻找安全的道路 ， 不去走 隐藏的死路
        hide,safeway = hide_lose_safe_way1(player1_left,player1_right,player2_left,player2_right)
        if hide == 1:
            if len(safeway) != 0:
                the_way = random.choice(safeway)
                random_player1 = int(the_way[0])
                random_player2 = int(the_way[1])

        # 判断时候可以直接消除 ， 若存在就直接碰手
        if player1_left + player2_right == 10 or player1_left + player2_left == 10 :
           player1_left = 10
           normal = 0
           key = 1
        if key == 0:
            if player1_right + player2_right == 10 or player1_right + player2_left == 10 :
               player1_right = 10
               normal = 0

        # 若无法直接消除 则随机碰
        if normal == 1:
            if random_player1 == 0:
                if random_player2 == 0:
                    player1_left = player1_left + player2_left

            if random_player1 == 0:
                if random_player2 == 1:
                    player1_left = player1_left + player2_right

            if random_player1 == 1:
                if random_player2 == 0:
                    player1_right = player1_right + player2_left

            if random_player1 == 1:
                if random_player2 == 1:
                    player1_right = player1_right + player2_right

        # 结束碰 开始计算数字
        player1_left = player1_left % 10
        player1_right = player1_right % 10
        player1 = [player1_left, player1_right]
        # 展示结果
        print_game(player1,player2)

        # 判断 player1 是否产生 “碰十”
        if player1_left == 0 or player1_right == 0:
            player1_firstlost = 1
            judge_firstlost(player1_firstlost,player2_firstlost,round)
            if player1_left == 0 :
                player1.remove(player1_left)
                break
            if player1_right == 0:
                player1.remove(player1_right)
                break


        # player2 后手
        # hide 判断 是否存在隐藏的 死路
        # key 是判断产生 直接碰10 时 ， 避免两只手同时碰 ， 这种情况下左手右手都一样 ， 默认为右手
        normal = 1
        hide = 0
        key = 0

        # 随机选择 左右手
        random_player1 = random.randint(0,1)
        random_player2 = random.randint(0,1)

        # 判断是否会产生 二次获胜
        hide,safeway = hide_lose_safe_way1(player2_left,player2_right,player1_left,player1_right)
        if hide == 1:
            if len(safeway) != 0:
                the_way = random.choice(safeway)
                random_player2 = int(the_way[0])
                random_player1 = int(the_way[1])


        # 判断是否可以直接消除
        if player2_left + player1_right == 10 or player2_left + player1_left == 10:
            player2_left = 10
            normal = 0
            key = 1
        if key == 0:
            if player2_right + player1_right == 10 or player2_right + player1_left == 10:
                player2_right = 10
                normal = 0

        # 若无法直接消除 则随机碰
        if normal == 1:
            if random_player2 == 0:
                if random_player1 == 0:
                    player2_left = player2_left + player1_left

            if random_player2 == 0:
                if random_player1 == 1:
                    player2_left = player2_left + player1_right

            if random_player2 == 1:
                if random_player1 == 0:
                    player2_right = player2_right + player1_left

            if random_player2 == 1:
                if random_player1 == 1:
                    player2_right = player2_right + player1_right

        # 结束碰 计算结果
        player2_left = player2_left % 10
        player2_right = player2_right % 10
        player2 = [player2_left, player2_right]
        # 展示结果
        print_game(player1,player2)
        print("--------------------------")

        # 判断是否产生“碰十”
        if player2_left == 0 or player2_right == 0:
            player2_firstlost = 1
            judge_firstlost(player1_firstlost, player2_firstlost,round)
            if player2_left == 0:
                player2.remove(player2_left)
                break
            if player2_right == 0:
                player2.remove(player2_right)
                break


    # 此处 STAGE 1 胜负已分
    # 汇报 Stage 1 战况
    print("Stage 1 战况为： ","player1："+str(player1)+"   "+"player2:"+str(player2))
    print("Stage 1 共经历 " + str(stage1_round) + "回合")
    print("\n")



    # stage 2 初始化
    # secondlost 代表Stage 2 的消除情况
    # secondlost 也可以代表 “后消” 情况 ， 若为 1 ，则代表发生“后消”
    player1_secondlost = 0
    player2_secondlost = 0

    # stage2_round 仅用于计算 STAGE 2 的轮数
    stage2_round = 0


    # 开始游戏 stage 2

    # player1_firstlost == 1时 ， player1 只有一根手指 ， player2 有两根手指
    if player1_firstlost == 1:
        print("Stage2 player2 先手")
        while 1:
            round = round + 1
            print_gameround(round)
            stage2_round += 1

            # player 2 先手

            # 初始化脑力信息
            # noemal 是 判断是否为 正常对局
            # hide 判断 是否存在隐藏的 死路
            # key 是判断产生 直接碰 10 时 ， 避免两只手同时碰 ， 这种情况下左手右手都一样 ， 默认为右手
            # first 代表 player 2 判断是否产生 隐藏的死路时 ， 检测出来的安全道路
            normal = 1
            hide = 0
            first = 0
            key = 0

            random_player2 = random.randint(0, 1)
            # 此时player 1 只剩下 一只手 ， 用 player1_flag 表示
            player1_flag = player1[0]

            # player1 是 数值，非列表 ， 默认 player1 是一根手指的玩家
            def hide_lose_danger_way2_1(player1,player2_left,player2_right):
                # 判读左手
                player2_left_future = player2_left + player1
                if (player2_left_future + player1) % 10 == 0:
                    return 1,0

                # 判断右手
                player2_right_future = player2_right + player1
                if (player2_right_future + player1) % 10 == 0:
                    return 1,1

                return 0,None

            # 判断是否有二次胜利
            hide,first = hide_lose_danger_way2_1(player1_flag,player2_left,player2_right)
            if hide == 1:
                while random_player2 == first:
                    random_player2 = random.randint(0,1)

            # 判断是否可以直接消除
            if player2_right + player1[0] == 10:
                player2_right = 10
                normal = 0
                key = 1
            if key == 0:
                if player2_left + player1[0] == 10:
                    player2_left = 10
                    normal = 0

            # 无法直接消除 则随机碰
            if normal == 1:
                if random_player2 == 0:
                    player2_left = player2_left + player1[0]

                if random_player2 == 1:
                    player2_right = player2_right + player1[0]

            # 更新 player2手指信息
            player2_left = player2_left % 10
            player2_right = player2_right % 10
            player2 = [player2_left, player2_right]
            print_game(player1, player2)

            # 判断是否产生“碰十”
            if player2_left == 0 or player2_right == 0:
                player2_secondlost = 1
                judge_secondlost(player1_secondlost, player2_secondlost, round)
                if player2_left == 0:
                    player2.remove(player2_left)
                    break
                if player2_right == 0:
                    player2.remove(player2_right)
                    break

            # player1 后手

            # 初始化脑力信息
            # normal 是判断是否为 正常对局
            # hide 判断 是否存在隐藏的 死路
            # key 是判断产生 直接碰10 时 ， 避免两只手同时碰 ， 这种情况下左手右手都一样 ， 默认为右手
            # second 是判断 player 1 是否存在 隐藏危险时， 检测到的安全道路
            normal = 1
            second = 0
            hide = 0
            key = 0

            random_player2 = random.randint(0, 1)

            # player1 是 数值，非列表， 默认 player1 是 一根手指的玩家
            def hide_lose_danger_way2_2(player1,player2_left,player2_right):
                # 判读对方左手
                player1_future = player2_left + player1
                if (player1_future + player2_left) % 10 == 0 or (player1_future + player2_right) % 10 == 0:
                    return 1,0

                # 判断对方右手
                player1_future = player2_right + player1
                if (player1_future + player2_left) % 10 == 0 or (player1_future + player2_right) % 10 == 0:
                    return 1,1

                return 0,None

            # 判断是否有二次胜利
            hide,first = hide_lose_danger_way2_2(player1_flag,player2_left,player2_right)
            if hide == 1:
                while random_player2 == first:
                    random_player2 = random.randint(0,1)

            # 判断是否可以直接 “碰十”
            if player1[0] + player2_left == 10:
                player1[0] = 10
                normal = 0
                key = 1
            if key == 0:
                if player1[0] + player2_right == 10:
                    player2[0] = 10
                    normal = 0

            # 若无法消 则随机碰
            if normal == 1:
                if random_player2 == 0:
                    player1[0] = player1[0] + player2_left

                if random_player2 == 1:
                    player1[0] = player1[0] + player2_right

            player1[0] = player1[0] % 10
            print_game(player1, player2)
            print("--------------------------")

            # 判断是否“碰十”
            all_stage = stage1_round + stage2_round
            if player1[0] == 0:
                print("在Round",str(round),"时，player1 在 Stage 2 中，连续消除 获胜")
                print("获胜方式：先手，先消")
                print("整场战斗 共经历 " + str(all_stage) + "回合")
                print("Stage 1 共经历 " + str(stage1_round) + "回合")
                print("Stage 2 共经历 " + str(stage2_round) + "回合")
                all_player1_firstlost_win += 1
                all_player1_win += 1
                all_firstlost_win += 1
                break

    # player2_firstlost == 1时 ， player2 只有一根手指 ， player1 有两根手指
    if player2_firstlost == 1:
        print("Stage2 player1 先手")
        while 1:
            round = round + 1
            print_gameround(round)
            stage2_round += 1

            # player1 先手

            # 初始化脑力信息
            # nomal 判断是否为 正常对局
            # hide 判断 是否存在隐藏的 死路
            # key 是判断产生 直接碰10 时 ， 避免两只手同时碰 ， 这种情况下左手右手都一样 ， 默认为右手
            # first判断 player1 是否存在 隐藏的危险 ， 检测所有的安全道路
            normal = 1
            first = 0
            hide = 0
            key = 0

            random_player1 = random.randint(0, 1)
            # 此时 player 2 只有 一只手， 用player2_flag 保存
            player2_flag = player2[0]

            # player1 是 数值，非列表 ， 默认 player1 是 一根手指的玩家
            def hide_lose_danger_way2_1(player1, player2_left, player2_right):
                # 判读左手
                player2_left_future = player2_left + player1
                if (player2_left_future + player1) % 10 == 0:
                    return 1, 0

                # 判断右手
                player2_right_future = player2_right + player1
                if (player2_right_future + player1) % 10 == 0:
                    return 1, 1

                return 0, None

            # 判断是否存在二次胜利
            hide, first = hide_lose_danger_way2_1(player2_flag, player1_left, player1_right)
            if hide == 1:
                while random_player1 == first:
                    random_player1 = random.randint(0, 1)

            # 判断是否可以直接消除
            if player1_right + player2[0] == 10:
                player1_right = 10
                normal = 0
                key = 1
            if key == 0:
                if player1_left + player2[0] == 10:
                    player1_left = 10
                    normal = 0

            # 若无法直接消除 随机碰
            if normal == 1:
                if random_player1 == 0:
                    player1_left = player1_left + player2[0]

                if random_player1 == 1:
                    player1_right = player1_right + player2[0]

            # 碰撞结束 更新数据
            player1_left = player1_left % 10
            player1_right = player1_right % 10
            player1 = [player1_left, player1_right]

            # 汇报战况
            print_game(player1, player2)

            # 判断是否产生“碰十”
            if player1_left == 0 or player1_right == 0:
                player1_secondlost = 1
                judge_secondlost(player1_secondlost, player2_secondlost, round)
                if player1_left == 0:
                    player1.remove(player1_left)
                    break
                if player1_right == 0:
                    player1.remove(player1_right)
                    break

            # player2 后手
            random_player1 = random.randint(0, 1)
            normal = 1
            hide = 0
            key = 0

            # player1 是 数值，非列表 ， 默认player1 是 一根手指的玩家
            def hide_lose_danger_way2_2(player1,player2_left,player2_right):
                # 判读对方左手
                player1_future = player2_left + player1
                if (player1_future + player2_left) % 10 == 0 or (player1_future + player2_right) % 10 == 0:
                    return 1,0

                # 判断对方右手
                player1_future = player2_right + player1
                if (player1_future + player2_left) % 10 == 0 or (player1_future + player2_right) % 10 == 0:
                    return 1,1

                return 0,None

            # 判断是否二次胜利
            hide,first = hide_lose_danger_way2_2(player2_flag,player1_left,player1_right)
            if hide == 1:
                while random_player1 == first:
                    random_player1 = random.randint(0,1)


            # 判断是否可以直接消除
            if player2[0] + player1_left == 10:
                player2[0] == 10
                normal = 0
                key = 1
            if key == 0:
                if player2[0] + player1_right == 10:
                    player2[0] == 10
                    normal = 0

            # 若无法直接消除，则随机碰
            if  normal == 1:
                if random_player1 == 0:
                    player2[0] = player2[0] + player1_left

                if random_player1 == 1:
                    player2[0] = player2[0] + player1_right

            # 更新数据
            player2[0] = player2[0] % 10
            print_game(player1, player2)
            print("--------------------------")

            # 判断是否产生“碰十”
            all_stage = stage1_round + stage2_round
            if player2[0] == 0:
                print("在Round",str(round),"时，player2 在Stage 2 中，连续消除 获胜")
                print("获胜方式：后手，先消")
                print("整场战斗 共经历 " + str(all_stage) + "回合")
                print("Stage 1 共经历 " + str(stage1_round) + "回合")
                print("Stage 2 共经历 " + str(stage2_round) + "回合")
                all_player2_firstlost_win += 1
                all_player2_win += 1
                all_firstlost_win += 1
                break

    # 判断 Stage 2 的战况
    if stage2_round != 0:
        print("Stage 2 战况为：","player1："+str(player1)+"   "+"player2:"+str(player2))
        print("Stage 2 共经历 " + str(stage2_round) + "回合")



    # stage 3 初始化

    # 仅记录 STAGE 3 的 轮数
    stage3_round = 0

    # stage 3 开始游戏

    # stage 3 player2 先手
    # 此时 player 1 后消 ， 必定 player 2 先消
    if player1_secondlost == 1:
        print("\n")
        print("第三阶段 player2 先手")
        while 1:
            round = round + 1
            print_gameround(round)
            stage3_round += 1

            # 判断是否进入死循环
            if stage3_round >= 30:
                print("--------------------------")
                print("陷入死循环，无解，平局")
                if player1_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 后消 ， player 2 先消
                    print("平局方式：进入BO3 player1 先手，player1 先消，player2 后消")
                    all_player1_firstlost_draw += 1
                    all_player2_secondlost_draw += 1
                    all_draw += 1
                    break
                if player2_firstlost == 1:
                    print("平局方式：进入BO3 player1 先手，player2 先消，plyaer1 后消")
                    all_player1_secondlost_draw += 1
                    all_player2_firstlost_draw += 1
                    all_draw += 1
                    break

            # player2 先手
            player2[0] = player2[0] + player1[0]
            player2[0] = player2[0] % 10
            print_game(player1,player2)

            # 判断是否 player2 胜出
            all_stage = stage1_round + stage2_round + stage3_round
            if player2[0] == 0:
                print("--------------------------")
                print("在Round",str(round),"时，player2 在Stage 3 中 获胜")
                if player1_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 后消 ， player 2 先消
                    print("获胜方式：player2 后手，player2 后消")
                    result()
                    all_player2_secondlost_win += 1
                    all_player2_win += 1
                    all_secondlost_win += 1
                    break
                if player2_firstlost == 1:
                    print("获胜方式：player2 后手，player2 先消")
                    result()
                    all_player2_firstlost_win += 1
                    all_player2_win += 1
                    all_firstlost_win += 1
                    break

            # player1 后手
            player1[0] = player1[0] + player2[0]
            player1[0] = player1[0] % 10
            print_game(player1, player2)

            # 判断是否 player1 胜出
            all_stage = stage1_round + stage2_round + stage3_round
            if player1[0] == 0:
                print("--------------------------")
                print("在Round",str(round),"时，player1 在Stage 3 中 获胜")
                if player1_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 后消 ， player 2 先消
                    print("获胜方式：player1 先手，player1 先消")
                    result()
                    all_player1_firstlost_win += 1
                    all_player1_win += 1
                    all_firstlost_win += 1
                    break
                if player2_firstlost == 1:
                    print("获胜方式：player1 先手，player1 后消")
                    result()
                    all_player1_secondlost_win += 1
                    all_player1_win += 1
                    all_secondlost_win += 1
                    break


    # Stage3 player1 先手
    # 此时 player2 后消， 必定player 1 先消
    if player2_secondlost == 1:
        print("\n")
        print("第三阶段 player1 先手")
        while 1:
            round = round + 1
            print_gameround(round)

            stage3_round += 1
            # 判断是否进入死循环
            if stage3_round >= 30:
                print("陷入死循环，无解，平局")
                if player1_firstlost == 1:
                    print("平局方式：进入BO3 player1 先手，player1 先消")
                    all_player1_firstlost_draw += 1
                    all_player2_secondlost_draw += 1
                    all_draw += 1
                    break
                if player2_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 先消 ， player 2 后消
                    print("平局方式：进入BO3 player1 先手，player2 先消")
                    all_player1_secondlost_draw += 1
                    all_player2_firstlost_draw += 1
                    all_draw += 1
                    break

            # player1 先手
            player1[0] = player1[0] + player2[0]
            player1[0] = player1[0] % 10
            print_game(player1,player2)

            # 判断 player1 是否胜出
            all_stage = stage1_round + stage2_round + stage3_round
            if player1[0] == 0:
                print("--------------------------")
                print("在Round",str(round),"时，player1 在Stage 3 中 获胜")
                if player1_firstlost == 1:
                    print("获胜方式：player1 先手，player1 先消")
                    result()
                    all_player1_firstlost_win += 1
                    all_player1_win += 1
                    all_firstlost_win += 1
                    break
                if player2_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 先消 ， player 2 后消
                    print("获胜方式：player1 先手，player1 后消")
                    result()
                    all_player1_secondlost_win += 1
                    all_player1_win += 1
                    all_secondlost_win += 1
                    break

            # player2 后手
            all_stage = stage1_round + stage2_round + stage3_round
            player2[0] = player2[0] + player1[0]
            player2[0] = player2[0] % 10
            print_game(player1, player2)
            print("--------------------------")

            # 判断 player2 是否胜出
            if player2[0] == 0:
                print("在Round",str(round),"时，player2 在Stage 3 中 获胜")
                if player2_firstlost == 1:
                    # 不可能进入这种获胜方式， player 1 先消 ， player 2 后消
                    print("获胜方式：player2 后手，player2 先消")
                    result()
                    all_player2_firstlost_win += 1
                    all_player2_win += 1
                    all_firstlost_win += 1
                    break
                if player1_firstlost == 1:
                    print("获胜方式：player2 后手，player2 后消")
                    result()
                    all_player2_secondlost_win += 1
                    all_player2_win += 1
                    all_secondlost_win += 1
                    break

    # 判断是否到达 总实验次数数目
    all_sum += 1
    if all_sum == all_times:
        break


# 此时 ， 已经达到规定次数
# 统计结果
print("\n")
print("-------------------------------------------------")
print("-------------------------------------------------")
print("\n")
print("总实验次数为：" + str(all_times))
print("所有实验结束，接下来统计实验结果\n")

p_all_player1_win ,p_all_player1_win_number = count_probability(all_player1_win)
p_all_player2_win ,p_all_player2_win_number = count_probability(all_player2_win)
p_all_firstlost_win , p_all_firstlost_win_number = count_probability(all_firstlost_win)
p_all_second_win , p_all_second_win_number = count_probability(all_secondlost_win)
p_all_draw , p_all_draw_number = count_probability(all_draw)

# 判断主要的 5 种情况
print("先手获胜的概率是：" + str(p_all_player1_win))
print("后手获胜的概率是：" + str(p_all_player2_win))
print("先消获胜的概率是：" + str(p_all_firstlost_win))
print("后消获胜的概率是：" + str(p_all_second_win))
print("    平局的概率是：" + str(p_all_draw) + "\n")




print("-------------------------------------------------")
print("-------------------------------------------------\n")


# 判断所有战况 ， 共 8 种
p_all_player1_firstlost_win , p_all_player1_firstlost_win_number = count_probability(all_player1_firstlost_win)
p_all_player2_firstlost_win , p_all_player2_firstlost_win_number = count_probability(all_player2_firstlost_win)
p_all_player1_secondlost_win , p_all_player1_secondlost_win_number = count_probability(all_player1_secondlost_win)
p_all_player2_secondlost_win , p_all_player2_secondlost_win_number= count_probability(all_player2_secondlost_win)
p_all_player1_firstlost_draw , p_all_player1_firstlost_draw_number= count_probability(all_player1_firstlost_draw)
p_all_player2_firstlost_draw , p_all_player2_firstlost_draw_number = count_probability(all_player2_firstlost_draw)
p_all_player1_secondlost_draw, p_all_player1_secondlost_draw_number = count_probability(all_player1_secondlost_draw)
p_all_player2_secondlost_draw, p_all_player2_secondlost_draw_number = count_probability(all_player2_secondlost_draw)

print("先手 + 先消 + 获胜的概率是：" + str(p_all_player1_firstlost_win))
print("后手 + 先消 + 获胜的概率是：" + str(p_all_player2_firstlost_win))
print("先手 + 后消 + 获胜的概率是：" + str(p_all_player1_secondlost_win))
print("后手 + 后消 + 获胜的概率是：" + str(p_all_player2_secondlost_win))
print("先手 + 先消 + 平局的概率是：" + str(p_all_player1_firstlost_draw))
print("后手 + 先消 + 平局的概率是：" + str(p_all_player2_firstlost_draw))
print("先手 + 后消 + 平局的概率是：" + str(p_all_player1_secondlost_draw))
print("后手 + 后消 + 平局的概率是：" + str(p_all_player2_secondlost_draw) + "\n")

# 最大的概率
p_best_right_way = max(p_all_player1_firstlost_win_number , p_all_player2_firstlost_win_number ,
                       p_all_player1_secondlost_win_number , p_all_player2_secondlost_win_number,
                       p_all_player1_firstlost_draw_number , p_all_player2_firstlost_draw_number ,
                       p_all_player1_secondlost_draw_number , p_all_player2_secondlost_draw_number)
# 寻找是哪个 战略产生了最大概率
best_right_way_list = [p_all_player1_firstlost_win_number , p_all_player2_firstlost_win_number ,
                       p_all_player1_secondlost_win_number , p_all_player2_secondlost_win_number,
                       p_all_player1_firstlost_draw_number , p_all_player2_firstlost_draw_number ,
                       p_all_player1_secondlost_draw_number , p_all_player2_secondlost_draw_number]
best_right_way_list_china = ["先手 + 先消 + 获胜" , "后手 + 先消 + 获胜" , "先手 + 后消 + 获胜" , "后手 + 后消 + 获胜",
                             "先手 + 先消 + 平局" , "后手 + 先消 + 平局" , "先手 + 后消 + 平局" , "后手 + 后消 + 平局"]
max_right_item = []
for i in range(0,len(best_right_way_list)):
    if p_best_right_way == best_right_way_list[i]:
        max_right_item.append(i)
for i in range(0,len(max_right_item)):
    right_way = best_right_way_list_china[max_right_item[i]]
# 输出结果
print("在“先手 + 先消 + 获胜”“后手 + 先消 + 获胜”“先手 + 后消 + 获胜”“后手 + 后消 + 获胜”"
      "\n"
      "  “平局”“先手 + 先消 + 平局”“后手 + 先消 + 平局”“先手 + 后消 + 平局”“后手 + 后消 + 平局” 中比较"+ "\n" +
      "最有可能获胜的情况是：" + str(right_way) + "\n" +
      "              概率为：" + str('%.2f%%' % p_best_right_way))

print("\n")
print("所有情况的概率计算完毕！\n")
gameover = input("按Enter结束程序！\n")