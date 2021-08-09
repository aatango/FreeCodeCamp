"""Module documentation per assignment, in README.md"""

class Rectangle:

	def __init__ (self, width: int, height:int) -> None:
		self.height = height
		self.width = width

	def __str__(self) -> str:
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_width(self, width: int) -> None:
		self.width = width

	def set_height(self, height: int) -> None:
		self.height = height

	def get_area(self) -> int:
		return self.height * self.width

	def get_perimeter(self) -> int:
		return 2 * (self.height + self.width)

	def get_diagonal(self) -> int:
		return (self.width ** 2 + self.height ** 2) ** 0.5

	def get_picture(self) -> str:
		if self.height > 50 or self.width > 50:
			return 'Too big for picture.'
		else:
			str_geo = ''
			for i in range(self.height):
				str_geo += self.width * '*' + '\n'
			return str_geo

	def get_amount_inside(self, shape) -> int:
		return self.width // shape.width * self.height // shape.height


class Square(Rectangle):

	def __init__(self, side: int) -> None:
		super().__init__(side, side)

	def __str__ (self) -> str:
		return f'Square(side={self.width})'

	def set_side(self, side: int) -> None:
		self.width = side
		self.height = side

