def calculate_pizza_slices(individuals):
    slices_large = 8
    slices_medium = 6
    slices_regular = 4
    slices_small = 1

    large_pizzas = individuals // slices_large
    medium_pizzas = 0
    regular_pizzas = (individuals % slices_large) // slices_regular
    small_pizzas = 0

    print(f"If there are {individuals} individuals:")
    print(f"1. we will have {large_pizzas} Large pizza")
    print(f"2. we will have {large_pizzas} Large pizza")
    print(f"3. we will have {large_pizzas} Large pizza")
    print(f"4. we will have {large_pizzas} Large pizza")

    total_slices = (large_pizzas * slices_large) + (medium_pizzas * slices_medium) + (regular_pizzas * slices_regular) + (small_pizzas * slices_small)
    print(f"\nTotal slices: {total_slices}")
    print(f"((large_pizzas * slices_large)+(medium_pizzas * slices_medium)+(regular_pizzas * slices_regular)+(small_pizzas * slices_small)):{total_slices}")
