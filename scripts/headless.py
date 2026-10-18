# Run through a series of commands to test the application
class HeadlessTest:
	def __init__(self, app, verbose : bool = False):
		print(f"\n-- Headless Test --")

		# Display Connected Modules
		if verbose:
			print(f"\nPresent :---:\n\n\tData Display: {app.data_display is not None}\n\tUser: {app.user is not None}\n\tSession: {app.session is not None}\n\tSession Manager: {app.sm is not None}\n\nTests   :---:")

		# Session Manager Tests
		if app.sm is not None:

			# Test 1 Start ------------------------------------------------------------------------------------

			print(f"\nJoining a test session - ")

			result = app.sm.join_or_create_session("Test Session 1")
			expected = "Successfully joined session: 'Test Session 1'"

			if verbose:
				print(f"Function: SessionManager.join_or_create_session")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 1 End ------------------------------------------------------------------------------------


			# Test 2 Start ------------------------------------------------------------------------------------

			print(f"\nJoining another test session - ")

			result = app.sm.join_or_create_session("Test Session 2")
			expected = "Successfully joined session: 'Test Session 2'"

			if verbose:
				print(f"Function: SessionManager.join_or_create_session")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 2 End ------------------------------------------------------------------------------------
   

			# Test 3 Start ------------------------------------------------------------------------------------

			print(f"\nList both active sessions - ")

			result = app.sm.get_remote_sessions()
			expected = ['Test Session 1', 'Test Session 2']

			if verbose:
				print(f"Function: SessionManager.get_remote_sessions")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 3 End ------------------------------------------------------------------------------------
   

			# Test 4 Start ------------------------------------------------------------------------------------

			print(f"\nCreate a new dataset - ")

			result = app.sm.sessions[0].new_dataset("Test Dataset")
			expected = "Dataset 'Test Dataset' successfully created"

			if verbose:
				print(f"Function: Session.new_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 4 End ------------------------------------------------------------------------------------
   

			# Test 5 Start ------------------------------------------------------------------------------------

			print(f"\nAdd the first test datasource to the dataset - ")

			result = app.sm.sessions[0].add_datasource("test_data/test_data_a.csv", "Test Dataset")
			expected = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'"

			if verbose:
				print(f"Function: Session.add_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 5 End ------------------------------------------------------------------------------------
   

			# Test 6 Start ------------------------------------------------------------------------------------

			print(f"\nCompile with the single datasource - ")

			result = app.sm.sessions[0].compile_dataset("Test Dataset")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 6 End ------------------------------------------------------------------------------------


			# Test 7 Start ------------------------------------------------------------------------------------

			print(f"\nAdd the second test datasource to the dataset - ")

			result = app.sm.sessions[0].add_datasource("test_data/test_data_b.csv", "Test Dataset")
			expected = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'"

			if verbose:
				print(f"Function: Session.add_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 7 End ------------------------------------------------------------------------------------


			# Test 8 Start ------------------------------------------------------------------------------------

			print(f"\nCompile with both datasources - ")

			result = app.sm.sessions[0].compile_dataset("Test Dataset")
			expected = {'test_data_a.csv + 1 other(s)': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}, {'key': 'x', 'diff': 'apple', 'value': '1'}, {'key': 'x', 'diff': 'banana', 'value': '2'}, {'key': 'y', 'diff': 'apple', 'value': '1'}, {'key': 'y', 'diff': 'banana', 'value': '2'}, {'key': 'z', 'diff': 'apple', 'value': '1'}, {'key': 'z', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 8 End ------------------------------------------------------------------------------------


			# Test 9 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a line graph from the test dataset - ")

			result = app.data_display.generate_chart_line(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_line")
				# print(f"Expected Result: {expected}")
				# print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")

			# Test 9 End ------------------------------------------------------------------------------------


			# Test 10 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a bar graph from the test dataset - ")

			result = app.data_display.generate_chart_bar(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_bar")
			# 	print(f"Expected Result: {expected}")
			# 	print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")

			# Test 10 End ------------------------------------------------------------------------------------


			# Test 11 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a pie chart from the test dataset - ")

			result = app.data_display.generate_chart_pie(app.sm.sessions[0].compile_dataset("Test Dataset"), "value", "key", "diff", "apple")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_pie")
			# 	print(f"Expected Result: {expected}")
			# 	print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")

			# Test 11 End ------------------------------------------------------------------------------------


			# Test 12 Start ------------------------------------------------------------------------------------

			print(f"\nRemove the second datasource from the test dataset - ")
			
			result = app.sm.sessions[0].remove_datasource("test_data_b.csv", "Test Dataset")
			expected = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'"

			if verbose:
				print(f"Function: Session.remove_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 12 End ------------------------------------------------------------------------------------


			# Test 13 Start ------------------------------------------------------------------------------------

			print(f"\nCompile the test dataset without the second datasource - ")
			
			result = app.sm.sessions[0].compile_dataset("Test Dataset")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 13 End ------------------------------------------------------------------------------------


			# Test 14 Start ------------------------------------------------------------------------------------

			print(f"\nRename the test dataset - ")

			result = app.sm.sessions[0].rename_dataset("Test Dataset", "New Name")
			expected = "Dataset 'Test Dataset' successfully renamed to 'New Name'"

			if verbose:
				print(f"Function: Session.rename_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")
				
			# Test 14 End ------------------------------------------------------------------------------------


			# Test 15 Start ------------------------------------------------------------------------------------

			print(f"\nFail to compile the old dataset name - ")

			result = app.sm.sessions[0].compile_dataset("Test Dataset")
			expected = "Invalid tag: 'Test Dataset'"

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 15 End ------------------------------------------------------------------------------------


			# Test 16 Start ------------------------------------------------------------------------------------

			print(f"\nCompile the new dataset name - ")
			
			result = app.sm.sessions[0].compile_dataset("New Name")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 16 End ------------------------------------------------------------------------------------


			# Test 17 Start ------------------------------------------------------------------------------------

			print(f"\nCompletely remove the test dataset - ")

			result = app.sm.sessions[0].remove_dataset("New Name")
			expected = "Dataset 'New Name' successfully removed"

			if verbose:
				print(f"Function: Session.remove_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 17 End ------------------------------------------------------------------------------------

			# User Tests
			if app.user is not None:

				# Test 1 Start ------------------------------------------------------------------------------------

				print(f"\nSend a message to the database - ")

				result = app.sm.sessions[0].send_message(app.user, "Hello World")
				expected = "Message sent"

				if verbose:
					print(f"Function: Session.send_message")
					print(f"Expected Result: {expected}")
					print(f"Actual Result: {result}")

				if result == expected:
					print("Passed")
				else:
					print("Failed")

				# Test 1 End ------------------------------------------------------------------------------------


				# Test 2 Start ------------------------------------------------------------------------------------

				print(f"\nReturn the session's chat log - ")

				result = app.sm.sessions[0].get_messages()
				expected = "None: Hello World"

				if verbose:
					print(f"Function: Session.get_messages")
					print(f"Expected Result: {expected}")
					print(f"Actual Result: {result}")

				if result == expected:
					print("Passed")
				else:
					print("Failed")

				# Test 2 End ------------------------------------------------------------------------------------

		# Session Tests
		if app.session is not None:

			# Test 1 Start ------------------------------------------------------------------------------------

			print(f"\nCreate a new dataset - ")

			result = app.session.new_dataset("Test Dataset")
			expected = "Dataset 'Test Dataset' successfully created"

			if verbose:
				print(f"Function: Session.new_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 1 End ------------------------------------------------------------------------------------


			# Test 2 Start ------------------------------------------------------------------------------------

			print(f"\nAdd the first test datasource to the dataset - ")
			
			result = app.session.add_datasource("test_data/test_data_a.csv", "Test Dataset")
			expected = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'"

			if verbose:
				print(f"Function: Session.add_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 2 End ------------------------------------------------------------------------------------


			# Test 3 Start ------------------------------------------------------------------------------------

			print(f"\nCompile with the single datasource - ")
			
			result = app.session.compile_dataset("Test Dataset")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 3 End ------------------------------------------------------------------------------------


			# Test 4 Start ------------------------------------------------------------------------------------

			print(f"\nAdd the second test datasource to the dataset - ")
			
			result = app.session.add_datasource("test_data/test_data_b.csv", "Test Dataset")
			expected = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'"

			if verbose:
				print(f"Function: Session.add_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 4 End ------------------------------------------------------------------------------------


			# Test 5 Start ------------------------------------------------------------------------------------

			print(f"\nCompile with both datasources - ")
			
			result = app.session.compile_dataset("Test Dataset")
			expected = {'test_data_a.csv + 1 other(s)': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}, {'key': 'x', 'diff': 'apple', 'value': '1'}, {'key': 'x', 'diff': 'banana', 'value': '2'}, {'key': 'y', 'diff': 'apple', 'value': '1'}, {'key': 'y', 'diff': 'banana', 'value': '2'}, {'key': 'z', 'diff': 'apple', 'value': '1'}, {'key': 'z', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 5 End ------------------------------------------------------------------------------------


			# Test 6 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a line graph from the test dataset - ")
			
			result = app.data_display.generate_chart_line(app.session.compile_dataset("Test Dataset"), "key", "value", "diff")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_line")
			# 	print(f"Expected Result: {expected}")
			# 	print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")


			# Test 6 End ------------------------------------------------------------------------------------


			# Test 7 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a bar graph from the test dataset - ")

			result = app.data_display.generate_chart_bar(app.session.compile_dataset("Test Dataset"), "key", "value", "diff")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_bar")
			# 	print(f"Expected Result: {expected}")
			# 	print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")

			# Test 7 End ------------------------------------------------------------------------------------


			# Test 8 Start ------------------------------------------------------------------------------------

			print(f"\nGenerate a pie chart from the test dataset - ")

			result = app.data_display.generate_chart_pie(app.session.compile_dataset("Test Dataset"), "value", "key", "diff", "apple")

			# There is currently no return value for this function

			if verbose:
				print(f"Function: DataDisplay.generate_chart_pie")
			# 	print(f"Expected Result: {expected}")
			# 	print(f"Actual Result: {result}")

			# if result == expected:
			# 	print("Passed")
			# else:
			# 	print("Failed")

			# Test 8 End ------------------------------------------------------------------------------------


			# Test 9 Start ------------------------------------------------------------------------------------

			print(f"\nRemove the second datasource from the test dataset - ")

			result = app.session.remove_datasource("test_data_b.csv", "Test Dataset")
			expected = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'"
			
			if verbose:
				print(f"Function: Session.remove_datasource")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 9 End ------------------------------------------------------------------------------------


			# Test 10 Start ------------------------------------------------------------------------------------

			print(f"\nCompile the test dataset without the second datasource - ")
			
			result = app.session.compile_dataset("Test Dataset")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 10 End ------------------------------------------------------------------------------------


			# Test 11 Start ------------------------------------------------------------------------------------

			print(f"\nRename the test dataset - ")
			
			result = app.session.rename_dataset("Test Dataset", "New Name")
			expected = "Dataset 'Test Dataset' successfully renamed to 'New Name'"

			if verbose:
				print(f"Function: Session.rename_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 12 End ------------------------------------------------------------------------------------


			# Test 13 Start ------------------------------------------------------------------------------------

			print(f"\nFail to compile the old dataset name - ")

			result = app.session.compile_dataset("Test Dataset")
			expected = "Invalid tag: 'Test Dataset'"

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 13 End ------------------------------------------------------------------------------------


			# Test 14 Start ------------------------------------------------------------------------------------

			print(f"\nCompile the new dataset name - ")

			result = app.session.compile_dataset("New Name")
			expected = {'test_data_a.csv': [{'key': 'a', 'diff': 'apple', 'value': '1'}, {'key': 'a', 'diff': 'banana', 'value': '2'}, {'key': 'b', 'diff': 'apple', 'value': '1'}, {'key': 'b', 'diff': 'banana', 'value': '2'}, {'key': 'c', 'diff': 'apple', 'value': '1'}, {'key': 'c', 'diff': 'banana', 'value': '2'}]}

			if verbose:
				print(f"Function: Session.compile_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 14 End ------------------------------------------------------------------------------------


			# Test 15 Start ------------------------------------------------------------------------------------

			print(f"\nCompletely remove the test dataset - ")

			result = app.session.remove_dataset("New Name")
			expected = "Dataset 'New Name' successfully removed"

			if verbose:
				print(f"Function: Session.remove_dataset")
				print(f"Expected Result: {expected}")
				print(f"Actual Result: {result}")

			if result == expected:
				print("Passed")
			else:
				print("Failed")

			# Test 15 End ------------------------------------------------------------------------------------
