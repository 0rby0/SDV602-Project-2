# Executes a specified test and returns the results
class Test:

    # test_name = The natural language description of what the test is doing (e.g. Get the name of the current session)
    # function_description = The high level format of the function being called (e.g. Session.get_session instead of app.sm.sessions[0].get_session())
    # test_function = The call to the exact function being tested (e.g. app.sm.sessions[0].get_session("Test Session"))
    # expected_result = The output that the function needs to return for the test to be considered a successful execution (e.g. {"name": "Test Session", "data": ["a", "b", "c"]})
    # print_verbose = Inherited from the headless runner, tells the test whether or not to return the extra details of its run
    def __init__(self, test_name, function_description, test_function, expected_result, print_verbose):
        output = {"text": "", "passed": False}

        output["text"] += f"\n\n{test_name} - "

        result = test_function

        if print_verbose:
            output["text"] += f"\n\tFunction: {function_description}"
            output["text"] += f"\n\tExpected Result: {expected_result}"
            output["text"] += f"\n\tActual Result: {result}"

        if result == expected_result:
            output["text"] += f"\nPassed"
            output["passed"] = True
        else:
            output["text"] += f"\nFailed"
            output["passed"] = False

        self.output = output