def ft_plant_age():
    PlantAge = int(input("Enter plant age in days:"))
    if PlantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
        
def main():
    ft_plant_age()

if __name__ == "__main__":
    main()