def dummy(battle_cry: str):
    x = 131
    y = 2938
    z = x**y
    battle_cry = battle_cry.upper()

    test_list = []
    for i in range(3,14,2):
        test_list.append(i)
    return x, y, z, test_list, battle_cry



def main():
    x = 'for the Mesozoic!'

    a,b,c,d,e = dummy(x)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)




if __name__ == '__main__':
    main()
