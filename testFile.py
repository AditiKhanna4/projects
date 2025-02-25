from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

#do not have to test the getters and setters

def test_CarConstruction():
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Honda", "CRV", 2008, 8000)
    c2 = Car("Nissan","Leaf",2010,7000)

    assert c.make == "HONDA"
    assert c.model == "CRV"
    assert c.year == 2007
    assert c.price == 8000

    assert c > c1 == True
    assert c1 < c2 == True
    assert c1 < c2 == False

    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"
    assert str(c1) == "Make: HONDA, Model: CRV, Year: 2008, Price: $8000"
    assert str(c2) == "Make: NISSAN, Model: LEAF, Year: 2010, Price: $7000"

def test_CarInventoryNodeConstruction():
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Honda", "CRV", 2008, 8000)
    c2 = Car("Nissan","Leaf",2010,7000)
    c3 = Car("Mercedes","E class",2018, 10000)

    carNode = CarInventoryNode(c)
    carNode.cars.append(c1)

    assert str(carNode) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: HONDA, Model: CRV, Year: 2008, Price: $8000\n"

    carNode.cars.append(c2)
    carNode.cars.append(c3)

def test_CarInventoryConstruction():
    #methods to check: 
    #addCar, getBestCar, getWorstCar, doesCarExist, inOrder,
    #preOrder, postOrder, getTotalInventoryPrice
    carInvent = CarInventory()

    car1 = Car("Nissan", "Leaf", 2020, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2019, 30000)
    car4 = Car("Mercedes", "Sprinter", 2012, 22000)
    car5 = Car("Ford", "Ranger", 2021, 20000)

    carInvent.addCar(car1)
    carInvent.addCar(car2)
    carInvent.addCar(car3)
    carInvent.addCar(car4)
    carInvent.addCar(car5)

    assert bst.getBestCar("Tesla","Model3") == car2
    assert bst.getBestCar("Honda","CRV") == None
    assert bst.getBestCar("Mercedes","Sprinter") == car3

    assert bst.getWorstCar("Nissan","Leaf") == car1
    assert bst.getWorstCar("Honda","Accord") == None
    assert bst.getWorstCar("Mercedes","Sprinter") == car4

    assert bst.getTotalInventoryPrice() == 140000

    assert bst.doesCarExist("Nissan") == True
    assert bst.doesCarExist("Prius") == False
    assert bst.doesCarExist("Mercedes") == True

    carIn = CarInventory()

    car6 = Car("Ford","Ranger",2015,20000)
    car7 = Car("Volvo","CRV",2010,10000)

    carIn.addCar(car6)
    carIn.addCar(car7)

    assert carIn.inOrder() == "Make: FORD, Model: RANGER, Year: 2015, Price: $20000\nMake: VOLVO, Model: CRV, Year: 2010, Price: $10000"
    assert carIn.preOrder() == "Make: FORD, Model: RANGER, Year: 2015, Price: $20000\nMake: VOLVO, Model: CRV, Year: 2010, Price: $10000"
    assert carIn.postOrder() == "Make: VOLVO, Model: CRV, Year: 2010, Price: $10000\nMake: FORD, Model: RANGER, Year: 2015, Price: $20000"

def test_SuccessorConstruction():
    bst = CarInventory()
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

    assert bst.getSuccessor("BMW","X5") == ("Mazda","CX-5")
    assert bst.getSuccessor("Tesla","Model3") == None
    assert bst.getSuccessor("Audi","A3") == ("BMW","X5")

def test_removingCars():
    bst = CarInventory()
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

    assert bst.removeCar("Tesla","Model3",2018,50000) == True
    assert bst.getCar("Tesla","Model3") == None

    assert bst.removeCar("Mazda","CX-5",2022,25000) == True
    assert bst.getCar("Mazda","CX-5") == None

    assert bst.removeCar("Honda","Civic",2018,30000) == False

    assert bst.preOrder() == "Make: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: AUDI, Model: A3, Year: 2021, Price: $25000\n"
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\n"
    assert bst.postOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\n"
    
    
    

    
    
    
