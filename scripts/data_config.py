# Handles the configuration for the data display

class DataConfig:
	def __init__(self, dataset):
		self.update_dataset(dataset)

	def update_dataset(self, dataset):
		# Default values
		self.data_name = ""
		self.data = []

		self.headings = []

		self.valid_y_keys = []
		self.y_key = ""

		self.x_key = ""
		self.series_key = None
  
		self.valid_series = []
		self.get_series = ""


		if dataset:
			prev_name = self.data_name
			prev_data = self.data

			# The data that the data display will show
			self.data_name = next(iter(dataset.keys()))
			self.data = next(iter(dataset.values()))


			# Check if one of the values in the data is an integer
			has_int = False

			for value in self.data[0]:
				if self.data[0][value].isnumeric():
					self.valid_y_keys.append(value)
					has_int = True

			if not has_int:
				self.data_name = prev_name
				self.data = prev_data
				return "Data has no number to plot"

			if len(self.data) >= 1:
				# Get the values being used as the labels/keys/headings of each value
				self.headings = list(self.data[0].keys())

			# If the list is long enough, set the corresponsing value to the key
			if len(self.valid_y_keys) >= 1:
				self.y_key = self.valid_y_keys[0]

			# Get the first values that don't overlap
			for heading in self.headings:
				if heading is not self.y_key:
					self.x_key = heading

			for heading in self.headings:
				if heading is not self.y_key and heading is not self.x_key:
					self.series_key = heading
	  
			# If there is a series key, get all its values and assign the first one as the get_series
			if self.series_key:
				for row in self.data:
					if self.series_key in row.keys():
						self.valid_series.append(row[self.series_key])
				
				self.get_series = self.valid_series[0]
		 
		 
	def change_setting(self, key, heading):
		"""Updates the given key to the given heading"""
		match key:
			case "x":
				if heading not in self.headings:
					return "Invalid heading"

				self.x_key = heading
    
				return "X key updated successfully"
 
			case "y":
				if heading not in self.valid_y_keys:
					return "Invalid heading"

				self.y_key = heading
    
				return "Y key updated successfully"
  
			case "series":
				if heading not in self.headings:
					return "Invalid heading"
  
				self.series_key = heading
	 
				# Reload the get_series
				self.valid_series = []
    
				if self.series_key:
					for row in self.data:
						if self.series_key in row.keys():
							self.valid_series.append(row[self.series_key])
					
					self.get_series = self.valid_series[0]
		
				return "Series key updated successfully"
 
			case "get":
				if heading not in self.valid_series:
					return "Invalid heading"
  
				self.get_series = heading
    
				return "Getting series updated successfully"
 
			case _:
				return "Invalid key"