

from datetime import datetime

name=(input("enter your name:"))
#list of items
list='''
Rice         USD 5/lb
oil          USD 6/lb
salt         USD 1/lb
sugar        USD 2/lb
cashew       USD 6/lb
cherries     USD 4/lb
idli batter  USD 3/lb
chicken      USD 10/lb
beef         USD 12/lb
fish         USD 15/lb
'''

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates of items
items={'Rice':5,'oil':6,'salt':1,'sugar':2,'cashew':6
,'cherries':4,'idli batter':3,'chicken':10,
'beef':12,'fish':15}

option=int(input('press 1 to diplay the list of items:'))
if option!=1:
    print("Sellect the valid option")
else:
    print(list)
for i in range(len(items)):
    inp1=int(input('press 1 to buy or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items: ')
        quantity=int(input('enter the quantity: '))
        if item in items.keys():
            price=quantity*(items[item]) 
            pricelist.append((item,items,quantity,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("Sorry! The item you've entered is not available")
    else:
        print("Sorry! You've entered a wrong number")
    inp=input("Press yes for billing or no for exit:")
    if inp=='yes':
        pass
        if finalprice!=0:
            print(27*"=","Walmart supercenter",27*"=")
            print(28*"=","Houston,Texas",28*"=")
            print("name:",name,18*" ","Date",datetime.now())
            print(75*"-")
            print("sno",5*" ",'items',8*" ",'quantity',12*" ",'price')

            for i in range(len(pricelist)):
                print(i+1,8*" ",ilist[i],10*" ",qlist[i],18*" ",plist[i])
            print(75*"-")
            print(50*" ","totalprice:",'USD',float(totalprice))
            print(50*" ","gst:",6*" ",'USD', gst)
            print(75*"-")
            print(50*" ",'finalprice:','USD',finalprice)
            print(75*"-")
            print(27*"-","Thanks for visiting",27*"-")

