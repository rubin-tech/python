from datetime import date
def initial_Display():
 print("\t\t\t", "Rubin Timilsina's Billing System", "\n \t\t\t", "Kathmandu Nepal")
 print("------------------------------------------------------------------------------------")
 today = date.today()
 print(f"\t\t\t\t {today}")
def input_user():
    allPrice = []
    n = int(input("number of customer"))
    for i in range(0, n):
        print(f"Customer[{i+1}]")
        noItem = int(input(f"item[{i+1}]"))
        price = []
        for j in range(0,noItem):
            print("Item" + str(j+1)) 
            priceTemp = int(input("Enter item price : "))
            price.append(priceTemp)
        allPrice.append(price)
    print(allPrice)

input_user()