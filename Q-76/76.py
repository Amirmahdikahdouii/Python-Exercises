# Buy-Sell Stock
def get_data(numbers: list):
    data = {}
    high = 0
    for i in range(len(numbers) - 1):
        difference = (numbers[i] - numbers[i+1]) * -1
        if difference in data.keys():
            data[difference] = [data[difference], [numbers[i], numbers[i+1]]]
        else:
            data.update({difference: [numbers[i], numbers[i+1]]})
        if difference > high:
            high = difference
    return {"high_profit": high, "months": data[high] if high > 0 else []}

numbers = list(map(int, input().split()))
print(get_data(numbers))