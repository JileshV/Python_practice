class TwoDVector:  
    def __init__(self, u, v):
        self.u = u
        self.v = v        

class ThreeDVector(TwoDVector):
    def __init__(self, u, v, w):
        super().__init__(u, v)
        self.w = w

V1 = TwoDVector(5, 10)
V2 = ThreeDVector(6, 12, 18)

print(V1.u, V1.v)
print(V2.u, V2.v, V2.w)