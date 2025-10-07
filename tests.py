from functions.run_python import run_python_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

print("Testing the 'run_pytyhon_file' function with various scenarios:")
print("CALCULATOR TESTS")
print(run_python_file(working_directory=".", file_path="calculator/tests.py"))

print("CONVERTER TESTS")
print(run_python_file(working_directory=".", file_path="converter/main.py"))
print(run_python_file(working_directory=".", file_path="converter/main.py", args=['convert 10 meters to feet']))
print(run_python_file(working_directory=".", file_path="converter/tests.py"))

print("Running python files completed.\n")

print("Testing get_file_content function with various scenarios:")
print(get_file_content(working_directory=".", file_path="calculator/main.py"))
print(get_file_content(working_directory=".", file_path="converter/main.py"))

print("Getting file content completed.\n")

print("Testing get_file_info function with various scenarios:")
print(get_files_info(working_directory=".", directory="calculator"))
print(get_files_info(working_directory=".", directory="converter"))

print("Getting file info completed.\n")