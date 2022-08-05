class Kasr():
    def __init__(self,S,M):
        self.Sorat=S
        self.Makhraj=M
    def Sum(self,x):
        Result=Kasr(None,None)
        Result.Sorat=self.Sorat*x.Makhraj+x.Sorat*self.Makhraj
        Result.Makhraj=self.Makhraj*x.Makhraj
        return Result
    def Mul(self,x):
        Result=Kasr(None,None)
        Result.Sorat=self.Sorat*x.Sorat
        Result.Makhraj=self.Makhraj*x.Makhraj
        return Result
    def Subtract(self,x):
        Result=Kasr(None,None)
        Result.Sorat=self.Sorat*x.Makhraj-x.Sorat*self.Makhraj
        Result.Makhraj=self.Makhraj*x.Makhraj
        return Result
    def Division(self,x):
        Result=Kasr(None,None)
        Result.Sorat=self.Sorat*x.Makhraj
        Result.Makhraj=self.Makhraj*x.Sorat
        return Result
    def Show(self):
        print(self.Sorat,'/',self.Makhraj)
A = Kasr(3,5)
B = Kasr(4,5)
A.Show()
B.Show()
C=A.Mul(B)#farghi nadare B.Mul(A)
print("Multiplicative: ",end='')
C.Show()
print("Division: ",end='')
C=A.Division(B)
C.Show()
print("Sum: ",end='')
C=A.Sum(B)
C.Show()
print("Subtract: ",end='')
C=A.Subtract(B)
C.Show()