def ft_harvest_total():
    First_Day = int(input("Day 1 harvest:"))
    Second_Day =  int(input("Day 2 harvest:"))
    Third_Day = int(input("Day 3 harvest:"))
    Total = First_Day + Second_Day + Third_Day
    print("Total harvest:", Total)
def main():
    ft_harvest_total()
if __name__ == "__main__":
    main()