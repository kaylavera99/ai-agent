# Main functions for the new mini-app and entry point the AI agent calls. 
# The AI Agent will call these functions as needed.


from pkg.new_app_template import example_function, another_function

# optional: define a dictionary mapping for dynamic function calls
FUNCTION_MAP = {
    "example_function": example_function,
    "another_function": another_function,
}

# optional: allow running as a script
if __name__ == "__main__":
    print(example_function("Test"))
    print(another_function(2, 3))