# 計算幾次方
def pow(x,y):
    print(f"{x}的{y} 次方:{x**y}")




def get_discount(total):
    if total >= 2000:
        total -= 200*(total//2000)
    return total

if __name__ == "__main__":
# 測試模組
    pow(2,4)
    result = get_discount(5000)
    print(f'折扣後金額: {result} 元')



# 簡單斷句




