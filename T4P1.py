class Circle:
    def __init__(self,listInp):
        self.listInp = listInp
        #declared pi value as private variable
        self.__pi = 3.141
        print(listInp)
    # MEthod for calculating area of circle
    def areaOfCircle(self,rad):
        #As pi is a private variable, accessing it within the method
        area = self.__pi * rad ** 2
        return area
    # Method for calculating perimeter of circle
    def periOfCircle(self,rad):
        peri = 2 * self.__pi * rad
        return peri
    # Method for calculating area of circle using list values
    def areaForList(self):
        #here area of circle method for each value of list
        return [self.areaOfCircle(rad) for rad in self.listInp]
    def perimeterForList(self):
        return [self.periOfCircle(rad) for rad in self.listInp]        
list1 = [10,501,22,37,100,999,87,351]
c1 = Circle(list1)
print("Area of circle: ", c1.areaForList())
print("Perimeter of circle: ",c1.perimeterForList())
