# https://leetcode.com/problems/jewels-and-stones/
'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
 
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
'''

# intput
jo = 'allennairbi' 
stone = 'ali'
# 計算jo裡頭有對中stone中的其中一個元素的數量
# jo有 2個a, 2個l, 1個i -> 加起來得到數量為 5

# 遇到難題時 回歸原點 重新建構
# 先歸納運作流程, Ex: 先用a來比對xyz..., 得到ww, 再用 b ...
# 平鋪直敘地寫成程式，規劃迴圈
# 先完成一版可執行出預期結果的程式
# 最後再進行優化，改寫

# Solution

def jss(jo,stone):
  n= sum([s in stone for s in jo ])
  return n

print(jss(jo,stone))