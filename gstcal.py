import os

def receipt(name,price,tax,gst,net):
    os.system('cls')
    print("-----------GST CALCULATOR-----------")
    print("------------------------------------")
    print("ITEM NAME: ",name)
    print("BILLING PRICE: ",price)
    print("GST %: ",tax)
    print("CGST:",gst)
    print("SGST:",gst)
    print("------------------------------------")
    print("TOTAL PRICE: ",net)
    print("------------------------------------")
    print("-------------THANK YOU--------------")


name=input("billing item: ")
price=float(input("billing price: "))
tax=float(input("enter the tax %: "))
choice=input("(+)add GST (-)subtract GST")
if(choice=='+'):
    gst=(price*tax)/100
    net=price+gst
    receipt(name,price,tax,gst,net)
else: 
    if(choice=='-'):
        gst=(price*tax)/100
        net=price-gst
        receipt(name,price,tax,gst,net)

    else:
        print("invalid input")

    
