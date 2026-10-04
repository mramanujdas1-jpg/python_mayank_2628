def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]  
    max_profit = 0          
    for price in prices[1:]: 
        profit_today = price - min_price
        max_profit = max(max_profit, profit_today)

        
        min_price = min(min_price, price)

    return max_profit
test_A = [7, 1, 5, 3, 6, 4]
test_B = [7, 6, 4, 3, 1]
test_C = [2, 4, 1]

print("Test A:", max_profit(test_A))  
print("Test B:", max_profit(test_B))  
print("Test C:", max_profit(test_C))