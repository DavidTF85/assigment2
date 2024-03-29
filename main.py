#we import the librerys that will be require to the main console works
import os
#import library.statistics
#import library.humidity
#import library.tvoc
#import library.co2
import statistics
#1st define de funtion to get the initial interface (task #6-1)
#as well defince the constants require
TEMPERATURE_ID = 1 #this is the ID number taht will be for each category
HUMIDITY_ID = 2
PRESSURE_ID = 3
ALTITUDE_ID = 4
TVOC_ID = 5
CO2_ID = 6

temperature =TEMPERATURE_ID
humidity = HUMIDITY_ID

#Then set clases so then we can devide it by id,value and time for task 6-3 & 6-4
class TimeSeriesData:
    id = 0
    value = 0
    time = 0
    def __init__(self,id,value,time):
        self.id = id
        self.value = value
        self.time = time

class Instrument:
    data = []
    def add_datum(self,id,value,time):
        datum = TimeSeriesData(id,value,time)
        self.data.append(datum)
        def get_values_by_id(self,id):
            values = [] #append values by id
            for datum in self.data:
                if datum.id == id:
                    values.append(datum.value)
            return values

    def get_mean_by_id(self,id):
            values = self.get_values_by_id(id)
            mean = statistics.mean(get_values)
            return mean

    def get_median_by_id(self,id):
            values = self.get_values_by_id(id)
            median = statistics.median(values)
            return median

    def get_value_by_id(self, id):
            self.id = id
            max_value = get_max_value()
            min_value = get_min_value()

    def print_list(self):
        print("————————————————————————————————————————————")
        print("Id " + "\t" + "Temp " + "\t" + "Pres" + "\t" + "Alt" + "\t" + "TVOC" + "\t" + "CO2")
        print("————————————————————————————————————————————")
        print(" ")
        for datum in self.data:
            print(str(datum.id) +"\t"+ str(datum.value) +"\t"+ str(datum.time))
            print("\n ")
            print("\n ")
            print(" ")

def get_user_input():
    print("_____________________________________________")
    print("Indoor Air Quality Monitoring Command Console")
    print("_____________________________________________\n")
    print("Please select from the following options:")
    print("(1) Add reading")
    print("(2) List readings")
    print("(3) Calculate")
    print("(4) Exit\n")
    user_input = input("Please choice one option: ")
    os.system("clear")
    return user_input
#here i made a funtion for get the interface if input=2 (task 6-2)
#also crate a librery name:readings where the imput will be safe
#for later use in if imput =3 (task 6-3)
def get_readings():
    print("Please input")
    temperature = input("Temperature (Degrees):  ")
    humidity = input("Humidity (%):  ")
    pressure= input("Pressure (kPa):  ")
    altitude= input("Altitude (Fts):  ")
    TVOC= input("TVOC (PPB):  ")
    co2= input("CO2 (PPM):  ")
    readings = {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "altitude": altitude,
        "TVOC" : TVOC,
        "co2" : co2
    }
    os.system("clear")

    print("__________________________")
    print("Successfully saved reading")
    print("__________________________\n")
    print("\nPlease press any key to return to the menu")
    input()

    os.system("clear")
    return readings

tool = Instrument()
#here i made  a funtion for task 6-3
#also a class with the custructor as well a secondari class od data & datum

def print_list(self):
    print("********************")
    print("Id " + "\t" + "Data " + "\t" + "Time")
    print("********************")
    print(" ")
    for datum in self.data:
        print(str(datum.id) +"\t"+ str(datum.value) +"\t"+ str(datum.time))
        print("\n ")
    print("\n ")
    print(" ")

def air_quality():
    print("Indoor Air Quality Monitoring Command Console")
    print("_____________________________________________\n")
    print("list\n")
    print("Id " + "\t" + "Temp " + "\t" + "Humid" + "\t" + "Pres" + "\t" + "Alt" + "\t" + "Tvoc" + "\t" + "CO2" + "\t" + "Time")
    print("\n")
    for datum in self.data:
        print(str(datum.id) +"\t"+ str(datum.value) +"\t"+ str(datum.time))
        print("\n ")
    os.system("clear")



import statistics
def main():
#here the loop and program will start,base of the imput of: get_user_input
#the loop will behave acordint will be need or been terminated
    main_loop_is_running = True

    readings = []

    while main_loop_is_running:
        temperature = []
        humidity = []
        pressure = []
        altitude = []
        tvoc = []
        co2 = []
        time = []

        user_input = get_user_input()

        if user_input == "1":#task 6-2
            data_reading = get_readings()
            readings.append(data_reading)

        elif user_input == "2":#task 6-3
            list_table=print_list()

        elif user_input == "3":
            for reading in readings:
                temperature = reading["temperature"]
                print("temperature")
                print("Unit:Degrees")
                print("Max: ",get_maximum in reading)
                print("Humidity: ",Humidity_level in readings)
        elif user_input == "4":
            main_loop_is_running = False
            print("Exit Successfully of Temperature Calculator! thank you :)")

if __name__ == "__main__":
    main()
#here make a funtion for task 6-2
