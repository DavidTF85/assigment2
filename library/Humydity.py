Humidity_level = 61
#imput from sensor

if  Humidity_level < 30:
    print("Dry")

elif Humidity_level > 60:
    print ("High Humidity")


elif Humidity_level > 30 and Humidity_level < 60:
    print("Ok")
