print ("FahrenheitTemperature\CelsiusTemperature")
for CelsiusTemperature in range (21):
    FahrenheitTemperature = (5/9) * CelsiusTemperature + 32

    print (CelsiusTemperature, "\t\t\t\t", \
           format( FahrenheitTemperature, ".1f"))
