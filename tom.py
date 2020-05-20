total_price = 0
reg_price = 3.70
extra_price = 3.90
premium_price = 4.10
reg_gals = 0
extra_gals = 0
premium_gals = 0


def fill():
    global total_price, reg_price, extra_price, premium_price, premium_gals, reg_gals, extra_gals
    print("Prices: Regular: Extra: Premium")
    print("$Per Gallon: " + str(reg_price) + " : " +
          str(extra_price) + " : " + str(premium_price))
    gas_type = input("Choose 1.Regular 2.Extra or 3.Premium  1/2/3>>> ")
    if gas_type == "1":
        print("Your selection: Regular " + str(reg_price) + "$per gallon")
        gas_prince = reg_price
    if gas_type == "3":
        print("Your selection: Extra " + str(extra_price) + "$per gallon")
        gas_prince = extra_price
    if gas_type == "3":
        print("Your selection: Premium " + str(premium_price) + "$per gallon")
        gas_prince = premium_price
    gtf = float(input("Enter how many gallons to fill...>"))
    print("Price: %.2f" % (gtf * gas_prince))
    if gas_prince == reg_price:
        reg_gals += gtf
    if gas_prince == extra_price:
        extra_gals += gtf
    if gas_prince == premium_gals:
        premium_gals += gtf

    total_price += gtf * gas_prince


def sales():
    print("Gallons sold: Regular: Extra: Premium")
    print("Total " + str(reg_gals) + " " +
          str(extra_gals) + " " + str(premium_gals))
    print("Total sales " + str(total_price))


def prices():
    global reg_price, extra_price, premium_price
    print("Prices: Regular: Extra: Premium")
    print("$Per Gallon: " + str(reg_price) + " : " +
          str(extra_price) + " : " + str(premium_price))
    print("For each grade, when prompted, enter new price, or hit Return if price stays same")
    new_reg = input("Enter new price for Regular: >>>")
    new_xtra = input("Enter new price for xtra: >>>")
    new_pre = input("Enter new price for pre: >>>")
    confirm = input("Enter 1 to confirm change of prices, 0 to cancel ")
    if confirm == "1":
        if new_reg:
            reg_price = new_reg
        if new_xtra:
            extra_price = new_xtra
        if new_pre:
            premium_price = new_pre


def end_of_day():
    global total_price, premium_gals, reg_gals, extra_gals
    sales()
    reset = input("Reset the logs (Y/N)? ")
    if reset == "Y":
        total_price = premium_gals = reg_gals = extra_gals = 0


quit = False
while not quit:
    print('1.Fill 2.Sales 3.Prices 4.End of Day 5.Exit')
    choice = int(input('Enter choice:  '))
    if choice == 1:
        fill()
    elif choice == 2:
        sales()
    elif choice == 3:
        prices()
    elif choice == 4:
        end_of_day()
    elif choice == 5:
        quit = True
    else:
        print('Invalid Choice!')
