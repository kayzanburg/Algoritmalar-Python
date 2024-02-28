# Stringin tersini bulmak için rekürsif bir fonksiyon
def ters_cevir(string):
    if len(string) <= 1:
        return string
    return ters_cevir(string[1:]) + string[0]

print(ters_cevir("Python"))

# Rekürsif olarak çarpma işlemi
def carp(x, y):
    if y == 0:
        return 0
    return carp(x, y - 1) + x

print(carp(2, 3))

# Üs alma işlemi x^y
def us_alma(a, b):
    if b == 0:
        return 1
    return carp(a, us_alma(a, b - 1))

print(us_alma(2, 3))
