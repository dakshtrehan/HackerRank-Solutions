class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        elementsorted = sorted(self.__elements)
        self.maximumDifference =  elementsorted[-1] - elementsorted[0]
	# Add your code here

# End of Difference class