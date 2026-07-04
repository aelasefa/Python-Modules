class Plant:
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = Height
        self.Age = Age
    def age(self):
         self.Age += 1
         return self.Age
    def grow(self):
        self.Height += 0.8
        return self.Height
    def show(self):
            return f"{self.name}: {round(self.Height, 2)} cm, {self.Age} Days old"
def main():
    print("=== Garden Plant Growth ===")
    Plan1 = Plant("Rose", 25, 30)
    initHeight = Plan1.Height
    for i in range(8):
        if i == 0:
            print(getattr(Plan1,'show')())
        else :
            print(f"=== Day {i} ===")
            Plan1.grow()
            Plan1.age()
            print(getattr(Plan1,'show')())
    print(f"Growth this week: {round(Plan1.Height - initHeight, 2)} cm")

if __name__ == "__main__":
    main()
    
