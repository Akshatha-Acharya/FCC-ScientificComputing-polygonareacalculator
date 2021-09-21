class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return diagonal
    
    def get_picture(self):
        if((self.width > 50) or (self.height > 50)):
            return "Too big for picture."
        
        line =""
        for i in range(self.height):
            line += "*"*self.width + "\n"
        return line
    
    def __str__(self):
        stmt = "Rectangle(width=" + str(self.width) + "," + " height=" + str(self.height) + ")"
        return stmt

    def get_amount_inside(self , Object):
        if((self.width < Object.width) or (self.height < Object.height)):
            return 0
        ans = (self.height // Object.height) * (self.width // Object.width)
        return ans
            
                


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side = side
    
    def set_side(self,side):
        self.side = side
        super().set_height(side)
        super().set_width(side)
    
    def set_height(self, height):
        self.side = height
        super().set_height(height)
    
    def set_width(self, width):
        self.side = width
        super().set_width(width)
    
    def __str__(self):
        stmt = "Square(side=" + str(self.side) + ")"
        return stmt