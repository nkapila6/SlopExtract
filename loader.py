def txtloader(path: str) -> list:
    with open(path, "r") as file:
        lines = file.readlines()

    products, current_product = [], []

    # very ineff way to do this but oke
    for line in lines:
        # add to current
        clean_line = line.strip()
        current_product.append(clean_line)

        # end of product indicated by start of $
        if clean_line.startswith("$"):
            products.append("\n".join(current_product))
            current_product = []  # reset current

    return products


print(txtloader("input.txt")[0])
print(len(txtloader("input.txt")))
