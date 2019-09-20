# how caculate the air quality rating of the `volatile organic compounds` (TVOC)
def get_TVOC(TVOC):

    TVOC = int(input("Please enter TVOC value"))

    if TVOC > 2200 and TVOC < 5500:
        print ("level 5, unhealty")

    elif TVOC > 660 and TVOC <= 2200:
        print ("level 4, poor")

    elif TVOC > 220 and TVOC <=660:
        print ("level 3, moderate")

    elif TVOC > 65 and TVOC <= 220:
        print ("level 2, good")

    elif TVOC <= 65:
        print ("level 1, excellent")
