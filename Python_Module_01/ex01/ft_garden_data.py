class Plant:
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = Height
        self.Age = Age
    def show(self):
            return f"{self.name}: {self.Height} cm, {self.Age} Days old"

def main():
    print("=== Garden Plant Registry ===")
    Plan1 = Plant("Rose", 25, 30)
    Plan2 = Plant("Sunflower", 80, 45)
    Plan3 = Plant("Cactus", 15, 120)
    print(getattr(Plan1,'show')())
    print(getattr(Plan2,'show')())
    print(getattr(Plan3,'show')())

if __name__ == "__main__":
    main()
    
