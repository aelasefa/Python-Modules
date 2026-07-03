def ft_count(Days, i):
    print(i)
    if Days == i:
        return 1
    else:
         ft_count(Days,i + 1)
def  ft_count_harvest_recursive():
    Days = int(input("Days until harvest: "))
    i = 1
    ft_count(Days, i)
    print("Harvest time!")
def main():
        ft_count_harvest_recursive()

if __name__ == "__main__":
    main()