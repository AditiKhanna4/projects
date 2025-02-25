from Car import Car

class CarInventoryNode(Car):

    def __init__(self,car):
     #   self.make = car.make.upper()
      #  self.model = car.model.upper()
        super().__init__(car.make,car.model,car.year,car.price)
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self,parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self,left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self,right):
        self.right = right

    def __str__(self):
        s = ""
        if not self.cars:
            return s
        
        for c in self.cars:
            s += str(c) + "\n"
        return s


