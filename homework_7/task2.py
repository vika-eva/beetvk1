stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

prices_1 = {
    "total price banana": stock["banana"] * prices["banana"],
    "total price apple": stock["apple"] * prices["apple"],
    "total price orange": stock["orange"] * prices["orange"],
    "total price pear": stock["pear"] * prices["pear"]
}
print(prices_1)
