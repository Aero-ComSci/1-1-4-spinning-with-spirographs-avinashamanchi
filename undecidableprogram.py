def halting_problem_simulator(program, input):
    """
    This function simulates a decision problem.
    """
    try:
        exec(program)  
    except Exception as e:
        print("The program threw an exception, which means it might be in an infinite loop.")

# Example usage
program_code = """
def run():
    while True:
        pass  

run()
"""

input_data = ""  

halting_problem_simulator(program_code, input_data)
