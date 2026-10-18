# Run through a series of commands to test the application
from test import Test

# Verbosity Levels:
#
# 0 = Just prints "passed" if all tests passed or "failed" if any tests failed
# 1 = Prints the short summary with how many tests passed and failed
# 2 = Prints the pass/fail for each test and the summary
# 3 = Prints all details, including what modules are present

class HeadlessTest:
	def __init__(self, app, verbosity : int = 2):

		print(f"\n-- Headless Test --")
		results = []

		# Display Connected Modules
		if verbosity >= 3:
			print(f"\nPresent :---:\n\n\tData Display: {app.data_display is not None}\n\tUser: {app.user is not None}\n\tSession: {app.session is not None}\n\tSession Manager: {app.sm is not None}\n\nTests   :---:")

		# Session Manager Tests
		if app.sm is not None:

			# Test 1.1 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Joining a test session",
											function_description = "SessionManager.join_or_create_session",
											test_function = app.sm.join_or_create_session("Test Session 1"),
											expected_result = "Successfully joined session: 'Test Session 1'",
											print_verbose = (verbosity >= 3)))

			# Test 1.1 End ------------------------------------------------------------------------------------


			# Test 1.2 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Joining another test session",
									  			function_description = "SessionManager.join_or_create_session",
											test_function = app.sm.join_or_create_session("Test Session 2"),
											expected_result = "Successfully joined session: 'Test Session 2'",
											print_verbose = (verbosity >= 3)))

			# Test 1.2 End ------------------------------------------------------------------------------------
	

			# Test 1.3 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "List both active sessions",
									  			function_description = "SessionManager.get_remote_sessions",
											test_function = app.sm.get_remote_sessions(),
											expected_result = ['Test Session 1', 'Test Session 2'],
											print_verbose = (verbosity >= 3)))

			# Test 1.3 End ------------------------------------------------------------------------------------
	

			# Test 1.4 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Create a new dataset",
									  			function_description = "Session.new_dataset",
											test_function = app.sm.sessions[0].new_dataset("Test Dataset"),
											expected_result = "Dataset 'Test Dataset' successfully created",
											print_verbose = (verbosity >= 3)))

			# Test 1.4 End ------------------------------------------------------------------------------------
	

			# Test 1.5 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Add the first test datasource to the dataset",
									  			function_description = "Session.add_datasource",
											test_function = app.sm.sessions[0].add_datasource("test_data/test_data_a.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.5 End ------------------------------------------------------------------------------------
	

			# Test 1.6 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Compile with the single datasource",
									  			function_description = "Session.compile_dataset",
											test_function = app.sm.sessions[0].compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'},
																									{'key': 'a', 'diff': 'banana', 'value': '2'},
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.6 End ------------------------------------------------------------------------------------


			# Test 1.7 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the second test datasource to the dataset",
													function_description = "Session.add_datasource",
											test_function = app.sm.sessions[0].add_datasource("test_data/test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.7 End ------------------------------------------------------------------------------------


			# Test 1.8 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with both datasources",
													function_description = "Session.compile_dataset",
											test_function = app.sm.sessions[0].compile_dataset("Test Dataset"),
											expected_result =  {'test_data_a.csv + 1 other(s)': [
																														{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'c', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'x', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'x', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'y', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'y', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'z', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'z', 'diff': 'banana', 'value': '2'}
																													]},
											print_verbose = (verbosity >= 3)))

			# Test 1.8 End ------------------------------------------------------------------------------------


			# Test 1.9 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a line graph from the test dataset",
													function_description = "DataDisplay.generate_chart_line",
											test_function = app.data_display.generate_chart_line(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 1.9 End ------------------------------------------------------------------------------------


			# Test 1.10 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a bar graph from the test dataset",
													function_description = "DataDisplay.generate_chart_bar",
											test_function = app.data_display.generate_chart_bar(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 1.10 End ------------------------------------------------------------------------------------


			# Test 1.11 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a pie chart from the test dataset",
													function_description = "DataDisplay.generate_chart_pie",
											test_function = app.data_display.generate_chart_pie(app.sm.sessions[0].compile_dataset("Test Dataset"), "value", "key", "diff", "apple"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 1.11 End ------------------------------------------------------------------------------------


			# Test 1.12 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Remove the second datasource from the test dataset",
													function_description = "Session.remove_datasource",
											test_function = app.sm.sessions[0].remove_datasource("test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.12 End ------------------------------------------------------------------------------------


			# Test 1.13 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the test dataset without the second datasource",
													function_description = "Session.compile_dataset",
											test_function = app.sm.sessions[0].compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.13 End ------------------------------------------------------------------------------------


			# Test 1.14 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Rename the test dataset",
													function_description = "Session.rename_dataset",
											test_function = app.sm.sessions[0].rename_dataset("Test Dataset", "New Name"),
											expected_result = "Dataset 'Test Dataset' successfully renamed to 'New Name'",
											print_verbose = (verbosity >= 3)))
				
			# Test 1.14 End ------------------------------------------------------------------------------------


			# Test 1.15 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Fail to compile the old dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.sessions[0].compile_dataset("Test Dataset"),
											expected_result = "Invalid tag: 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.15 End ------------------------------------------------------------------------------------


			# Test 1.16 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the new dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.sessions[0].compile_dataset("New Name"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.16 End ------------------------------------------------------------------------------------


			# Test 1.17 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Completely remove the test dataset",
													function_description = "Session.remove_dataset",
											test_function = app.sm.sessions[0].remove_dataset("New Name"),
											expected_result = "Dataset 'New Name' successfully removed",
											print_verbose = (verbosity >= 3)))

			# Test 1.17 End ------------------------------------------------------------------------------------


			# Test 1.18 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Leave the first test session",
															function_description = "SessionManager.leave_session",
            											test_function = app.sm.leave_session("Test Session 1"),
															expected_result = "Successfully left session",
                                             print_verbose = (verbosity >= 3)))
	
			# Test 1.18 Start ------------------------------------------------------------------------------------


			# Test 1.19 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Fail to leave a non-existant session",
															function_description = "SessionManager.leave_session",
            											test_function = app.sm.leave_session("Not a session"),
															expected_result = "Not in session",
                                             print_verbose = (verbosity >= 3)))
	
			# Test 1.19 Start ------------------------------------------------------------------------------------
   
			# User Tests
			if app.user is not None:

				# Test 2.1 Start ------------------------------------------------------------------------------------

				results.append(Test ( test_name = "Send a message to the database",
												function_description = "Session.send_message",
												test_function = app.sm.sessions[0].send_message(app.user, "Hello World"),
												expected_result = "Message sent",
												print_verbose = (verbosity >= 3)))

				# Test 2.1 End ------------------------------------------------------------------------------------


				# Test 2.2 Start ------------------------------------------------------------------------------------

				results.append(Test ( test_name = "Return the session's chat log",
												function_description = "Session.get_messages",
												test_function = app.sm.sessions[0].get_messages(),
												expected_result = "None: Hello World",
												print_verbose = (verbosity >= 3)))

				# Test 2.2 End ------------------------------------------------------------------------------------

		# Session Tests
		if app.session is not None:

			# Test 3.1 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Create a new dataset",
													function_description = "Session.new_dataset",
											test_function = app.session.new_dataset("Test Dataset"),
											expected_result = "Dataset 'Test Dataset' successfully created",
											print_verbose = (verbosity >= 3)))

			# Test 3.1 End ------------------------------------------------------------------------------------


			# Test 3.2 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the first test datasource to the dataset",
													function_description = "Session.add_datasource",
											test_function = app.session.add_datasource("test_data/test_data_a.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 3.2 End ------------------------------------------------------------------------------------


			# Test 3.3 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with the single datasource",
													function_description = "Session.compile_dataset",
											test_function = app.session.compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 3.3 End ------------------------------------------------------------------------------------


			# Test 3.4 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the second test datasource to the dataset",
													function_description = "Session.add_datasource",
											test_function = app.session.add_datasource("test_data/test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 3.4 End ------------------------------------------------------------------------------------


			# Test 3.5 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with both datasources",
													function_description = "Session.compile_dataset",
											test_function = app.session.compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv + 1 other(s)': [
																														{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'c', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'x', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'x', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'y', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'y', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'z', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'z', 'diff': 'banana', 'value': '2'}
																													]},
											print_verbose = (verbosity >= 3)))

			# Test 3.5 End ------------------------------------------------------------------------------------


			# Test 3.6 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a line graph from the test dataset",
													function_description = "DataDisplay.generate_chart_line",
											test_function = app.data_display.generate_chart_line(app.session.compile_dataset("Test Dataset"), "key", "value", "diff"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 3.6 End ------------------------------------------------------------------------------------


			# Test 3.7 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a bar graph from the test dataset",
													function_description = "DataDisplay.generate_chart_bar",
											test_function = app.data_display.generate_chart_bar(app.session.compile_dataset("Test Dataset"), "key", "value", "diff"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 3.7 End ------------------------------------------------------------------------------------


			# Test 3.8 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a pie chart from the test dataset",
													function_description = "DataDisplay.generate_chart_pie",
											test_function = app.data_display.generate_chart_pie(app.session.compile_dataset("Test Dataset"), "value", "key", "diff", "apple"),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 3.8 End ------------------------------------------------------------------------------------


			# Test 3.9 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Remove the second datasource from the test dataset",
													function_description = "Session.remove_datasource",
											test_function = app.session.remove_datasource("test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 3.9 End ------------------------------------------------------------------------------------


			# Test 3.10 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the test dataset without the second datasource",
													function_description = "Session.compile_dataset",
											test_function = app.session.compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 3.10 End ------------------------------------------------------------------------------------


			# Test 3.11 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Rename the test dataset",
													function_description = "Session.rename_dataset",
											test_function = app.session.rename_dataset("Test Dataset", "New Name"),
											expected_result = "Dataset 'Test Dataset' successfully renamed to 'New Name'",
											print_verbose = (verbosity >= 3)))

			# Test 3.11 End ------------------------------------------------------------------------------------


			# Test 3.12 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Fail to compile the old dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.session.compile_dataset("Test Dataset"),
											expected_result = "Invalid tag: 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 3.12 End ------------------------------------------------------------------------------------


			# Test 3.13 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the new dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.session.compile_dataset("New Name"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 3.13 End ------------------------------------------------------------------------------------


			# Test 3.14 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Completely remove the test dataset",
													function_description = "Session.remove_dataset",
											test_function = app.session.remove_dataset("New Name"),
											expected_result = "Dataset 'New Name' successfully removed",
											print_verbose = (verbosity >= 3)))

			# Test 3.14 End ------------------------------------------------------------------------------------

		# Print the test results

		if verbosity >= 2:

			output_text = ""

			for result in results:
				output_text += result.output["text"]
				output_text += f"\n"

			print(output_text)

		# Print the result summary

		if verbosity >= 1:

			passed_tests = 0
			failed_tests = 0

			for result in results:
				if result.output["passed"] == True:
					passed_tests += 1
				else:
					failed_tests += 1

			summary = f"\nHeadless Test Summary :---:\n\n\tPassed: {passed_tests}\n\tFailed: {failed_tests}\n"

			print(summary)

		# Print if any tests failed or not
		else:
			for result in results:
				if result.output["passed"] == False:
					print(f"\nHeadless Test Failed\n")
					return
			
			print(f"\nHeadless Test Passed\n")