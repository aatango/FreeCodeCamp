def arithmetic_arranger(problems: list, solve: bool = 'False') -> str:
	""" Rearrange add/sub operations into vertical layout.

	Receives a list of strings that are arithmetic problems
	and returns the problems arranged verticallz and side-by-side.
	
	Function takes optional second argument:
	when true, answer to problem is calculated and displayed.
	"""

	# Valid problem length
	if len(problems) > 5: return 'Error: Too many problems.'

	# Split operands from operator, and validate input
	operands_a = []
	operands_b = []
	operators = []
	for problem in problems:
		problem = problem.split()
		if not (problem[1] == '+' or problem[1] == '-'):
			return 'Error: Operator must be \'+\' or \'-\'.'
		try:
			a = int(problem[0])
			b = int(problem[2])
		except ValueError:
			return 'Error: Numbers must only contain digits.'
		if not (len(str(a)) < 5 and len(str(b)) < 5):
			return 'Error: Numbers cannot be more than four digits.'
		operands_a.append(a)
		operands_b.append(b)
		operators.append(problem[1])

	# If requested, produce solution to each problem
	solutions = [None] * len(operators)
	if solve == True:
		for i in range(len(operators)):
			if operators[i] == '+':
				solutions[i] = operands_a[i] + operands_b[i]
			else:
				solutions[i] = operands_a[i] - operands_b[i]

	# Output formatting
	dashes = []
	for i in range(len(operators)):
		str_a = str(operands_a[i])
		str_b = str(operands_b[i])
		str_s = str(solutions[i])
		char_length = max(len(str_a), len(str_b)) + 2
		dashes.append('-' * char_length)
		operands_a[i] = str_a.rjust(char_length)
		operands_b[i] = str_b.rjust(char_length)
		solutions[i] = str_s.rjust(char_length)
		operands_b[i] = operators[i] + operands_b[i][1:]

	# String concatenation
	str_conc = []
	str_conc.extend((
			'    '.join(operands_a),
			'    '.join(operands_b),
			'    '.join(dashes)
		))
	arranged_problems = '\n'.join(str_conc)
	if solve == True:
		arranged_problems += '\n' + '    '.join(solutions)

	return arranged_problems
