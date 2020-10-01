class Annuitätentilgung:
    def __init__ (self, k_o, p, n):
        self.k_o = k_o
        self.p = p 
        self.n = n 
        self.q = 1+p/100
        self.a = (self.k_o * self.q**self.n * (self.q-1) / ( self.q ** self.n - 1))
        self.t_1 = (self.k_o * (self.q-1)) / (self.q**self.n -1)
        
    def zinsd(self):
        self.q = 1 + self.p/100
        ls = []
        for v in range (1,self.n+1,1):
            z_v = (self.k_o * (self.q-1) * (self.q**self.n - self.q**(v-1))) / (self.q**self.n -1)
            ls.append(z_v)
        return ls

    def annui(self):
        ls_t = []
        for v in range (1,self.n,1):
            self.t_v = self.t_1 * self.q**(v-1)
            ls_t.append(self.t_v)
        
        return ls_t
        
    def restz(self):
        ls_r = []
        for v in range (1,self.n,1):
            self.k_v = self.k_o * self.q**v - (self.a * (self.q**v -1)) / (self.q-1)
            ls_r.append(self.k_v)
        return ls_r

    def show_matrix(self):
        x1 = ann.restz()
        x2 = ann.zinsd()
        x3 = ann.annui()
        
    

ann = Annuitätentilgung(40000, 10, 4)
ann.show_matrix()



'''
print(zinsd(40000, 10, 4))
print(annui(40000, 10, 4))
print(restz(40000, 10, 4))
'''

