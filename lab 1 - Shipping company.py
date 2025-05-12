package_weight = float(input("Enter weight of package: "))
shipping_charges = 0.0

message = "Shipping charges = "

if package_weight <= 2:
    shipping_charges = package_weight * 1.50
elif package_weight > 2 and package_weight <= 6:
    shipping_charges = package_weight * 3.00
elif package_weight > 6 and package_weight <= 10:
    shipping_charges = package_weight * 4.00
elif package_weight > 10:
    shipping_charges = package_weight * 4.75

message += "$" + format(shipping_charges, ',.2f')

print(message) 
