# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 強制結束 Ctrl + C

# 報錯時 提示使用者「請輸入數字 而不是文字」

# 猜錯三次就不繼續
# 猜對可以 詢問使用者要不要再玩一次
import random
answer = random.randint(1,100)
print(answer)
count = 0
while True:
    try:
        user_input = int(input("請輸入1-100數字:"))
    except ValueError:
        print("請輸入數字 而不是文字")
        continue
    if user_input == answer:
        print("恭喜中獎")
        if input("要不要再玩一次(Y/N)") == "y":
            answer = random.randint(1,100)
            count = 0
            print(answer)
            continue
        else:
            break
    elif user_input < 1 or user_input > 100:
        print("超出範圍請重新執行")
    elif user_input > answer:
        print("請輸入更小的數字")
    else:
        print("請輸入更大的數字")
    count +=1
    if count == 3:
        print("猜超過三次，失敗")
        break









