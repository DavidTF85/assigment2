#human_imput= the imput provide by the user
# Values measured in degrees
#but not yet as a funtion :S

def get_maximum(human_imput)
maximum = 0
minimum = 0
i = 0
# maximum calculation
while i < len(human_imput):
    temperature = human_imput[i]
    i = i + 1
    if temperature > maximum:
        maximum = temperature
print ("The maximum temperature is", maximum , "degrees.")

# Minimum calculation
def get_minimum(human_imput)
i = 0
minimum = maximum
while i < len(human_imput):
    temperature = human_imput[i]
    i = i + 1
    if temperature < minimum:
        minimum = temperature
print("The minimum temperature is", minimum, "degrees.")

# this will show the minimum value in the array

# mean (but not a as a funtion :S)
def get_mean (human_imput)
x= len (human_imput)
i= int (x)
print (str(i) + " is the length of the data set.")

y= sum (human_imput)
z= int (y)
print(str(z)+ " is the sum value of the numbers in the data set.")

mean = y / x
h= int(mean)
print ( str(h) + " is the mean (average) of the data.")

#median
def get_median (human_imput)
  import statistics
  median=statistics.median(human_imput)
print(median, "is the median of the data")

# mode
#mode
def get_mode(human_imput)
mod =statistics.mode(human_imput)
print (mod, "is the mode in the data set" )

# print starndart deviation
def get_stdev(human_imput)
stdev = statistics.stdev(human_imput)
print("The standart dDeviation of the sample is" , int(stdev))

# variance calculation
def get_variance(human_imput)
var= statistics.variance(human_imput)
print("Variance of sample set is" , int(var))


#range
def get_range(human_imput)

print(len(human_imput), "is the range of the data set")

#variance
def get_variance(human_imput)
variance = statistics.variance(human_imput)
print(int(variance), "is the variance of the data set")
