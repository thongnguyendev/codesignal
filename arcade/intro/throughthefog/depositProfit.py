import math


def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(threshold / deposit, (1 + rate / 100)))


def depositProfit2(deposit, rate, threshold):
    year = 0
    while threshold > deposit:
        threshold = threshold / (1 + rate / 100)
        year = year + 1
    return year

#        threshold
# ------------------------  <= deposit
# (1 + rate / 100) ^ year
#
# ===> (1 + rate / 100) ^ year >= threshold / deposit
# ===> year >= log(threshold / deposit, (1 + rate / 100))
#
