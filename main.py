# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(51)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

# rect = shape_calculator.Rectangle(1, 1)
# rect.set_height(10)
# rect.set_width(15)
# sq = shape_calculator.Square(5)
# print(rect.get_amount_inside(sq))




# Run unit tests automatically
main(module='test_module', exit=False)