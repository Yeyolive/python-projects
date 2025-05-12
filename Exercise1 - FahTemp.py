
def celsius(Fahrenheit):
    return (Fahrenheit - 32)*(5/9)

print("Fahrenheit \t\t Celsius")

for i in range(21):
    print (i, "\t\t",celsius(i))


