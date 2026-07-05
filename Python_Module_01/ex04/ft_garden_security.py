class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}: {round(self._height)}cm, {self._age} days old")

    def get_height(self):
        return self._height
    
    def get_age(self):
         return self._age
    
    def set_height(self, height):
        if height > 0:
            self._height = height
            print(f"Height updated: {round(self._height, 2)}cm")
        else:
            print(f"{self.name}:Error, height can't be negative")
            print("Height update rejected")
    
    def set_age(self, age):
        if age > 0:
            self._age = age
            print(f"Age updated: {self._age}days")
        else:
            print(f"{self.name}:Error, age can't be negative")
            print("Age update rejected")

    def show(self):
            return f"Current state: {self.name}: {round(self._height, 2)} cm, {self._age} Days old"
def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 25, 30)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-1)
    rose.set_age(-10)
    print(rose.show())
    # print(getattr(rose,'show')())

if __name__ == "__main__":
    main()
    

