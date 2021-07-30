import math

print(math.pow(2, 3)) #8.0


import random
random.randint(1,100) #включая 100


import statistics
#mean
nums=[1,5,33,12,46,33,2]
print(statistics.mean(nums))
#median
print(statistics.median(nums))
#mode
print(statistics.mode(nums))
#Fast, floating point arithmetic mean.
print(statistics.fmean(nums))
#Divide data into intervals with equal probability.
print(statistics.quantiles(nums))
#Low median of data.
print(statistics.median_low(nums))


import keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
