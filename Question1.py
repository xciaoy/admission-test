# 定義一個函式，用來找出輸入 list 中最大的數字
def find_max(numbers):
    # 初始值為第一個數字
    max_num = numbers[0]
    # 逐一比較每個數字，如果比目前最大值還大，則更新最大值
    for num in numbers:
        if num > max_num:
            max_num = num
    # 回傳最大值
    return max_num

# 定義一個函式，用來找出目標數字在輸入 list 中的位置
def find_position(numbers, target):
    # 初始值為 -1
    position = -1
    # 比較每個數字，如果找到目標數字，則更新位置並跳出迴圈
    for i in range(len(numbers)):
        if numbers[i] == target:
            position = i
            break
    # 回傳位置
    return position


print(find_max([1, 2, 4, 5]) )  #5
print(find_max([5, 2, 7, 1, 6]) )  #7
print(find_position([5, 2, 7, 1, 6], 5))  #0
print(find_position([5, 2, 7, 1, 6], 7))  #2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  #2(第一個符合條件的位置)
print(find_position([5, 2, 7, 1, 6], 8))  #-1