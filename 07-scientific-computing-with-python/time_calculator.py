def add_time(start: str, duration: str, start_day: str = '') -> str:
	"""
	Adds a time to add to a starting time, and returns the elasped time, inc. days.

	ARGS
		start: str
			start time, HH:MM AM/PM formatted 12-hour-clock

		duration: str
			duration to measure, HH:MM formatted 24-hour-clock

		start_day: str = ''
			optional, starting day of the week

	RETURNS
		end_clock: str
			calculated time, formatted 12-hour-clock & elapsed days.
			If start_day is given, will include ending day of the week
			before elapsed days.
	"""

	# AM/PM evaluation
	start_clock = start.split()
	post_meridiem = start_clock[1] == 'PM'

	# Conversion to decimal number, in 24-hour-clock format
	start_clock = [int(i) for i in start_clock[0].split(':')]
	start_clock = start_clock[0] + start_clock[1] / 60
	start_clock += post_meridiem * 12

	# end time, elasped days not included
	# 0.0001 added to account for memory precision
	duration = [int(i) for i in duration.split(':')]
	end_time = start_clock + duration[0] + duration[1] / 60 + 0.0001

	# evaluation of elasped days
	nth_day = int(end_time // 24)
	end_time -= nth_day * 24
	if nth_day == 0:
		days_later = ''
	elif nth_day == 1:
		days_later = ' (next day)'
	else:
		days_later = f' ({nth_day} days later)'

	# evaluate end weekday
	WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
			'Sunday')
	if len(start_day) == 0:
		week_day = ''
	else:
		# ! doesn't raise exceptions if user given start_day isn´t valid weekday
		start_day = start_day.lower().title()
		day_index = WEEK.index(start_day)
		week_day = ', ' + WEEK[(day_index + nth_day) % 7]

	# back to 12-hour-clock, and output formatting
	am_pm = ' PM' if bool(end_time // 12) else ' AM'
	end_time = end_time % 12
	end_hour = 12 if int(end_time) == 0 else int(end_time)
	end_clock = str(end_hour) + ':' \
		+ str(int((end_time % 1) * 60)).zfill(2) + am_pm \
		+ week_day + days_later

	return end_clock

