def get_expected_val(curr_val, n, t):
    if n <= 0:
        return curr_val
    
    big_w = get_expected_val(curr_val*2, n - 1, t)
    # a * big_w > curr_val

    prob_minimale = curr_val / big_w
    longeur = 1 - t  



    if prob_minimale <= t:
        return big_w

    return ((1 - prob_minimale) / longeur)*big_w + (1 - ((1 - prob_minimale) / longeur))*curr_val


while True:
    n, t = list(map(float, input().split()))
    if n == 0:
        break

    print(get_expected_val(1, n, t))
