
class shape:
    def __init__(self):
        pass
    def getArea(self):
        pass

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def getArea(self):
        return self.length * self.width 


class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius * self.radius

class triangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def getArea(self):
        return (self.length * self.width)/2

#input text file
file = open(r'C:\GIS-Programming-Private\Lab03\shapes.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(",") #this splits the three elements into 3 elements in each line -> rectangle,1,5 
    shape = components[0] 
    if shape == 'Rectangle':
        thing1 = components[1] 
        thing2 = components[2]
        thing1 = int(thing1)
        thing2 = int(thing2)
        rect1 = rectangle(thing1, thing2)
        area1 = rect1.getArea()
        print(area1)
    elif shape == 'Circle':
        thing1 = components[1]
        thing1 = int(thing1)
        circ1 = circle(thing1)
        area1 = circ1.getArea()
        print(area1)
    else: 
        thing1 = components[1]
        thing2 = components[2]
        thing1 = int(thing1)
        thing2 = int(thing2)
        tri1 = triangle(thing1, thing2)
        area1 = tri1.getArea()
        print(area1)

