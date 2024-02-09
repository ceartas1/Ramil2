class chair:
    def __init__(self, legs, saddle, material):
        self.legs = legs 
        self.saddle = saddle
        self.material = material

    def __str__(self):    
        return f"Chair (legs: {self.legs}, sadlle: {self.saddle}, material: {self.material}) "
    def __repr__(self):
        return f"Chair (legs: {self.legs}, sadlle: {self.saddle}, material: {self.material}) "
stul = chair(4, "big", "plastick")

print(*[stul])