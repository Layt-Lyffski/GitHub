class Annuitätentilgung:
    def __init__ (self, k_o, p, n):
        self.k_o = k_o
        self.p = p 
        self.n = n 
        self.q = 1+p/100
        self.a = round(self.k_o * self.q**self.n * (self.q-1) / ( self.q ** self.n - 1), 2)
        self.t_1 = round((self.k_o * (self.q-1)) / (self.q**self.n -1), 2)
        
    def zinsd(self):
        ls = []
        for v in range (1,self.n+1,1):
            z_v = (self.k_o * (self.q-1) * (self.q**self.n - self.q**(v-1))) / (self.q**self.n -1)
            ls.append(z_v)
        return ls

    def annui(self):
        ls = []
        for v in range (1,self.n+1,1):
            self.t_v = self.t_1 * self.q**(v-1)
            ls.append(self.t_v)
        return ls
        
    def restz(self):
        ls = []
        for v in range (1,self.n,1):
            self.k_v = self.k_o * self.q**v - (self.a * (self.q**v -1)) / (self.q-1)
            ls.append(self.k_v)
        return ls

    def show_matrix(self):
        x1 = ann.annui()
        x2 = ann.zinsd()
        x3 = ann.restz()
        print(x1)
        print(x2)
        print(x3)
        print(self.a)

ann = Annuitätentilgung(75000, 4.5, 5)
ann.show_matrix()

