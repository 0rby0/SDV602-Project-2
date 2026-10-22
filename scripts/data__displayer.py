# Takes in a set of data and generates a graph from it
import matplotlib.pyplot as plt
from operator import itemgetter

class DataDisplay:
	def generate_chart_line(self, data, x_key, y_key, series_key=None):
		"""Creates a line chart from the given settings."""
		try:
			if not next(iter(data.values())):
				print("No data to plot!")
				return

			series = {}
			for row in next(iter(data.values())):
					series.setdefault(row.get(series_key), []).append(row)

			plt.figure(figsize=(8, 6))

			for name, rows in series.items():
					rows.sort(key=itemgetter(x_key))

					x_values = []
					y_values = []

					for row in rows:
						x_values.append(row[x_key])
						y_values.append(float(row[y_key]))

					plt.plot(x_values, y_values, marker='o', label=name)

			if series_key:
					plt.legend()

			plt.xlabel(x_key)
			plt.ylabel(y_key)
			plt.title(next(iter(data.keys())))

			plt.show()  

		except:
			return "Graph failed to plot"


	def generate_chart_pie(self, data, value_key, label_key, series_key, get_series):
		"""Creates a pie chart from the given settings."""
		try:
			if not next(iter(data.values())):
				print("No data to plot!")
				return

			values = []
			labels = []

			for row in next(iter(data.values())):
				if row[series_key] == get_series:
					values.append(int(row[value_key]))
					labels.append(row[label_key])

			plt.pie(values, labels=labels, autopct='%1.0f%%')
			plt.show()

		except:
			return "Graph failed to plot"


	def generate_chart_bar(self, data, x_key, y_key, series_key):
		"""Creates a bar chart from the given settings."""
		try:
			if not next(iter(data.values())):
				print("No data to plot!")
				return

			x_values = []
			y_values = {}

			for data_row in next(iter(data.values())):
				if data_row[x_key] not in x_values:
					x_values.append(data_row[x_key])

				if data_row[series_key] in y_values:
					y_values[data_row[series_key]].append(int(data_row[y_key]))
				else:
					y_values[data_row[series_key]] = [int(data_row[y_key])]

			plt.grouped_bar(y_values, tick_labels=x_values)
			plt.legend()
			plt.show()
   
		except:
			return "Graph failed to plot"