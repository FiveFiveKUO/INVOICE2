# 發票對號
win = open("win.txt"). read(). split()
mine = open("mine.txt"). read(). split()
print(win)
print(mine)

cnt = 0
sum = 0
cnt1 = 0
sum1 = 0
cnt2 = 0
sum2 = 0
cnt3 = 0
sum3 = 0
for i, num in enumerate(mine):
    for win_num in win:
        if num == win_num:
            cnt = cnt + 1
            sum = cnt * 1000000
            print("第", i + 1, "張發票中獎", num, "!")

        elif num[-5:] == win_num[-5:]:
            cnt1 = cnt1 + 1
            sum1 = cnt1 * 5000
            print("第", i + 1, "張發票中獎", num[-5:], "!")

        elif num[-4 : ] == win_num[-4 : ]:
            cnt2 = cnt2 + 1
            sum2 = cnt2 * 1000
            print("第", i + 1, "張發票中獎", num[-4 : ], "!")

        elif num[-3 : ] == win_num[-3 : ]:
            cnt3 = cnt3 + 1
            sum3 = cnt3 * 200
            print("第", i + 1, "張發票中獎", num[-3 : ], "!")

print("頭獎中獎發票共", cnt, "張")
print("頭獎中獎金額共", sum, "元")
print("5碼中獎發票共", cnt1, "張")
print("5碼中獎金額共", sum1, "元")
print("4碼中獎發票共", cnt2, "張")
print("4碼中獎金額共", sum2, "元")
print("3碼中獎發票共", cnt3, "張")
print("3碼中獎金額共", sum3, "元")
print("TOTAL中獎發票共", cnt + cnt1 + cnt2 + cnt3, "張")
print("TOTAL中獎金額共", sum + sum1 + sum2 + sum3, "元")



# # 參考 "對中發票之總發票數" & "對中發票之總金額"
# # 對中發票之總發票數
# cnt = 0
# data = [1, 2, 23, 45, 56]
# for i, num in enumerate(data):
#     if num > 5:
#           cnt = cnt + 1
# print("中獎發票共", cnt, "張")
#
#
# # 對中發票之總金額
# sum = 0
# data = [1, 2, 23, 45, 56]
# for i, num in enumerate(data):
#     sum = sum + num
# print("中獎金額共", sum, "元")




