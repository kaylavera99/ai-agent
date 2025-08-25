import os
from google.genai import types
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file


def get_files_info(working_directory, directory = "."):
    full_path = os.path.join(working_directory,directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' 
    
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        contents = os.listdir(abs_path)
    except Exception as e:
        return f'Error: {str(e)}'
    

    output_lines = []
    for item in os.listdir(abs_path):
        item_path = os.path.join(abs_path, item)
        try:
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
            output_lines.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
        except Exception as e:
            output_lines.append(f'- {item}: Error: {str(e)}')


    return "\n".join(output_lines)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)







