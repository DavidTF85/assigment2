#1
idef C_to_F(c):
    f = (c * 9/5) + 32
    # convertion formula is:T(°F) = T(°C) × 9/5 + 32
    #check here URL: https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
    return f


#2
def K_2_C(c):
    # kalving formula = T(K) = T(°C) + 273.15
    #check here URL: https://www.rapidtables.com/convert/temperature/
    k = c+273.5
    return k

#3
def F_2_C(f):
    c = (f-32) *5/9
    return c

#4
def F_2_K(f):
    k = (f + 459.67) * 5/9
    return k
#5
def k_2_c(k):
    c = k - 273.15
    return c

#6
def k_2_f(k):
    c = (k * 9/5) - 459.67
    return c
