
if __name__ == '__main__':
    print('Tack1:')
    string = input('Enter string:')
    str = string.split(' ')
    print(str)
    my_dict = {}
    for i in str:
        my_dict[i] = str.count(i)
    print(my_dict)

    print('tack2:')
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
    dict_sum = {}
    for i, j in zip(stock, prices):
        dict_sum.update({i: stock[i] + prices[j]})
    print(dict_sum)

    print('Tack3:')
    tup_list = []
    for i in range(1, 10):
        tup_list.append((i, i ** 2))
    print(tup_list)