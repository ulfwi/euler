import math

P = lambda n: int(n*(3*n-1)/2)

D = lambda P_k, P_j: abs(P_k - P_j)

def is_pentagonal(n):

    root_pos = 1/6 + math.sqrt(1 + 24*n) / 6
    if root_pos == int(root_pos):
        return True

    root_neg = 1/6 - math.sqrt(1 + 24*n) / 6
    if root_neg == int(root_neg) and root_neg > 0:
        return True

    return False

def get_pentagonal():
    n = 0
    while True:
        n += 1
        print(n)
        yield P(n)

min_diff = 100000000
current_diff = 0
gen = get_pentagonal()
pent_list = [next(gen)]
not_found = True
while min_diff > current_diff and not_found:
    nbr = next(gen)
    pent_list += [nbr]
    for el in pent_list[:-1]:
        diff = nbr - el
        summ = nbr + el
        if is_pentagonal(diff) and is_pentagonal(summ):
            print(diff)
            if diff < min_diff:
                min_diff = diff
                print(min_diff)
                not_found = False

    current_diff = pent_list[-1] - pent_list[-2]

print(min_diff)

print(is_pentagonal(P(2167)))
print(is_pentagonal(P(1020)))
print(is_pentagonal(P(2167 - 1020)))
print(is_pentagonal(P(2167 + 1020)))

print(P(2167))

a = get_pentagonal()
print(next(a))
print(next(a))
print(next(a))
