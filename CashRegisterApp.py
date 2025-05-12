
p1 = Product("P1", 5.00)
p2 = Product("P2", 1.00)
p3 = Product("P3", 2.00)
l = [p1, p2, p3]

print("P1 price =", p1.getProductPrice())
print("totalprice with tax for p1 is", p1.getTotalPrice())
print("P2 price =", p2.getProductPrice())
print("totalprice with tax for p2 is", p2.getTotalPrice())
print("P3 price =", p3.getProductPrice())
print("totalprice with tax for p3 is", p3.getTotalPrice())


print("Grand Total the customer needs to pay is "+str(p1.getTotalPrice())+" + "+str(p2.getTotalPrice())+" + "+str(p3.getTotalPrice())+" = "+str(p1.getTotalPrice() + p2.getTotalPrice()+p3.getTotalPrice()))

