#
#  summation.py
#  Adding numbers for fun. Getting used to Python semantics
#

from math import sqrt

#  Maximum value to loop to
NUM_VALUES = 100

#  Initialize sum count
totalSum = 0

#  xrange only generates numbers as needed so it can be way more memory efficient if the loop has the possibility
#  of breaking early.  Why not use it all the time?

#  scratch that.  xrange is deprecated in Python3 and range behaves like xrange used to.  Good reminder to change
#  my IDE over to Python3
for x in range(0, NUM_VALUES):
    totalSum += x
    print("added ", x)
    #  scope is indicated solely by indentation.

print(totalSum)

#  Did this just to learn how to do an import.  Did sqrt explicitly.  Wildcard imports still suck.
print(sqrt(totalSum))
