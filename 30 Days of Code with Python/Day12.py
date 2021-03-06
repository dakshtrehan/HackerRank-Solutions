class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        averageScore = 0
        for i in range(len(scores)):
            averageScore += scores[i]

        if 90 <= (averageScore/len(scores)) <= 100:
            return "O"
        elif 80 <= (averageScore/len(scores)) < 90:
            return "E"
        elif 70 <= (averageScore/len(scores)) < 80:
            return "A"
        elif 55 <= (averageScore/len(scores)) < 70:
            return "P"
        elif 40 <= (averageScore/len(scores)) < 55:
            return "D"
        else:
            return "T"

line = input().split()