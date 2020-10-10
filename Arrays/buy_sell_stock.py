# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_stock_once(prices):
    max_profit = 0
    for buy_idx, buy_price in enumerate(prices):
        for sell_idx, sell_price in enumerate(prices[buy_idx:]):
            max_profit = sell_price - buy_price if (sell_price - buy_price) > max_profit else max_profit
    return max_profit


# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


A = [310, 315, 275, 295, 260, 270, 290, 230, 255]

print(buy_and_sell_once(A))

print(buy_and_sell_stock_once(A))
