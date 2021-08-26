import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self,**balls: dict) -> None:
		self.ball_colours = list(balls.keys())
		self.ball_numbers = list(balls.values())
		self.contents = []
		for i in range(len(self.ball_colours)):
			self.contents.extend([self.ball_colours[i]] * self.ball_numbers[i])

	def draw(self,count: int) -> list:
		"""Removes balls at random from contents, returning those as list.

		return random.sample(self.contents, count) achieves overall result,
		but fails assignment tests. Alternative method is included.
		"""

		removed_balls = []
		if count >= len(self.contents):	return self.contents
		for i in range(count):
			drawn = random.choice(self.contents)
			removed_balls.append(drawn)
			self.contents.remove(drawn)
		return removed_balls


def experiment(
	hat: object,
	expected_balls: dict,
	num_balls_drawn: int,
	num_experiments: int) -> float:
	"""Runs the experiment to calculate the desired probability.

	An experiment consists of:
	- starting with a hat containing the specified balls;
	- draw a number of balls; and
	- check for expected outcome.

	Results should have AT LEAST same as expected_balls, more is also OK.
	"""

	success = 0
	for i in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		results = hat_copy.draw(num_balls_drawn)
		for k in expected_balls.keys():
			if results.count(k) < expected_balls[k]:
				break
		else:
			success += 1
	return success / num_experiments

