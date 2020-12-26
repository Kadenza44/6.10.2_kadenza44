class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_info(self):
        print(f"{__class__.__name__}: Height = {self.width}, Width = {self.height}, Area = {self.width * self.height}")

rectangle1 = Rectangle(10, 33)
rectangle2 = Rectangle(11, 31)

rectangle1.get_info()
rectangle2.get_info()
