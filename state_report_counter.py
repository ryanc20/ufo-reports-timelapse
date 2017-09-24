class ReportCounter:
	""" ReportCounter keeps track of the amount of reports per state."""

	state_report_count = {
		'al': 0,
		'ak': 0,
		'az': 0,
		'ar': 0,
		'ca': 0,
		'co': 0,
		'ct': 0,
		'de': 0,
		'fl': 0,
		'ga': 0,
		'hi': 0,
		'id': 0,
		'il': 0,
		'in': 0,
		'ia': 0,
		'ks': 0,
		'ky': 0,
		'la': 0,
		'me': 0,
		'md': 0,
		'ma': 0,
		'mi': 0,
		'mn': 0,
		'ms': 0,
		'mo': 0,
		'mt': 0,
		'ne': 0,
		'nv': 0,
		'nh': 0,
		'nj': 0,
		'nm': 0,
		'ny': 0,
		'nc': 0,
		'nd': 0,
		'oh': 0,
		'ok': 0,
		'or': 0,
		'pa': 0,
		'ri': 0,
		'sc': 0,
		'sd': 0,
		'tn': 0,
		'tx': 0,
		'ut': 0,
		'vt': 0,
		'va': 0,
		'wa': 0,
		'wv': 0,
		'wi': 0,
		'wy': 0,
	}

	def update_count(self, us_state):
		"""Update the count of each state each time there is a report."""
		for state in self.state_report_count:
			if us_state == state:
				self.state_report_count[state] += 1

	def display_count(self):
		"""Print out the count of reports per state."""
		for state in self.state_report_count:
			print(state, self.state_report_count[state])