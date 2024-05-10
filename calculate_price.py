def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def calculate_price(prices, discount):
    sorted_prices = bubble_sort(prices)
    total = 0.0
    i, j = 0, len(sorted_prices) - 1

    while j - i >= 2:
        total += sorted_prices[i]
        total += sorted_prices[i + 1]
        total += sorted_prices[j] * (1 - discount / 100.0)

        i += 2
        j -= 1

    if j - i <= 3:
        total += sum(sorted_prices[i:j+1])

    return total

print(calculate_price([50, 20, 30, 17, 100],10))