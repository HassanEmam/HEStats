from hestat import HEStat

list = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]
print("Summation", HEStat.summation(list, 3, 4))
print("Mean",HEStat.mean(list))
print("Variance", HEStat.variance(list))
print("StdDev", HEStat.stdDev(list))
print("Median", HEStat.median(list))
