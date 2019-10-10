#get_readings= the imput provide by the user
# Values measured in degrees
#but not yet as a funtion :S
def get_maximum(get_readings)
maximum = 0
minimum = 0
i = 0
# maximum calculation
while i < len(get_readings):
    temperature = get_readings[i]
    i = i + 1
    if temperature > maximum:
        maximum = temperature
print ("The maximum temperature is", maximum , "degrees.")

# Minimum calculation
def get_minimum(get_readings)
i = 0
minimum = maximum
while i < len(get_readings):
    temperature = get_readings[i]
    i = i + 1
    if temperature < minimum:
        minimum = temperature
print("The minimum temperature is", minimum, "degrees.")

# this will show the minimum value in the array

# mean (but not a as a funtion :S)
def get_mean (get_readings)
x= len (get_readings)
i= int (x)
print (str(i) + " is the length of the data set.")

y= sum (get_readings)
z= int (y)
print(str(z)+ " is the sum value of the numbers in the data set.")

mean = y / x
h= int(mean)
print ( str(h) + " is the mean (average) of the data.")

#median
def get_median (get_readings)
  import statistics
  median=statistics.median(get_readings)
print(median, "is the median of the data")

# mode
#mode
def get_mode(get_readings)
mod =statistics.mode(get_readings)
print (mod, "is the mode in the data set" )

# print starndart deviation
def get_stdev(get_readings)
stdev = statistics.stdev(get_readings)
print("The standart dDeviation of the sample is" , int(stdev))

# variance calculation
def get_variance(get_readings)
var= statistics.variance(get_readings)
print("Variance of sample set is" , int(var))


#range
def get_range(get_readings)

print(len(get_readings), "is the range of the data set")

#variance
def get_variance(get_readings)
variance = statistics.variance(get_readings)
print(int(variance), "is the variance of the data set")
