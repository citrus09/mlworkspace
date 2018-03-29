import math
pslow = (-.5 * math.log(.5, 2))
phigh = (-.5 * math.log(.5, 2))

print (pslow + phigh)

pslow = (-(2/3) * math.log(2/3, 2))
phigh = (-(1/3) * math.log(1/3, 2))

print (pslow + phigh)

information_gain = 1.0 - (3/4)*(pslow + phigh) - (1/4)*0
print((information_gain))

pslow = (-(2/4) * math.log(2/4, 2))
phigh = (-(2/4) * math.log(2/4, 2))

print (pslow + phigh)

information_gain = 1.0 - (2/4)*(pslow + phigh) - (2/4)*(pslow + phigh)
print((information_gain))

##neural networks
print((1*(1/2)) - 1.5)