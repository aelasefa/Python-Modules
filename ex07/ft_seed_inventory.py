def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print (seed_type.capitalize(), "seeds:", quantity,"packets available")
    elif unit == "grams":
        print (seed_type.capitalize(), "seeds:", quantity,"grams total")
    elif unit == "area":
        print (seed_type.capitalize(), "seeds:  covers", quantity,"square meters")
    else:
        print("Unknown unit type")
    

def main():
    seed_type = str(input("seed_type: "))
    quantity = int(input("quantity: "))
    unit = str(input("unit: "))
    ft_seed_inventory(seed_type,quantity,unit)

if __name__ == "__main__":
    main()