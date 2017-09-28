
#Currency Converter
#Scripted by: Syed Maisam Ali Jafri
#Description: Converts USD to Bitcoin and vice versa according to data on Monday September 4th @ 5:20PM

# 1 USD = 0.00022 BTC
# 1 BTC = 4528.99 USD
# USD to BTC = variable_USD * .00022
# BTC to USD = variable_BTC * 4528.99


def CC():
    # 1)figure out what user wants to convert I) USD to BTC or II) BTC to USD
    # 2)store answer in a variable
    user_choices = input("Which option do you want to use? \n1) USD -> BTC \n2) BTC -> USD \n")
    # 3)check and see what the user typed
    # 4)if user types 2  - do something
        # ask user how much BTC they want to convert and store in variable
    if user_choices == "2":
        print("BTC -> USD")
        user_btc = float(input ("Enter the amount in BTC you would like to convert \n"))
        btc = user_btc * 4528.99
        print (user_btc, "BTC", "= ", "$ %0.2f" %btc)
    # 5)if user types 1 - do something else
        # ask user how much USD they want to convert and store in variable
    elif user_choices == "1":
        print("USD -> BTC")
        user_usd = float(input ("Enter the amount in USD you would like to convert \n"))
        usd = user_usd * 0.00022
        print ("$ %0.2f" %user_usd, "= ", usd, "BTC")
    # 6)if user types else - error report
    else:
        print("Error, choose option 1 or 2")
    # 7)output value to user with units

CC()








