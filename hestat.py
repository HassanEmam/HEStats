import math

class HEStat:

    @staticmethod
    def summation(list, start=0, finish=0):
        if list:
            res = 0
            if finish == 0 :
                finish = len(list)
            else:
                finish = finish
            if start > 0:
                start = start -1
            for i in range(start, finish):
                res += list[i]
            return res

    @staticmethod
    def mean(list):
        if list:
            summation = HEStat.summation(list)
            n = len(list)
            value = summation / n
            return value

    @staticmethod
    def variance(list):
        average = HEStat.mean(list)
        variance = 0
        for x in list:
            var = x - average
            variance = variance + (var * var)
        return variance/ (len(list))

    @staticmethod
    def stdDev(list):
        if list:
            return math.sqrt(HEStat.variance(list))

    @staticmethod
    def median(list):
        if list:
            list.sort()
            print(list)
            if len(list)%2 == 0:
                indx1 = int(len(list)/2)
                indx2 = indx1-1
                return (list[indx1]+list[indx2])/2
            else:
                indx = int(len(list)/2)
                return list[indx]

