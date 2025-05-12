def _init_(self,nm,strt,cit,sta):

  

self.name=nm

self.street=strt

self.city=cit

self.state=sta

''' we have the product as a class defined with

attributesss as given below..'''

class product:

  

def _init_(self,name,prc):

  

self.product_name=name

self.price=prc

  

'''orderLine has product quantity and total as given below..'''

class orderLine:

  

def _init_(self,p_name,prc,qty):

  

self.product=product(p_name,prc)

self.quantity=qty

self.total=(self.product.price)*(self.quantity)

  

''' we have the class order as order_NO name1 street1 and city1 as given below we pass and declare here

instance of various above class to implement composition

'''

class order:

  

def _init_(self,order_NO,name1,street1,city1,state1,name2,street2,city2,state2):

  

self.order_NO=order_NO

self.OrderLine=[]

self.order_total=0

print("enter the no. of products")

self.n=int(input())

  

for i in range(self.n):

  

print("enter the product line info like product name,price,quantity")

p_name=input()

prc=float(input())

qty=int(input())

self.OrderLine.append(orderLine(p_name,prc,qty))

  

self.ship_to_address=address(name1,street1,city1,state1)

self.bill_to_address=address(name2,street2,city2,state2)

  

  

for i in range(self.n):

self.order_total+=self.OrderLine[i].total

  

  

#finlly we have functon to print all the detail.s

def print_orders(self):

print("Order No: "+str(self.order_NO)+" order Total: "+str(self.order_total))

print("product Name "+"quantity "+"unit price "+" Total ")

  

for i in range(self.n):

print(self.OrderLine[i].product.product_name +" "+str(self.OrderLine[i].quantity)+" "+str(self.OrderLine[i].product.price)+" "+str(self.OrderLine[i].total))

  

print("ship To: "+self.ship_to_address.name+","+self.ship_to_address.street+","+self.ship_to_address.city+","+self.ship_to_address.state)

print("BiLL To: "+self.bill_to_address.name+","+self.bill_to_address.street+","+self.bill_to_address.city+","+self.bill_to_address.state)

def main():

  

print("enter the order NO")

order_No=input()

  

  

print("Enter the shiping address name,street,city,state")

name1=input()

street1=input()

city1=input()

state1=input()

  

print("Enter the billing address name,street,city,state")

name2=input()

stree2=input()

city2=input()

state2=input()

#call the functons here..

Orders=order(order_No,name1,street1,city1,state1,name2,stree2,city2,state2)

Orders.print_orders()

  

  

if _name=="main_":

  

main()

  

Input:

1234

raj

st_street

houston

newyork

newton

linkin park

albania

iraq

2

lipstic

45.56

10

polo t shirt

10

20

