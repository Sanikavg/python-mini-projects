package=int(input("enter the number of packages: "))
if package>=10 and package<=19:
    print("there is a discount of 10%")
    amount=package*99
    value=amount-(10/100*(amount))
    print("the totat amount after the purchase",value,"$")
elif package>=20 and package<=49:
    print("there is a discount of 20%")
    amount=package*99
    value=amount-(20/100*(amount))
    print("the totat amount after the purchase",value,"$")
elif package>=50 and package<=99:
    print("there is a discount of 30%")
    amount=package*99
    value=amount-(30/100*(amount))
    print("the totat amount after the purchase",value,"$")
elif package>=100:
    print("there is a discount of 40%")
    amount=package*99
    value=amount-(40/100*(amount))
    print("the totat amount after the purchase",value,"$")
else:
    print("there is no discount")
