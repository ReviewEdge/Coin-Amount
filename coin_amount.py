def start_program():
    weight = float(raw_input("Enter weight in grams:"))
    coin_type = (raw_input("Enter coin type:")).lower()
    if coin_type == "penny":
        coin_amount = int(weight / 2.5)
    elif coin_type == "nickel":
        coin_amount = int(weight / 5)
    elif coin_type == "dime":
        coin_amount = int(weight / 2.268)
    elif coin_type == "quarter":
        coin_amount = int(weight / 5.670)
    else:
        print("invalid coin")
    if coin_amount < 1:
        print "invalid weight"
    else:
        return coin_amount


print(start_program())
