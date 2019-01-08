def process(deg, dis):
    degs = [1125, 3375, 5625, 7875, 10125, 12375, 14625, 16875, 19125, 21375, 23625, 25875, 28125, 30375, 32625, 34875]
    deg_name = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    diss = [3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327]

    s = ((dis/6.0)*2+1)//2
    sn = 0
    for i, d in enumerate(diss):
        if s < d:
            break
        sn = i + 1

    n = 'N'
    dg = deg * 10
    if sn == 0:
        n = 'C'
    else:
        for i, d in enumerate(degs):
            if dg < d:
                break
            n = deg_name[(i + 1) % 16]

    return "{} {}".format(n, sn)


if __name__ == '__main__':
    deg, dis = map(int, input().split())
    print(process(deg, dis))

