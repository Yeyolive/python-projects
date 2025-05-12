try:
    price = float(input('Enter price: '))
    quantity = int(input("Enter quantity: "))
    subTotal = price*quantity
    salesTax = subTotal*0.825
    total = subTotal + salesTax
    print("Total amount =",total)
except ArithmeticError:
    print("ArithmeticError occurred...")
except ValueError:
    print("ValueError occurred...")
except Exception:
    print("Error occurred...")
