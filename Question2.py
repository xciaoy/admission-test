# 定義一個函式，用來計算輸入 list 中每個元素的數量
def count(input):
    # 建立一個空的字典
    result = {}
    # 逐一處理輸入 list 中的每個元素
    for element in input:
        # 如果字典中已經有這個元素，則將對應的值加 1
        if element in result:
            result[element] += 1
        # 否則新增一個新的鍵值對
        else:
            result[element] = 1
    # 回傳結果
    return result

# 定義一個函式，用來將輸入 list 中相同 key 的 value 加總起來
def group_by_key(input):
    # 建立一個空的字典
    result = {}
    # 逐一處理輸入 list 中的每個元素
    for element in input:
        # 取出 key 和 value
        key = element['key']
        value = element['value']
        # 如果字典中已經有這個 key，則將對應的 value 加上目前的 value
        if key in result:
            result[key] += value
        # 否則新增一個新的鍵值對
        else:
            result[key] = value
    # 回傳結果
    return result

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # 印出 {'a': 3, 'b': 1, 'c': 2, 'x': 1}
input2 = [{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}]
print(group_by_key(input2))  # 印出 {'a': 6, 'b': 1, 'c': 7}