def zinsd(k_o, p, n):
    q = 1 + p/100
    ls = []
    for v in range (1,n+1,1):
        z_v = (k_o * (q-1) * (q**n - q**(v-1))) / (q**n -1)
        ls.append(z_v)
    return ls

def annui(k_o, p, n):
    ls_t = []
    q = 1 + p/100
    a = (k_o * q**n * (q-1) / ( q ** n - 1))
    t_1 = (k_o * (q-1)) / (q**n -1)
    for v in range (1,n,1):
        t_v = t_1 * q**(v-1)
        ls_t.append(t_v)
    
    return ls_t
    
def restz(k_o, p, n):
    ls_r = []
    q = 1 + p/100
    a = (k_o * q**n * (q-1) / ( q ** n - 1))
    for v in range (1,n,1):
        k_v = k_o * q**v - (a * (q**v -1)) / (q-1)
        ls_r.append(k_v)
    return ls_r
    



print(zinsd(40000, 10, 4))
print(annui(40000, 10, 4))
print(restz(40000, 10, 4))