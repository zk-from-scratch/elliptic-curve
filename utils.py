# Extended euclidean algorithm to find modular inverses for
# integers
def find_modular_inverse(val, field_modulus):
    if val == 0:
        return 0
    lm, hm = 1, 0
    low, high = val % field_modulus, field_modulus
    while low > 1:
        r = high // low
        nm, new = hm - lm * r, high - low * r
        lm, low, hm, high = nm, new, lm, low
    return lm % field_modulus
