class Orange:
    def __init__(self, variety, color, weight):
        self.variety = variety
        self.color = color
        self.weight = weight

    def display_details(self):
        print("Variety of Orange:", self.variety)
        print("Colour of Orange:", self.color)
        print("Weight of Orange in grams:", self.weight)

class Basket:
    def __init__(self, count):
        self.count = count

    def add_orange(self, orange):
        self.count += 1
        print("Orange added to the basket.")
        orange.display_details()

    def show_status(self):
        print("Oranges in Basket:", self.count)

# Creating Orange objects
o1 = Orange("Nagpur Kamala Orange", "Orange", 165)
o2 = Orange("Mosambi Orange", "Light Greenish Orange", 180)

# Creating Basket object
b1 = Basket(0)
# Interaction between objects
b1.add_orange(o1)
b1.add_orange(o2)
b1.show_status()
