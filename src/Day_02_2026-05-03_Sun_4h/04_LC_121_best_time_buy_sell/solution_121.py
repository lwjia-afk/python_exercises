# LC 121 — Best Time to Buy and Sell Stock
def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_prof = 0
    for price in prices:
        min_price = min(min_price, price)
        max_prof = max(max_prof, price - min_price)
        
    return max_prof
    
if __name__ == "__main__": 
        print(maxProfit([7,1,5,3,6,4]))  # Output: 5
        print(maxProfit([1,2,3,4,5]))    # Output: 4
        print(maxProfit([7,6,4,3,1]))    # Output: 0
