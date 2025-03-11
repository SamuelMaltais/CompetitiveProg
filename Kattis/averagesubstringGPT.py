import math

def F(s, d):
    """Count the number of substrings of s in which every digit is <= d."""
    total = 0
    current_length = 0
    for ch in s:
        if int(ch) <= d:
            current_length += 1
        else:
            total += current_length * (current_length + 1) // 2
            current_length = 0
    total += current_length * (current_length + 1) // 2
    return total

def main():
    s = input().strip()
    n = len(s)
    total_substrings = n * (n + 1) // 2

    sum_value = 0
    F_prev = 0  # F(d-1), starts with F(-1)=0
    for d in range(10):
        F_d = F(s, d)
        count_d = F_d - F_prev  # substrings with maximum exactly d
        sum_value += d * count_d
        F_prev = F_d

    # Now, average = sum_value / total_substrings.
    # We want to output it in lowest terms, either as an integer,
    # a proper fraction, or as a mixed fraction.
    num = sum_value
    den = total_substrings

    whole = num // den
    rem = num % den

    if rem == 0:
        print(whole)
    else:
        g = math.gcd(rem, den)
        rem //= g
        den //= g
        if whole > 0:
            print(f"{whole} {rem}/{den}")
        else:
            print(f"{rem}/{den}")

if __name__ == '__main__':
    main()
