class Rectangle:
	"""When Rectangle object is created, it is initialised with width and height."""

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
		"""Returns string that represents the shape using lines of "*".

		Number of lines equals the height and the number of "*" in each line
		is equal to the width.

		There is a new line (\\n) at the end of each line.

		If the width or height is larger than 50, this returns string "Too big for picture"
		"""
		if self.height > 50 or self.width > 50:
			return 'Too big for picture.'
		else:
			str_geo = ''
			for i in range(self.height):
				str_geo += self.width * '*' + '\n'
			return str_geo

	def get_amount_inside(self, shape) -> int:
		"""Returns the number of times the passed shape coud fit inside the shape (with no rotations).

		Takes another shape (square or rectangle) as argument.
		"""
		return self.width // shape.width * self.height // shape.height


class Square(Rectangle):
	"""Is subclass of Rectangle, and inherits methods and attributes.

	When created, a single side length is passed in.
	It is stored both in width and height attributes of Rectangle class.

	Square class can access Rectangle's methods, but also contains set_side method.

	set_width and set_height methods on square class set both width and height.
	"""

	def __init__(self, side: int) -> None:
		super().__init__(side, side)

	def __str__ (self) -> str:
		return f'Square(side={self.width})'

	def set_side(self, side: int) -> None:
		self.width = side
		self.height = side

