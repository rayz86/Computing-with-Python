w=float(input("weight:"))
c=input("(K)g or (L)bs?")

if c.lower()=="k":
    print("weight in lbs:", w*2.205)

elif c.lower()=="l":
    print("weight in kgs:", w/2.205)

else:
    print("invalid input")

print('thanks')