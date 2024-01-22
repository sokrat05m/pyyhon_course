prices = [2, 4, 1]
lst = []
while len(prices) > 0:
    check = max(zip(prices, range(len(prices))))
    if prices.index(max(prices)) == 0:
        prices.remove(max(prices))
    else:
        lst.append(max(prices) - min(prices[:check[1]]))
        prices.remove(max(prices))
        prices.remove(min(prices[:check[1]]))
print(prices)
print(lst)