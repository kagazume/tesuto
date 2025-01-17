for i in range(1, 101):  
    if i % 3 == 0 and i % 5 == 0:  # 3の倍数かつ5の倍数
        print("だいがく爆破したい")
    elif i % 3 == 0:  # 3の倍数
        print("勉強したい")
    elif i % 5 == 0:  # 5の倍数
        print("就活したい")
    else:  # それ以外
        print(i)
