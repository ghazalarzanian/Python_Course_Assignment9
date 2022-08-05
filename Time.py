class Time:
    def __init__(self,h,m,s):
        self.Hour=h
        self.Minute=m
        self.Second=s
    def Sum(self,x):
        result=Time(None,None,None)
        result.Second=self.Second+x.Second
        if result.Second>59:
            result.Minute=int(result.Second/60)
            result.Second=result.Second%60
        result.Minute+=self.Minute
        result.Minute+=x.Minute
        if result.Minute>59:
            result.Hour=int(result.Minute/60)
            result.Minute=result.Minute%60
        result.Hour+=self.Hour
        result.Hour+=x.Hour
        return result
    def Subtract(self,x):
        result=Time(None,None,None)
        if self.Second>=x.Second:
            result.Second=self.Second-x.Second
        else:
            self.Second+=60
            self.Minute-=1
            result.Second=self.Second-x.Second
        if self.Minute>=x.Minute:
            result.Minute=self.Minute-x.Minute
        else:
            self.Minute+=60
            self.Hour-=1
            result.Minute=self.Minute-x.Minute
        result.Hour=int(self.Hour-x.Hour)
        return result
    def SecondToClock(self,x):
        result=Time(None,None,None)
        result.Hour=int(x/3600)
        x=x-result.Hour*3600
        result.Minute=int(x/60)
        x=x-result.Minute*60
        result.Second=int(x)
        return result
    def ClockToSecond(self):
        result=int()
        result+=self.Hour*3600
        result+=self.Minute*60
        result+=self.Second
        return result
    def Show(self):
       print(self.Hour,':',self.Minute,":",self.Second)
A=Time(12,30,12)
B=Time(11,50,56)
A.Show()
B.Show()
print('Sum: ',end='')
C=A.Sum(B)
C.Show()
print('Subtract: ',end='')
C=A.Subtract(B)
C.Show()
print('ClockToSecond: ',end='')
C=A.ClockToSecond()
print(C)
print('SecondToClock: ',end='')
C=A.SecondToClock(123124)
C.Show()