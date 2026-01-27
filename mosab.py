price1 = 125
price2 = 150
price3 = 200
totalcost = price1 + price2 + price3
print("item 1 price is ", price1)
print("item 2 price is ", price2)
print("item 3 price is ", price3)
 
budget = int(input("inter your budget: "))
item = int(input("whitch item do you want 1,2 or 3 \n if you want all items enter 4: "))
if item == 1:
    if budget > price1:
        print("you will have ",budget - price1 )
    if budget < price1:
        print("you will need ",price1 -budget, "to buy item 1" )
    if budget == price1:
        print("you have just enough to buy item 1")
if item == 2:
    if budget > price2:
        print("you will have ",budget - price2 )
    if budget < price2:
        print("you will need ",price2 -budget, "to buy item 2" )    
    if budget == price2:
        print("you have just enough to buy item 2")
if item == 3:
    if budget > price3:
        print("you will have ",budget - price3 )
    if budget < price3:
        print("you will need ",price3 -budget, "to buy item 3" )
    if budget == price3:
        print("you have just enough to buy item 3")
if item == 4:
    if budget > totalcost:
        print("you will have ",budget - totalcost )
    if budget < totalcost:
        print("you will need ",totalcost -budget, "to buy all items" )
    if budget == totalcost:
        print("you have just enough to buy all items")