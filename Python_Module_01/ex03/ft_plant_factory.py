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
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower= Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 150)
    print("=== Plant Factory Output ===")
    Plants = [rose, oak, cactus, sunflower, fern]
    for i in Plants:
         print(i.show())

if __name__ == "__main__":
    main()
    
