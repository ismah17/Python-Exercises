a=12
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

for i in range(1,3):
    print("result,",i)

##for i in range(1,a/b):
##    print(i)
##

for i in range(1,a//b):
    print(i)


#### Exercise Solution###
###bun price 2.40
### money 15
### requiremnets
#inform customer how many buns he gets
#he knows if there's remainder money
### methods###
#ask how much money, then do integer division
# #print the result #multiply integer division with unit price
# #print him the cost #substract with total money
#print him remainder money

Recieved_money= float(input(print("Enter how much money you have")))
print("You said", Recieved_money)

bun_price=2.40
number_of_buns= Recieved_money// bun_price

if number_of_buns > 0:
    print("great! You will recieve" , number_of_buns , "buns")
else:
    print("Sorry, come back again!")
    Redundant=bun_price-Recieved_money
    print("If you can give", Redundant, "You can get one bun")

total_price= bun_price* number_of_buns
print("Your total cost is", total_price)
remainder= Recieved_money - total_price
if Recieved_money >= bun_price:
    print("You have" , remainder, "as change from us")3