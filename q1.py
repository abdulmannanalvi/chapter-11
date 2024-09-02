class Two_D_Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def Show(self):
        print(f"The Vector is {self.i}i + {self.j}j")
    
class Three_D_Vector(Two_D_Vector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k
    def Show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a=Two_D_Vector(1,2)
a.Show()
b=Three_D_Vector(2,4,3)
b.Show()