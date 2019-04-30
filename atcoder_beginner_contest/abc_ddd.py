def execute(A):
    ac = len(set(A))
    aset = set(A)
    if len(aset) == 1:
        return 1
    if len(aset) == 2:
        return 2
    result = 1000000
    for i, a in enumerate(A):
        # 探索済みの島は除外
        A_dash = A[i:]
        # 必要な島の数以下になったらbreak
        if len(A_dash) < ac:
            break
        # 必要な島が含まれなくなったらbreak
        is_all_loc = [aseti in A_dash for aseti in aset]
        if False in is_all_loc:
            break
        days = 0
        # すべての島に行くための最長を計算
        for aseti in aset:
            if days < A_dash.index(aseti):
                days = A_dash.index(aseti)
        if days < result:
            result = days
    return result + 1










if __name__ == '__main__':
    print(execute(input()))
