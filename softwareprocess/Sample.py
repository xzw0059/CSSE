import math
class Sample(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "Sample.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    def getN(self):
        return self.n

    
    def p(self, t=None, tails=1):
        functionName = "Sample.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")
        
        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")
        
        constant = self.calculateConstant(self.n)
        integration = self.integrate(0.0,t, self.n, self.f)
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")
        
        return result
        
# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result

    def number1(self,s,n,highBound,w):
        #sum= float(n)
        sum = 0.0
        for i in range(s + 1):
            if i == 0:
                sum += self.f(0.0, n)
            elif i == s:
                sum += self.f(highBound, n)
            elif i != s and i != 0 and (i % 2) == 1:
                sum += 4 * self.f(w * i, n)
            elif i != s and i != 0 and (i % 2) == 0:
                sum += 2 * self.f(w * i, n)

        return sum




    def integrate(self, lowBound , highBound, n, f):
        lowBound = 0.0
        epsilon = 0.001
        simpsonOld = 0.0
        simpsonNew = epsilon
        s = 16

        while abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon:

            simpsonOld = simpsonNew
            w = (highBound - 0.0) / s
            simpsonNew = (w / 3) * self.number1(s,n,highBound,w)

        return simpsonNew
        
        
    
        
            
        
