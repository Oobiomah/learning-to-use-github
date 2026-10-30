def analyze_sales(prices):
    total = 0
    count = 0

    for price in prices:
        total += price
        count += 1

    average_price = round((total/count), 2)

    sorted_prices = sorted(prices, reverse=True)

    highest = sorted_prices[0]

    lowest = sorted_prices[-1]

    return {
        "total": total,
        "average": average_price,
        "highest": highest,
        "lowest": lowest
    }

python_prices = [500, 1200, 300, 4500, 1200]
print(analyze_sales(python_prices))