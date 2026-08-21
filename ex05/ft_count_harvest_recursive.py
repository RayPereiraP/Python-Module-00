def ft_count_harvest_recursive(old_val=None):
    if old_val == 0:
        return 
    if (old_val is None):
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(old_val - 1)
        print(f"Day {old_val}")