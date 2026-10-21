# Executes a specified test and returns the results
class Test:

	# test_name = The natural language description of what the test is doing (e.g. Get the name of the current session)
	# function_description = The high level format of the function being called (e.g. Session.get_session instead of app.sm.sessions[0].get_session())
	# test_function = The call to the exact function being tested (e.g. app.sm.sessions[0].get_session("Test Session"))
	# expected_result = The output that the function needs to return for the test to be considered a successful execution (e.g. {"name": "Test Session", "data": ["a", "b", "c"]})
	# print_verbose = Inherited from the headless runner, tells the test whether or not to return the extra details of its run
	def __init__(self, test_name, function_description, test_function, expected_result, print_verbose):
		output = {"text": "", "passed": False}

		output["text"] += f"\n\n\033[1m{test_name}\033[0m - "

		result = test_function

		if print_verbose:
				output["text"] += f"\n\tFunction: {function_description}"
				output["text"] += f"\n\tExpected Result: |{expected_result}|"
				output["text"] += f"\n\tActual Result: |{result}|"

		valid_result = True
		# If the result or expected output is None, or the result if a string, check for a direct match
		if result == None or expected_result == None or type(result) == str:
			valid_result = (result == expected_result)
     
		else:
			# Check that the result of the function contains all of the expected items
			for entry in result:
					if entry not in expected_result:
						valid_result = False

		if valid_result:
				output["text"] += f"\n\033[92mPassed\033[0m"
				output["passed"] = True
		else:
				output["text"] += f"\n\033[91mFailed\033[0m"
				output["passed"] = False

		self.output = output