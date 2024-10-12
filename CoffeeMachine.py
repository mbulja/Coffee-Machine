MENU={
  "espresso":{
      "milk":0,
      "water":50,
      "coffee":18,
      "cost":1.5
  },
  "latte":{
      "milk":150,
      "water":200,
      "coffee":24,
      "cost":2.5
  },
"cappuccino":{
      "milk":100,
      "water":250,
      "coffee":24,
      "cost":3
  }

}
zalihe={
     "milk":700,
     "water":1000,
     "coffee":200,
     "money":0


 }
flag1=True


while flag1==True:

    flag=True

    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="espresso":

        if zalihe["milk"]<0:
            print("Sorry there is not enough milk.")
            flag=False


        if zalihe["water"] < 50:
            print("Sorry there is not enough water.")
            flag=False

        if zalihe["coffee"] < 18:
            print("Sorry there is not enough coffee.")
            flag=False

        if flag==True:
             zalihe["milk"]= zalihe["milk"] - MENU["espresso"]["milk"]
             zalihe["water"] = zalihe["water"] - MENU["espresso"]["water"]
             zalihe["coffee"] = zalihe["coffee"] - MENU["espresso"]["coffee"]





    elif choice=="latte":
        if zalihe["milk"] <150:
            print("Sorry there is not enough milk.")
            flag = False

        if zalihe["water"] < 200:
            print("Sorry there is not enough water.")
            flag = False

        if zalihe["coffee"] < 24:
            print("Sorry there is not enough coffee.")
            flag = False

        if flag == True:
            zalihe["milk"] = zalihe["milk"] - MENU["latte"]["milk"]
            zalihe["water"] = zalihe["water"] - MENU["latte"]["water"]
            zalihe["coffee"] = zalihe["coffee"] - MENU["latte"]["coffee"]





    elif choice=="cappuccino":
        if zalihe["milk"] < 100:
            print("Sorry there is not enough milk.")
            flag = False

        if zalihe["water"] < 250:
            print("Sorry there is not enough water.")
            flag = False

        if zalihe["coffee"] < 24:
            print("Sorry there is not enough coffee.")
            flag = False

        if flag == True:
            zalihe["milk"]= zalihe["milk"] - MENU["cappuccino"]["milk"]
            zalihe["water"] = zalihe["water"] - MENU["cappuccino"]["water"]
            zalihe["coffee"] = zalihe["coffee"] - MENU["cappuccino"]["coffee"]



    elif choice=="report":
        print(f'milk: {zalihe["milk"]}ml, water: {zalihe["water"]}ml, coffee: {zalihe["coffee"]}g, money=${zalihe["money"]}')
        flag=False


    elif choice=="off":
        flag1=False
        flag=False



    else:
        print("Wrong input, try again!")
        flag=False

    if flag==True:
        print("Please insert the coins.")
        quarters=int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money=pennies*0.01+nickles*0.05+dimes*0.1+quarters*0.25
        if choice=="espresso":
            if money<1.5:
                print("Sorry that's not enough money. Money refunded.")
            else:

                zalihe["money"]=zalihe["money"]+1.5
                print(f'Here is ${money - 1.5} in change')


        if choice=="latte":
            if money<2.5:
                print("Sorry that's not enough money. Money refunded.")
            else:
                zalihe["money"]=zalihe["money"]+2.5
                print(f'Here is ${money - 2.5} in change')


        if choice=="cappuccino":
                 if money<3:
                    print("Sorry that's not enough money. Money refunded.")
                 else:
                    zalihe["money"]=zalihe["money"]+3
                    print(f'Here is ${money-3} in change')





