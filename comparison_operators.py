temperature = int(input("Enter Temperature in Celsius: "))

if temperature >= 40:
    print('Very Hot')
elif temperature >= 27 and temperature < 40 :
    print('Warm')
elif temperature < 27 and temperature >= 18:
    print('Normal')
elif temperature < 18 and temperature > 0:
    print('Cold')
else:
    print('Freezing')