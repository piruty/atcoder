def execute(A):
    # 両端のどちらかが最小
    if A[0] == min(A) or A[-1] == min(A):
        return abs(max(A) - min(A))

    # 左右両方にmax Aが含まれるようになったら計算しなくて良い
    max_a = max(A)
    i_max_a = [i for i, a in enumerate(A) if a == max_a]
    max_i = len(A)
    if len(i_max_a) > 1:
        if i_max_a[0] < len(A) - i_max_a[-1]:
            # 左側から先に最大数が来る
            max_i = i_max_a[0] + 1
        else:
            # 右側から先に最大数が来る
            max_i = i_max_a[-1] + 1
    m = 0
    for i in range(max_i - 1):
        # from left
        mt = abs(max(set(A[:i + 1])) - max(set(A[i + 1:])))
        if m < mt:
            m = mt
        # from right
        mt = abs(max(set(A[:- i - 1])) - max(set(A[- i:])))
        if m < mt:
            m = mt
    return m


if __name__ == '__main__':
    print(execute(input()))
