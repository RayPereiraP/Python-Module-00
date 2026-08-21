def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed_type = seed_type.capitalize()
    match unit:
        case "packets":
            string = f"{seed_type} seeds: {quantity} packets available"
        case "grams":
            string = f"{seed_type} seeds: {quantity} grams total"
        case "area"
            string = f"{seed_type} seeds: covers {quantity} square meters"
        case _:
            string = "Unknown unit type"
        print(string)