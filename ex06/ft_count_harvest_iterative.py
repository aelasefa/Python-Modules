def ft_count_harvest_iterative():
    Days = int(input("Days until harvest: "))
    for i in range(0, Days):
        print(i + 1)
    print("Harvest time!")
def main():
    ft_count_harvest_iterative()
if __name__ == "__main__":
    main()