'''
You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.
'''


def depositProfit(deposit, rate, threshold):
    counter = 0
    while deposit < threshold:
        money = deposit * (rate/100)
        deposit += money
        counter += 1
    return counter


deposit = 100
rate = 20
threshold = 170

print(depositProfit(deposit, rate, threshold))
