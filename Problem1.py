"""Find the number of rounds until 1 coin remains"""


def round(coins):
    if coins < 1:
        return None
    if coins == 1:
        return 1
    n = round(coins // 2) + 1
    return n


no_coin = int(input())
print("It took {0} rounds to change coins into 1".format(round(no_coin)))
