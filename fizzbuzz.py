n=input("enter a number")
n=int(n)
if(n%3==0 and n%5==0):
    print("fizz buzz")

else:
    if(n%5==0):
        print("buzz")
    else:
        if(n%3==0):
            print("fizz")
        else:
            print(n)

