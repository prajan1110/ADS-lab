# Create a class rectangle with attributes - length and breadth. Define two methods - find_area(self) and find perimeter(self). Create two instances and find the area and perimeter of the two instances.
class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def find_area(self):
        self.area=self.length * self.breadth
        print("The area of the rectangle is ",self.area)  
          
    def find_perimeter(self):
        self.perimeter=2*(self.length + self.breadth)
        print("The perimeter of the rectangle is ",self.perimeter)  
        
rectangle(5,6).find_area()
rectangle(5,6).find_perimeter()

        
# Create a class triangle with attributes - base, height. Define a method - find_area(self) Create two instances and find the area of the two instances.
class triangle():
    def __init__(self,height,base):
        self.height=height
        self.base=base
        
    def find_area(self):
        self.area= 1/2*self.height * self.base
        print("The area of the triangle is ",self.area)
        
triangle(4,7).find_area()

# Create a class complex number with attributes real and imaginary. Define a method to find the sum of a complex number
class Complex:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine
        
    def find_sum(self, other):
        self.real += other.real
        self.imagine += other.imagine
    
    def complex_sum(self):
        print("The sum of the complex number is", self.real, "+", self.imagine, "i")
        
c1 = Complex(4, 3)
c2 = Complex(5, 7)

c1.find_sum(c2)
c1.complex_sum()  