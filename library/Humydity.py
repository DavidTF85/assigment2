def get_humidity_level(Readings):
    readings = humidity
#imput from sensor

if  get_humidity_level < 30:
    print("Dry")

elif get_humidity_level > 60:
    print ("High Humidity")


elif get_humidity_level > 30 and get_humidity_level < 60:
    print("Ok")
