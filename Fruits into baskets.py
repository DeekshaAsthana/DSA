class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    window_start = 0
    res= 0
    fruit_basket = {}
    for window_end in range(len(fruits)):
        right= fruits[window_end]
        if right not in fruit_basket:
            fruit_basket[right] = 1
        else:
            fruit_basket[right] += 1
        while len(fruit_basket) > 2:
            left= fruits[window_start]
            fruit_basket[left] -= 1
            if fruit_basket[left] == 0:
                del fruit_basket[left]
            window_start += 1
        res = max(res, window_end - window_start+1)
    return res
