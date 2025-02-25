from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory(CarInventoryNode):

    def __init__(self):
        self.root = None

    def addCar(self,car):
        if self.root is None:
            self.root = CarInventoryNode(car)
        else:
            self.insertCar(car,self.root)

    def insertCar(self,car,currentNode):
        if car.make == currentNode.make and car.model == currentNode.model:
            currentNode.cars.append(car)
            
        elif (car.make == currentNode.make and car.model < currentNode.model) or car.make < currentNode.make:
            if currentNode.getLeft() is None:
                nextNode = CarInventoryNode(car)
                currentNode.setLeft(nextNode)
                nextNode.setParent(currentNode)
                
            else:
                self.insertCar(car,currentNode.getLeft())
                
        else:
            if currentNode.getRight() is None:
                nextNode = CarInventoryNode(car)
                currentNode.setRight(nextNode)
                nextNode.setParent(currentNode)
            else:
                self.insertCar(car,currentNode.getRight())

    def doesCarExist(self,car):
        return self.carExists(car,self.root)

    def carExists(self,car,currentNode):
        if currentNode is None:
            return False

        for c in currentNode.cars:
            if c == car:
                return True

        if car < currentNode.cars[0]:
            return self.carExists(car, currentNode.getLeft())
        else:
            return self.carExists(car, currentNode.getRight())

    def inOrder(self):
        return self.orderCheck(self.root)

    def orderCheck(self,currentNode):
        s = ""
        if currentNode is None:
            return s
        else:
            s += self.orderCheck(currentNode.getLeft())

            for c in currentNode.cars:
                s += str(c) + "\n"
            s += self.orderCheck(currentNode.getRight())

            return s

    def preOrder(self):
        return self.preOrderHelper(self.root)

    def preOrderHelper(self,currentNode):
        s = ""
        if currentNode is None:
            return s
        else:
            for c in currentNode.cars:
                s += str(c) + "\n"
            s += self.preOrderHelper(currentNode.getLeft())
            s += self.preOrderHelper(currentNode.getRight())

            return s

    def postOrder(self):
        return self.postOrderHelper(self.root)

    def postOrderHelper(self,currentNode):
        s = ""
        if currentNode is None:
            return s
        else:
            s += self.postOrderHelper(currentNode.getLeft())
            s += self.postOrderHelper(currentNode.getRight())

            for c in currentNode.cars:
                s += str(c) + "\n"

            return s

    def getBestCar(self,make,model):
        return self.bestCar(make,model,self.root)

    def bestCar(self,make,model,currentNode):
        if currentNode is None:
            #print("test")
            return None

        elif currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            #print("test1")
            best = currentNode.cars[0]
            for c in currentNode.cars:
                if best is None or c.year > best.year or (c.year == best.year and c.price > best.price):
                    best = c 
            return best
        elif (make.upper() == currentNode.make.upper() and model.upper() > currentNode.model.upper()) or make.upper() > currentNode.make.upper():
            return self.bestCar(make,model,currentNode.getRight())
        else:
            return self.bestCar(make,model,currentNode.getLeft())
        
    def getWorstCar(self,make,model):
        return self.worstCar(self.root,make,model)

    def worstCar(self,currentNode,make,model):
        #worst = currentNode.cars[0]
        if currentNode is None:
            return None
        
        elif currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            worst = None
            for c in currentNode.cars:
                if worst is None or c.year < worst.year or (c.year == worst.year and c.price < worst.price):
                    worst = c
            return worst
        elif (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()) or make.upper() < currentNode.make.upper():
            return self.worstCar(currentNode.getLeft(),make,model)
        else:
            return self.worstCar(currentNode.getRight(),make,model)


    def getTotalInventoryPrice(self):
        return self.priceCalculation(self.root)

    def priceCalculation(self,currentNode):
        priceTotal = 0
        if currentNode is None:
            return priceTotal
        else:
            for c in currentNode.cars:
                priceTotal += c.price

            priceTotal += self.priceCalculation(currentNode.getLeft())
            priceTotal += self.priceCalculation(currentNode.getRight())

            return priceTotal

    def getSuccessor(self,make,model):
        currentNode = self.getNode(self.root,make,model)
        if currentNode is None:
            return None
        if currentNode.getRight():
            return self.getMinimum(currentNode.getRight())
        return self.findSuccessor(make,model)

    def getNode(self,currentNode,make,model):
        if currentNode is None:
            return None
        if currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            return currentNode
        if make.upper() < currentNode.make.upper() or (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()):
            return self.getNode(currentNode.getLeft(),make,model)
        return self.getNode(currentNode.getRight(),make,model)

    def getMinimum(self,currentNode):
        current = currentNode
        while current.getLeft():
            current = current.getLeft()
        return current


    def findSuccessor(self,make,model):
        s = None
        currentNode = self.root
        while currentNode is not None:
            if make.upper() < currentNode.make.upper() or (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()):
                s = currentNode
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
        return s

    def removeCar(self,make,model,year,price):
        carRemoval = Car(make,model,year,price)
        return self.removeCarNode(self.root,carRemoval)

    def removeCarNode(self,currentNode,carRemoval):
        if currentNode is None:
            return False

        if carRemoval in currentNode.cars:
            currentNode.cars.remove(carRemoval)
            if not currentNode.cars:
                self.root = self.removeNode(self.root,currentNode)
            return True
        elif carRemoval < currentNode:
            return self.removeCarNode(currentNode.getLeft(),carRemoval)
        else:
            return self.removeCarNode(currentNode.getRight(),carRemoval)

        
            
    def removeNode(self,currentNode,removalNode):
        #if currentNode.getLeft() is None and currentNode.getRight() is None:
        if currentNode is None:
            return None
        if removalNode < currentNode:
            currentNode.left = self.removeNode(currentNode.getLeft(),removalNode)
        elif removalNode > currentNode:
            currentNode.right = self.removeNode(currentNode.getRight(),removalNode)
        else:
            if currentNode.getLeft() is None and currentNode.getRight() is None:
                return None
            elif currentNode.getLeft() is None:
                return currentNode.getRight()
            elif currentNode.getRight() is None:
                return currentNode.getLeft()
            else:
                minim = self.findMinimum(currentNode.getRight())
                currentNode.make = minim.make
                currentNode.model = minim.model
                currentNode.cars = minim.cars
                currentNode.right = self.removeNode(currentNode.getRight(),minim)
                
        return currentNode

    def findMinimum(self,currentNode):
        current = currentNode
        while current.left is not None:
            current = current.left
        return current
            
                    
'''bst = CarInventory()
car1 = Car("Mazda", "CX-5", 2022, 25000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("BMW", "X5", 2022, 60000)
car4 = Car("BMW", "X5", 2020, 58000)
car5 = Car("Audi", "A3", 2021, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)
bst.removeCar("Tesla","Model3",2018,50000)
bst.removeCar("Mazda","CX-5",2022,25000)
bst.removeCar("Honda","Civic",2018,30000)
print(bst.postOrder())'''








        
            
    
            
